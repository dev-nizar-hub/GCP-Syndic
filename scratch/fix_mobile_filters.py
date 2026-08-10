import glob

files = ['public/nos-biens-achat.html', 'public/nos-biens-location.html']

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # The issue: min-width: 180px and max-width: 260px causes overlap on very small screens.
    # Let's just add a media query for the filter bar to stack elements on small screens.
    
    # Let's insert a media query inside the <style> block that contains the filter CSS.
    # The filter CSS has "/* ===== FILTER BAR ===== */"
    
    if '/* ===== MOBILE FILTER BAR FIX ===== */' not in html:
        # We can append it just before </style> that comes after "/* ===== FILTER BAR ===== */"
        
        fix_css = """
/* ===== MOBILE FILTER BAR FIX ===== */
@media (max-width: 600px) {
  .frm_pro_form .frm_fields_container {
    flex-direction: column !important;
    align-items: stretch !important;
    padding: 0 15px !important;
  }
  .frm_form_field.frm_fourth {
    min-width: 100% !important;
    max-width: 100% !important;
  }
  .frm_button_submit {
    width: 100% !important;
  }
}
"""
        # Find the </style> tag that follows "/* ===== FILTER BAR ===== */"
        filter_start = html.find('/* ===== FILTER BAR ===== */')
        if filter_start != -1:
            style_end = html.find('</style>', filter_start)
            if style_end != -1:
                html = html[:style_end] + fix_css + html[style_end:]
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(html)
                print('Fixed mobile filter layout in:', fpath)
            else:
                print('Could not find </style> after filter bar in', fpath)
        else:
            print('Could not find filter bar section in', fpath)
