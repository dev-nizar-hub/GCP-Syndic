import os
import re
import glob

public_dir = "public"
html_files = glob.glob(os.path.join(public_dir, '*.html'))

# Keywords to find map / agences / location image references
keywords = ['marqueur', 'map', 'carte', 'agence', 'plan', 'contact-map', 'paris.svg', 'paris.png']

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        imgs = re.findall(r'src="([^"]+)"', content)
        for img in imgs:
            if any(kw in img.lower() for kw in keywords):
                print(f"{os.path.basename(filepath)}: {img}")
    except Exception as e:
        print(f"Error: {filepath}: {e}")
