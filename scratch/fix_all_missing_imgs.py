import os
import urllib.request
import shutil

# Map of missing files -> replacement Unsplash URLs or local file copies
REPLACEMENTS = {
    # Recrutement photo - team/office
    "public/assets/wp-content/uploads/2020/05/GCP Syndic-Gestion-recrutement-400.jpg":
        "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=400&q=80&auto=format&fit=crop",
    
    # Ballon / balloon icon - use a building icon style PNG
    "public/assets/wp-content/uploads/2021/02/Ballon-.png":
        "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=200&q=80&auto=format&fit=crop",

    # Cle.svg - key icon (use generic real estate key image)
    # This is SVG - will create manually below

    # gestion-1.jpg - property management photo
    "public/assets/wp-content/uploads/2021/02/gestion-1.jpg":
        "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=600&q=80&auto=format&fit=crop",

    # mains.svg - hands icon (will create SVG manually)

    # vente-achat-location.jpg - real estate
    "public/assets/wp-content/uploads/2021/02/vente-achat-location.jpg":
        "https://images.unsplash.com/photo-1582407947304-fd86f028f716?w=600&q=80&auto=format&fit=crop",

    # valeurs.png - values/team
    "public/assets/wp-content/uploads/2021/05/valeurs.png":
        "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=600&q=80&auto=format&fit=crop",

    # Assurance photos
    "public/assets/wp-content/uploads/2021/07/Assurance_multirisque_habitation.jpg":
        "https://images.unsplash.com/photo-1560520653-9e0e4c89eb11?w=500&q=80&auto=format&fit=crop",
    "public/assets/wp-content/uploads/2021/07/Assurance_proprietaire_non_occupant.jpg":
        "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?w=500&q=80&auto=format&fit=crop",
    "public/assets/wp-content/uploads/2021/07/GCP SyndicGestion_Location.jpg":
        "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=500&q=80&auto=format&fit=crop",
    "public/assets/wp-content/uploads/2021/07/Garantie_defaut_entretien.jpg":
        "https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=500&q=80&auto=format&fit=crop",
    "public/assets/wp-content/uploads/2021/07/Garantie_loyers_impayes.jpg":
        "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=500&q=80&auto=format&fit=crop",
    "public/assets/wp-content/uploads/2021/07/Garantie_vacance_locative.jpg":
        "https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=500&q=80&auto=format&fit=crop",
    "public/assets/wp-content/uploads/2021/07/Protection_juridique_premium.jpg":
        "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=500&q=80&auto=format&fit=crop",

    # VisuelMaisonmobile.png - mobile house visual
    "public/assets/wp-content/uploads/2022/03/VisuelMaisonmobile.png":
        "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=500&q=80&auto=format&fit=crop",

    # AnthonyCarle_2.webp - person photo (replaced with Moroccan professional)
    "public/assets/wp-content/uploads/2025/02/AnthonyCarle_2.webp":
        "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&q=80&auto=format&fit=crop",
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

for local_path, url in REPLACEMENTS.items():
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            with open(local_path, 'wb') as f:
                f.write(response.read())
        print(f"OK: {local_path}")
    except Exception as e:
        print(f"FAIL: {local_path} - {e}")

print("\nDone downloading replacement images!")
