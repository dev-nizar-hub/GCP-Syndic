import glob
import re

BRAND_LINK = '    <link rel="stylesheet" href="/assets/gcp-brand.css" />\n'

html_files = glob.glob('public/*.html')
updated = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove any previous brand link injection
    html = html.replace(BRAND_LINK, '')

    # Also replace logo references
    old_logo_patterns = [
        (r'https://atrium-gestion\.fr/wp-content/uploads/2022/03/picto-atrium\.png', '/logo.png'),
        (r'https://atrium-gestion\.fr/wp-content/uploads/2024/12/picto-atrium\.jpg', '/logo.png'),
        (r'/assets/wp-content/uploads/2022/03/picto-atrium\.png', '/logo.png'),
        (r'/assets/wp-content/uploads/2024/12/picto-atrium\.jpg', '/logo.png'),
    ]
    for pattern, replacement in old_logo_patterns:
        html = re.sub(pattern, replacement, html)

    # Inject the brand CSS link LAST in head (so it overrides all other CSS)
    if '</head>' in html:
        html = html.replace('</head>', BRAND_LINK + '</head>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    updated += 1
    print(f"Updated: {filepath}")

print(f"\nDone! Brand CSS injected into {updated} pages.")
