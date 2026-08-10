import glob
import re

files = glob.glob('public/*.html')
count = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        html = fh.read()

    original = html

    # Replace any existing favicon link tags
    # Handles .ico, .png, .gif etc.
    html = re.sub(
        r'<link[^>]+rel=["\'](?:shortcut icon|icon)["\'][^>]*>',
        '',
        html,
        flags=re.IGNORECASE
    )
    html = re.sub(
        r'<link[^>]+href=["\'][^"\']*favicon[^"\']*["\'][^>]*>',
        '',
        html,
        flags=re.IGNORECASE
    )

    # Inject new favicon right after <head>
    new_favicon = '<link rel="icon" type="image/png" href="/favicon.png">'
    html = html.replace('<head>', '<head>\n' + new_favicon, 1)

    if html != original:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(html)
        count += 1
        print('Updated: ' + f)

print('Total updated: ' + str(count))
