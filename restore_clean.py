import glob
import re

# Re-download all pages fresh and apply ONLY the safe link replacement
import urllib.request

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

def safe_process(html):
    """Replace ONLY URLs - never touch color values or text content"""
    # Replace asset URLs
    html = re.sub(r'https://atrium-gestion\.fr/(wp-content/[^\s"\'<>]+)', r'/assets/\1', html)
    html = re.sub(r'https://atrium-gestion\.fr/(wp-includes/[^\s"\'<>]+)', r'/assets/\1', html)
    # Strip version query params from local assets
    html = re.sub(r'(/assets/[^\s"\'<>]+\.(?:css|js|png|jpg|jpeg|svg|webp|woff|woff2|ttf|gif))\?[^\s"\'<>]+', r'\1', html)
    # Replace page links
    for old_url, new_url in link_replacements.items():
        html = html.replace(old_url, new_url)
    # Replace remaining atrium links with #
    html = re.sub(r'https://atrium-gestion\.fr/[^\s"\'<>]*', '#', html)
    return html

for url, filepath in routes.items():
    print(f"Fetching fresh: {url}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
        html = safe_process(html)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Saved: {filepath}")
    except Exception as e:
        print(f"  FAILED: {url}: {e}")

print("\nDone! All pages restored to clean state.")
