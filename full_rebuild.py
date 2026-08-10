import re
import urllib.request
import glob

# Brand link to inject
BRAND_LINK = '    <link rel="stylesheet" href="/assets/gcp-brand.css" />\n'

link_replacements = {
    'https://atrium-gestion.fr/contact/': '/contact.html',
    'https://atrium-gestion.fr/nos-metiers/': '/nos-metiers.html',
    'https://atrium-gestion.fr/nos-metiers/syndic-de-copropriete/': '/nos-metiers-syndic.html',
    'https://atrium-gestion.fr/nos-metiers/gestion-locative/': '/nos-metiers-gestion-locative.html',
    'https://atrium-gestion.fr/nos-metiers/vente/': '/nos-metiers-vente.html',
    'https://atrium-gestion.fr/nos-metiers/location/': '/nos-metiers-location.html',
    'https://atrium-gestion.fr/nos-metiers/assurances/': '/nos-metiers-assurances.html',
    'https://atrium-gestion.fr/nos-biens/achat/': '/nos-biens-achat.html',
    'https://atrium-gestion.fr/nos-biens/location/': '/nos-biens-location.html',
    'https://atrium-gestion.fr/notre-maison/': '/notre-maison.html',
    'https://atrium-gestion.fr/nous-rejoindre/': '/nous-rejoindre.html',
    'https://atrium-gestion.fr/nouvel-espace-client-progestra/': '/espace-client.html',
    'https://atrium-gestion.fr/': '/',
}

# Hero background - use single quotes inside url() to avoid breaking the outer style="..."
HERO_BG_URL = "/Quality Restoration-Ultra HD-Grand-Theatre-of-Rabat-Morocco-1024x546.jpeg"

routes = {
    'https://atrium-gestion.fr/': 'public/atrium.html',
    'https://atrium-gestion.fr/contact/': 'public/contact.html',
    'https://atrium-gestion.fr/nos-metiers/': 'public/nos-metiers.html',
    'https://atrium-gestion.fr/nos-metiers/syndic-de-copropriete/': 'public/nos-metiers-syndic.html',
    'https://atrium-gestion.fr/nos-metiers/gestion-locative/': 'public/nos-metiers-gestion-locative.html',
    'https://atrium-gestion.fr/nos-metiers/vente/': 'public/nos-metiers-vente.html',
    'https://atrium-gestion.fr/nos-metiers/location/': 'public/nos-metiers-location.html',
    'https://atrium-gestion.fr/nos-metiers/assurances/': 'public/nos-metiers-assurances.html',
    'https://atrium-gestion.fr/nos-biens/achat/': 'public/nos-biens-achat.html',
    'https://atrium-gestion.fr/nos-biens/location/': 'public/nos-biens-location.html',
    'https://atrium-gestion.fr/notre-maison/': 'public/notre-maison.html',
    'https://atrium-gestion.fr/nous-rejoindre/': 'public/nous-rejoindre.html',
    'https://atrium-gestion.fr/nouvel-espace-client-progestra/': 'public/espace-client.html',
}

import math

WHITE     = (255, 255, 255)
DARK_BLUE = (10,  38,  49)
BLUE      = (49,  123, 255)
BRAND     = [WHITE, DARK_BLUE, BLUE]
BRAND_HEX = ['#ffffff', '#0a2631', '#317bff']

def hex_to_rgb(h):
    h = h.lstrip('#')
    if len(h) == 3: h = ''.join(c*2 for c in h)
    if len(h) != 6: return None
    try: return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    except: return None

def closest(hex_code):
    rgb = hex_to_rgb(hex_code)
    if rgb is None: return hex_code
    dists = [math.sqrt(sum((a-b)**2 for a,b in zip(rgb, brand))) for brand in BRAND]
    return BRAND_HEX[dists.index(min(dists))]

def replace_in_style_blocks(html):
    def replace_block(m):
        block = m.group(0)
        block = re.sub(r'#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}\b', lambda hm: closest(hm.group(0)), block)
        def repl_rgb(rm):
            r,g,b = int(rm.group(1)),int(rm.group(2)),int(rm.group(3))
            dists = [math.sqrt(sum((a-b_)**2 for a,b_ in zip((r,g,b), brand))) for brand in BRAND]
            return BRAND_HEX[dists.index(min(dists))]
        block = re.sub(r'rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)', repl_rgb, block)
        return block
    return re.sub(r'<style[^>]*>.*?</style>', replace_block, html, flags=re.DOTALL)

def replace_in_style_attrs(html):
    """Only replace colors within style="..." attrs, but preserve url() contents"""
    def replace_style(m):
        style_content = m.group(1)
        # Split out url() parts to avoid touching them
        parts = re.split(r'(url\([^)]*\))', style_content)
        new_parts = []
        for part in parts:
            if part.startswith('url('):
                new_parts.append(part)  # Don't touch urls
            else:
                # Replace hex colors
                part = re.sub(r'#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}\b', lambda hm: closest(hm.group(0)), part)
                # Replace rgb
                def repl_rgb(rm):
                    r,g,b = int(rm.group(1)),int(rm.group(2)),int(rm.group(3))
                    dists = [math.sqrt(sum((a-b_)**2 for a,b_ in zip((r,g,b), brand))) for brand in BRAND]
                    return BRAND_HEX[dists.index(min(dists))]
                part = re.sub(r'rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)', repl_rgb, part)
                new_parts.append(part)
        return ' style="' + ''.join(new_parts) + '"'
    return re.sub(r' style="([^"]*)"', replace_style, html)

for url, filepath in routes.items():
    print(f"Processing {url}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')

        # 1. Replace asset URLs
        html = re.sub(r'https://atrium-gestion\.fr/(wp-content/[^\s"\'<>]+)', r'/assets/\1', html)
        html = re.sub(r'https://atrium-gestion\.fr/(wp-includes/[^\s"\'<>]+)', r'/assets/\1', html)
        html = re.sub(r'(/assets/[^\s"\'<>]+\.(?:css|js|png|jpg|jpeg|svg|webp|woff|woff2|ttf|gif))\?[^\s"\'<>]+', r'\1', html)

        # 2. Replace page links
        for old_url, new_url in link_replacements.items():
            html = html.replace(old_url, new_url)
        html = re.sub(r'https://atrium-gestion\.fr/[^\s"\'<>]*', '#', html)

        # 3. Replace old logos
        html = html.replace('/assets/wp-content/uploads/2020/10/Logo_Atrium_Gestion_long_sign_300px-1.svg', '/logo.png')
        html = html.replace('/assets/wp-content/uploads/2019/11/logo-400.png', '/logo.png')
        html = re.sub(r' srcset="[^"]*logo[^"]*"', '', html)

        # 4. Replace hero bg with local image - use &quot; safe encoding
        # The original uses url(&quot;path&quot;) - keep &quot; to avoid breaking style=""
        html = html.replace(
            '/assets/wp-content/uploads/2025/03/home-2025.webp&quot;)',
            '/Quality%20Restoration-Ultra%20HD-Grand-Theatre-of-Rabat-Morocco-1024x546.jpeg&quot;)'
        )
        html = html.replace(
            '/assets/wp-content/uploads/2025/03/home-2025-mob.webp&quot;)',
            '/Quality%20Restoration-Ultra%20HD-Grand-Theatre-of-Rabat-Morocco-1024x546.jpeg&quot;)'
        )

        # 5. Apply smart color replacement (preserving url() contents)
        html = replace_in_style_blocks(html)
        html = replace_in_style_attrs(html)

        # 6. Inject brand CSS last in head
        html = html.replace('</head>', BRAND_LINK + '</head>')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Saved: {filepath}")
    except Exception as e:
        print(f"  FAILED {url}: {e}")

print("\nAll done!")
