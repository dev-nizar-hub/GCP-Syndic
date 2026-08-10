import os
import glob
import re

public_dir = "c:/xampp/htdocs/GCP Syndic Website v2/public"
html_files = glob.glob(os.path.join(public_dir, '*.html'))

unsplash_copro = "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=600&q=80&auto=format&fit=crop"
new_img_tag = f'<img src="{unsplash_copro}" width="600" height="520" alt="Gestion de copropriété" style="object-fit:cover; border-radius:8px; width:100%; height:auto;" loading="lazy">'

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original = content
        
        # 1. Fix grammatical error
        content = content.replace("de le Maroc", "du Maroc")
        content = content.replace("de Le Maroc", "du Maroc")
        
        # 2. Replace the broken copro.jpg image tag completely
        # Find the <img ... src="...copro.jpg"...> tag
        content = re.sub(r'<img[^>]*src="[^"]*copro\.jpg"[^>]*>', new_img_tag, content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed {os.path.basename(filepath)}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

print("Done fixing texts and missing images.")
