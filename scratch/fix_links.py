import os
import glob
import re

public_dir = 'public'
html_files = glob.glob(os.path.join(public_dir, '*.html'))

replacements = {
    r'/nos-metiers\.htmlsyndic-de-copropriete/?': '/nos-metiers-syndic.html',
    r'/nos-metiers\.htmlgestion-locative/?': '/nos-metiers-gestion-locative.html',
    r'/nos-metiers\.htmlvente/?': '/nos-metiers-vente.html',
    r'/nos-metiers\.htmllocation/?': '/nos-metiers-location.html',
    r'/nos-metiers\.htmlassurances/?': '/nos-metiers-assurances.html'
}

for filepath in html_files:
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original_content = content
    total_replaced = 0

    for pattern, replacement in replacements.items():
        content, count = re.subn(pattern, replacement, content)
        total_replaced += count

    if total_replaced > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"FIXED {filename}: {total_replaced} links updated")
    else:
        print(f"OK    {filename}")

print("\nDone!")
