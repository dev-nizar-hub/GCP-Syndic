import re

files = ['public/nos-biens-achat.html', 'public/nos-biens-location.html']

# This pattern looks for the column containing the "Nouvelle recherche" title
# and the following column containing the form, up to the end of that form.
pattern = re.compile(
    r'<div class="fusion-layout-column fusion_builder_column fusion-builder-column-12[^>]+>\s*'
    r'<div class="fusion-column-wrapper[^>]+>\s*'
    r'<div class="fusion-title[^>]+id="tr1"[^>]*>.*?'
    r'<h2[^>]*>Nouvelle recherche</h2>.*?'
    r'</div>\s*</div>\s*</div>\s*'
    r'<div class="fusion-layout-column fusion_builder_column fusion-builder-column-13[^>]+>\s*'
    r'<div class="fusion-column-wrapper[^>]+>\s*'
    r'<div class="fusion-text[^>]+>\s*'
    r'<div class="frm_forms[^>]+>\s*'
    r'<form.*?</form>\s*'
    r'</div>\s*</div>\s*</div>\s*</div>',
    re.DOTALL
)

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    new_content, count = pattern.subn('', content)
    
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(new_content)
    
    print(f'{f}: removed {count} Nouvelle recherche blocks')
