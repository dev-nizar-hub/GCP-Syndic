import re

with open('public/atrium.html', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Find the full style attribute containing awb-background-image
matches = re.findall(r'style="[^"]{0,600}awb-background[^"]{0,600}"', html)
for m in matches[:3]:
    print(repr(m[:600]))
    print()
