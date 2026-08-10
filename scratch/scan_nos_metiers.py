import os
import re
import glob

public_dir = "public"
html_files = glob.glob(os.path.join(public_dir, '*.html'))
nos_metiers_files = [f for f in html_files if 'nos-metiers' in os.path.basename(f)]

print("=== SCANNING NOS METIERS FILES ===")
for filepath in sorted(nos_metiers_files):
    name = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    imgs = re.findall(r'src=["\'](/assets/[^"\']+)["\']', content)
    links = re.findall(r'href=["\'](?!http|#|mailto|tel|javascript)([^"\']+)["\']', content)
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else 'No Title'
    
    print(f"\n--- {name} ---")
    print(f"Title: {title}")
    print(f"Size: {len(content):,} bytes")
    print(f"Total Local Images: {len(imgs)}")
    print(f"Total Local Links: {len(links)}")
    
    # Check for missing images
    missing_imgs = []
    for img in set(imgs):
        local_path = 'public' + img.replace('%20', ' ')
        if not os.path.exists(local_path):
            missing_imgs.append(img)
            
    if missing_imgs:
        print("Missing Images:")
        for m in missing_imgs:
            print(f"  [MISSING] {m}")
    else:
        print("All local images exist.")
