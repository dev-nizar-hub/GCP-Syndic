import os
import glob
import re

public_dir = 'public'
html_files = glob.glob(os.path.join(public_dir, '*.html'))

for filepath in html_files:
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Clean up lingering uppercase ATRIUM references
    content = re.sub(r'ATRIUM GESTION LEVALLOIS', 'GCP Syndic Maroc', content)
    content = re.sub(r'ATRIUM GESTION', 'GCP Syndic', content)
    content = re.sub(r'ATRIUM', 'GCP Syndic', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
