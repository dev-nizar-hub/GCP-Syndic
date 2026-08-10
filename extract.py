import re

with open('public/atrium.html', 'r', encoding='utf-8') as f:
    html = f.read()

links = set(re.findall(r'https://atrium-gestion\.fr/[^\s"\'<>]+', html))

with open('scratch_links.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(links)))
