import glob

files = glob.glob('public/*.html')
count = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        html = fh.read()
    
    original = html
    
    # Revert header logo from 192px to 120px (user originally asked to make 80px bigger by 50% = 120px)
    html = html.replace('height:192px;width:auto;object-fit:contain', 'height:120px;width:auto;object-fit:contain')
    
    # Now correctly target the footer logo
    # The current footer CSS is: .gcp-footer-logo img{height:52px;width:auto;object-fit:contain;filter:brightness(0) invert(1);margin-bottom:20px}
    # 52px * 1.6 = 83px
    html = html.replace('.gcp-footer-logo img{height:52px;', '.gcp-footer-logo img{height:83px;')
    # Also replace any inline styles if they exist (just in case)
    # The actual HTML is usually <div class="gcp-footer-logo"><img alt="GCP Syndic" src="/logo-transparent.png"/></div>
    
    if html != original:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(html)
        count += 1
        print('Fixed: ' + f)

print('Total fixed: ' + str(count))
