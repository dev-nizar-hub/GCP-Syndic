import os
from bs4 import BeautifulSoup

def clean_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    changed = False
    
    # 1. Remove old Avada footer
    old_footers = soup.find_all(class_='fusion-tb-footer')
    for f in old_footers:
        f.decompose()
        changed = True
        
    # 2. Remove broken modal popups / frm_show_form sections
    frm_widgets = soup.find_all(id=lambda x: x and x.startswith('frm_show_form'))
    for widget in frm_widgets:
        widget.decompose()
        changed = True
        
    # 3. Remove stray modal containers just in case
    modals = soup.find_all(class_='fusion-modal')
    for modal in modals:
        modal.decompose()
        changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Cleaned {os.path.basename(filepath)}")
    else:
        print(f"No garbage found in {os.path.basename(filepath)}")

public_dir = "public"
for filename in os.listdir(public_dir):
    if filename.endswith(".html"):
        clean_html_file(os.path.join(public_dir, filename))
