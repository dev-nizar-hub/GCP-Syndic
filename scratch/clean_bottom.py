import re

files = ['public/nos-biens-achat.html', 'public/nos-biens-location.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    # 1. Update the CSS to center columns 12 and 13 for Nouvelle recherche
    content = content.replace(
        '.fusion-builder-column-9, .fusion-builder-column-10 {',
        '.fusion-builder-column-9, .fusion-builder-column-10, .fusion-builder-column-12, .fusion-builder-column-13 {'
    )
    content = content.replace(
        '.fusion-builder-column-9 .fusion-column-wrapper {',
        '.fusion-builder-column-9 .fusion-column-wrapper, .fusion-builder-column-12 .fusion-column-wrapper {'
    )
    
    # 2. Remove the broken raw contact forms
    # We look for <div class="gcp-modal-body"> up to </div>\n</div>\n</div> or similar.
    # The block starts with <div class="gcp-modal-body"> and ends with </button>\n    </div>\n  </div>\n</div>
    contact_form_pattern = re.compile(
        r'<div class="gcp-modal-body">\s*<h4>Remplissez vos coordonnees pour etre contacte :</h4>.*?</button>\s*</div>\s*</div>\s*</div>',
        re.DOTALL
    )
    
    content, count = contact_form_pattern.subn('', content)
    
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(content)
        
    print(f'{f}: Removed {count} contact forms')
