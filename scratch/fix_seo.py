"""
Fix SEO for pages missing tags, add sitemap.xml and robots.txt.
"""
import glob, re

DOMAIN = "https://www.gcp-syndic.ma"

# ── Per-page SEO data ────────────────────────────────────────────────────────
PAGE_SEO = {
    "contact.html": {
        "title": "Contactez GCP Syndic | Agence Immobilière Meknès Maroc",
        "description": "Contactez GCP Syndic par téléphone, email ou formulaire. Notre équipe à Meknès vous répond rapidement pour vos projets immobiliers au Maroc.",
        "og_title": "Contactez GCP Syndic | Agence Immobilière Meknès",
        "og_desc": "Contactez GCP Syndic par téléphone, email ou formulaire. Agence immobilière à Meknès.",
        "canonical": f"{DOMAIN}/contact.html",
    },
    "demande-bien.html": {
        "title": "Demande de Bien Immobilier | GCP Syndic Maroc",
        "description": "Vous êtes intéressé par un bien GCP Syndic ? Remplissez ce formulaire et nous vous contacterons via WhatsApp pour finaliser votre demande.",
        "og_title": "Demande de Bien Immobilier | GCP Syndic",
        "og_desc": "Contactez-nous via WhatsApp pour votre demande de bien immobilier à Meknès et dans les villes du Maroc.",
        "canonical": f"{DOMAIN}/demande-bien.html",
    },
    "nos-metiers.html": {
        "description": "GCP Syndic vous propose syndic de copropriété, location, gestion locative, assurances et vente immobilière à Meknès et dans tout le Maroc.",
    },
}

def make_og_tags(title, desc, canonical, img=None):
    if img is None:
        img = f"{DOMAIN}/logo-transparent.png"
    return f"""  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{img}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <link rel="canonical" href="{canonical}">"""

files = glob.glob('public/*.html')
updated = []

for fpath in files:
    fname = fpath.split('\\')[-1]
    if fname not in PAGE_SEO:
        continue
    
    seo = PAGE_SEO[fname]
    
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original = html
    
    # Update title if specified
    if 'title' in seo:
        html = re.sub(r'<title>.*?</title>', f'<title>{seo["title"]}</title>', html, flags=re.DOTALL)
    
    # Update or add description
    if 'description' in seo:
        new_desc = f'<meta name="description" content="{seo["description"]}">'
        if re.search(r'<meta\s+name="description"', html, re.IGNORECASE):
            html = re.sub(r'<meta\s+name="description"[^>]*>', new_desc, html, flags=re.IGNORECASE)
        else:
            html = html.replace('</title>', f'</title>\n  {new_desc}', 1)
    
    # Add OG tags + canonical if missing
    if 'og_title' in seo and 'og:title' not in html:
        og = make_og_tags(seo['og_title'], seo['og_desc'], seo['canonical'])
        html = html.replace('</head>', f'{og}\n</head>', 1)
    elif 'canonical' in seo and 'canonical' not in html:
        html = html.replace('</head>', f'  <link rel="canonical" href="{seo["canonical"]}">\n</head>', 1)
    
    if html != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        updated.append(fname)
        print('SEO fixed: ' + fname)

print('Updated:', len(updated), 'files')

# ── Create robots.txt ────────────────────────────────────────────────────────
robots_content = f"""User-agent: *
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""
with open('public/robots.txt', 'w', encoding='utf-8') as f:
    f.write(robots_content)
print('Created: robots.txt')

# ── Create sitemap.xml ───────────────────────────────────────────────────────
pages = [
    ("atrium.html",                    "1.0",  "weekly"),
    ("nos-biens-achat.html",           "0.9",  "weekly"),
    ("nos-biens-location.html",        "0.9",  "weekly"),
    ("nos-metiers.html",               "0.8",  "monthly"),
    ("nos-metiers-syndic.html",        "0.8",  "monthly"),
    ("nos-metiers-location.html",      "0.8",  "monthly"),
    ("nos-metiers-gestion-locative.html", "0.8", "monthly"),
    ("nos-metiers-assurances.html",    "0.8",  "monthly"),
    ("nos-metiers-vente.html",         "0.8",  "monthly"),
    ("notre-maison.html",              "0.7",  "monthly"),
    ("contact.html",                   "0.7",  "monthly"),
    ("nous-rejoindre.html",            "0.6",  "monthly"),
    ("espace-client.html",             "0.5",  "monthly"),
]

urls = ""
for page, priority, freq in pages:
    url = f"{DOMAIN}/{page}"
    urls += f"""  <url>
    <loc>{url}</loc>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>
"""

sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}</urlset>"""

with open('public/sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)
print('Created: sitemap.xml')
print('Done!')
