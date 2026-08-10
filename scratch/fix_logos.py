import glob

files = glob.glob('public/*.html')
count = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        html = fh.read()
    
    original = html
    
    # Target the footer logo
    # The current footer CSS is: .gcp-footer-logo img{height:83px;...
    # Original was 52px. 400% of 52px = 208px.
    html = html.replace('.gcp-footer-logo img{height:83px;', '.gcp-footer-logo img{height:208px;')
    
    if html != original:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(html)
        count += 1
        print('Fixed: ' + f)

print('Total fixed: ' + str(count))
