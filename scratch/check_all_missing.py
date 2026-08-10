import os
import re
import glob

public_dir = "public"
html_files = glob.glob(os.path.join(public_dir, '*.html'))

missing_all = set()

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        imgs = re.findall(r'src="(/assets/[^"]+)"', content)
        for img in imgs:
            local = 'public' + img.replace('%20', ' ')
            if not os.path.exists(local):
                missing_all.add(img)
    except Exception as e:
        print(f"Error: {filepath}: {e}")

print(f"\n=== ALL MISSING IMAGES ACROSS SITE ({len(missing_all)}) ===")
for m in sorted(missing_all):
    print(m)
