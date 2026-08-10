import os
import re

with open('public/nos-metiers-syndic.html', 'r', encoding='utf-8') as f:
    content = f.read()

imgs = re.findall(r'src="(/assets/[^"]+)"', content)
missing = []
for img in set(imgs):
    local = 'public' + img.replace('%20', ' ')
    if not os.path.exists(local):
        missing.append(img)
    else:
        print('OK:', img)

print()
print('MISSING:')
for m in missing:
    print(m)
