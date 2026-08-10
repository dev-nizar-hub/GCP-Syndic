import re

with open('public/atrium.html', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Find the logo src
logos = re.findall(r'<img[^>]*logo[^>]*>', html, re.IGNORECASE)
print('=== LOGO IMGS ===')
for l in logos:
    print(l[:200])

# Find background-image
print('\n=== BACKGROUND IMAGES ===')
bgs = re.findall(r'background-image[^;"\)]{0,300}', html)
for bg in bgs[:10]:
    print(bg[:200])

# Find hero/slider section
print('\n=== HERO SECTION (awb-background) ===')
heroes = re.findall(r'awb-background[^"]{0,300}', html)
for h in heroes[:5]:
    print(h[:200])

# Find 2025/03 or home images
print('\n=== HOME BG IMAGES ===')
home_imgs = re.findall(r'home[^"\'<>]{0,100}', html, re.IGNORECASE)
for h in home_imgs[:5]:
    print(h[:200])
