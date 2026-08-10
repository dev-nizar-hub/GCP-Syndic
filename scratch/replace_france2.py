import os
import re

search_dir = "c:/xampp/htdocs/GCP Syndic Website v2/public"

replacements = [
    ("PARIS II", "RABAT II"),
    ("PARIS 15ème", "Meknès"),
    ("-au-studio-harcourt-paris/", "-au-studio-harcourt-maroc/"),
    ("AgenceImmoParis", "AgenceImmoMaroc"),
]

for root, dirs, files in os.walk(search_dir):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                new_content = content
                for old, new in replacements:
                    new_content = new_content.replace(old, new)
                
                if content != new_content:
                    with open(path, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    print(f"Updated: {f}")
            except Exception as e:
                print(f"Error processing {path}: {e}")

print("Final replacement complete.")
