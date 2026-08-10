import re

with open('public/atrium.html', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Find the hero section style
heroes = re.findall(r'awb-background-image[^"\']{0,300}', html)
print('=== HERO BG ===')
for h in heroes[:3]:
    print(repr(h[:300]))

# Find the logo img tag full
print('\n=== LOGO IMG FULL ===')
logos = re.findall(r'<img[^>]{0,500}logo\.png[^>]*>', html, re.IGNORECASE)
for l in logos:
    print(repr(l))

# Check if logo.png actually exists in public
import os
print('\n=== PUBLIC FILES ===')
for f in os.listdir('public'):
    if 'logo' in f.lower() or 'quality' in f.lower():
        print(f)
