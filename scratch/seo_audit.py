import glob, re

files = sorted(glob.glob('public/*.html'))
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        html = fh.read()
    title = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
    desc = re.search(r'name="description"[^>]*content="([^"]*)"', html, re.IGNORECASE)
    if not desc:
        desc = re.search(r'content="([^"]*)"[^>]*name="description"', html, re.IGNORECASE)
    og = 'og:title' in html
    canon = 'canonical' in html
    name = f.split('\\')[-1]
    print(name)
    print('  title:', title.group(1).strip()[:70] if title else 'MISSING')
    print('  desc:', desc.group(1)[:70] if desc else 'MISSING')
    print('  OG tags:', 'yes' if og else 'MISSING')
    print('  canonical:', 'yes' if canon else 'MISSING')
    print()
