import re

with open('public/nos-metiers-syndic.html', 'r', encoding='utf-8') as f:
    content = f.read()

images = re.findall(r'<img[^>]+>', content)
for img in images:
    src_match = re.search(r'src="([^"]+)"', img)
    if src_match:
        print(src_match.group(1))
    else:
        print("No src:", img)
