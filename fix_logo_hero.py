import re
import glob

html_files = glob.glob('public/*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    original = html

    # 1. Replace the old Atrium logo SVG/PNG with our new GCP logo
    html = html.replace(
        '/assets/wp-content/uploads/2020/10/Logo_Atrium_Gestion_long_sign_300px-1.svg',
        '/logo.png'
    )
    html = html.replace(
        '/assets/wp-content/uploads/2019/11/logo-400.png',
        '/logo.png'
    )
    # Remove old logo srcset (it'll cause broken paths)
    html = re.sub(r' srcset="[^"]*logo[^"]*"', '', html)

    # 2. Replace hero background image with our local Grand Theatre photo
    html = html.replace(
        '/assets/wp-content/uploads/2025/03/home-2025.webp',
        '/Quality%20Restoration-Ultra%20HD-Grand-Theatre-of-Rabat-Morocco-1024x546.jpeg'
    )
    html = html.replace(
        '/assets/wp-content/uploads/2025/03/home-2025-mob.webp',
        '/Quality%20Restoration-Ultra%20HD-Grand-Theatre-of-Rabat-Morocco-1024x546.jpeg'
    )

    # 3. Also fix the &quot; encoding in background-image URLs (already decoded by smart_color_fix)
    # The hero bg may use HTML-encoded quotes like &quot; — fix to regular quotes
    html = html.replace('url(&quot;', 'url("').replace('&quot;)', '")')

    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Fixed: {filepath}')
    else:
        print(f'No change: {filepath}')

print('\nDone. Logo and hero background image fixed on all pages.')
