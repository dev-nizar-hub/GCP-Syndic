import re

with open('public/atrium.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace asset URLs (wp-content, wp-includes, etc.) with local equivalents
# We'll replace "https://atrium-gestion.fr/" with "/assets/" ONLY for asset paths (wp-content, wp-includes).
html = re.sub(r'https://atrium-gestion\.fr/(wp-content/[^\s"\'<>]+)', r'/assets/\1', html)
html = re.sub(r'https://atrium-gestion\.fr/(wp-includes/[^\s"\'<>]+)', r'/assets/\1', html)

# Also strip the query params (?ver=...) from the newly replaced /assets/ paths so they match local filenames
# We use a regex that finds /assets/ path ending with some extension, followed by ?... and removes the ?...
html = re.sub(r'(/assets/[^\s"\'<>]+\.(?:css|js|png|jpg|jpeg|svg|webp|woff|woff2|ttf|gif))\?[^\s"\'<>]+', r'\1', html)

# 2. Replace internal page links to point locally (e.g. /contact.html instead of https://atrium-gestion.fr/contact/)
# We'll map the main ones
routes = {
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

for old_url, new_url in routes.items():
    html = html.replace(old_url, new_url)

# Replace any remaining atrium-gestion.fr links with # (to prevent external navigation)
html = re.sub(r'https://atrium-gestion\.fr/[^\s"\'<>]*', '#', html)

with open('public/atrium.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Replaced all links in atrium.html")
