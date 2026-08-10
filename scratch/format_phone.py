import glob
import re

html_files = glob.glob('public/*.html')

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace the visible text
    new_html = html.replace('>07 08 06 61 88<', '>+212 7 08 06 61 88<')
    
    if new_html != html:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print('Updated:', fpath)
