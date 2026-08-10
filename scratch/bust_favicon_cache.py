import glob

files = glob.glob('public/*.html')
count = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        html = fh.read()
    
    original = html
    
    # Update favicon cache buster
    html = html.replace('href="/favicon.png"', 'href="/favicon.png?v=2"')
    
    if html != original:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(html)
        count += 1
        print('Updated: ' + f)

print('Total updated: ' + str(count))
