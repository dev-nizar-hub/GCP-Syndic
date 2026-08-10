import glob
import os

# 1. Rename atrium.html to index.html
if os.path.exists('public/atrium.html'):
    os.rename('public/atrium.html', 'public/index.html')
    print('Renamed public/atrium.html to public/index.html')

# 2. Replace occurrences of "atrium.html" across all files
files = glob.glob('public/*.html') + ['public/sitemap.xml']

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace absolute and relative links
        new_content = content.replace('/atrium.html', '/index.html')
        new_content = new_content.replace('"atrium.html"', '"index.html"')
        new_content = new_content.replace('www.gcp-syndic.ma/atrium.html', 'www.gcp-syndic.ma/index.html')
        
        if new_content != content:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print('Updated references in:', fpath)
