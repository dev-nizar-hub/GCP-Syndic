import glob

files = glob.glob('public/*.html')
count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        html = fh.read()
    if 'logo-transparent.png' in html and 'height:80px' in html:
        new_html = html.replace('height:80px;width:auto;object-fit:contain', 'height:120px;width:auto;object-fit:contain')
        if new_html != html:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(new_html)
            count += 1
            print('Updated: ' + f)
print('Total updated: ' + str(count))
