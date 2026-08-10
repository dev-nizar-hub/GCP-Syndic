import os
import re

search_dir = "c:/xampp/htdocs/GCP Syndic Website v2/public"

replacements = [
    ("GCP Syndic Paris 8", "GCP Syndic Meknès"),
    ("GCP Syndic Paris 15", "GCP Syndic Fès"),
    ("GCP Syndic Paris 16", "GCP Syndic Rabat"),
    ("GCP Syndic Paris 17", "GCP Syndic Casablanca"),
    ("GCP Syndic Levallois", "GCP Syndic Tanger"),
    ("<h3>Paris 8</h3>", "<h3>Meknès</h3>"),
    ("<h3>Paris 9</h3>", "<h3>Fès</h3>"),
    ("<h3>Paris 11</h3>", "<h3>Kénitra</h3>"),
    ("<h3>Paris 15</h3>", "<h3>Salé</h3>"),
    ("<h3>Paris 16</h3>", "<h3>Rabat</h3>"),
    ("<h3>Paris 17</h3>", "<h3>Casablanca</h3>"),
    ("gcpsyndic-paris-viii", "gcpsyndic-meknes"),
    ("gcpsyndic-paris-xv", "gcpsyndic-sale"),
    ("gcpsyndic-paris-16", "gcpsyndic-rabat"),
    ("gcpsyndic-paris-xvii", "gcpsyndic-casablanca"),
    (">Paris<", ">Meknès<"),
    ('"Paris"', '"Meknès"'),
    ("Bagnolet", "Marrakech"),
    ("Boulogne-Billancourt", "Agadir"),
    ("Asnières-sur-Seine", "Tanger"),
    ("Cormeilles-en-Parisis", "Oujda"),
    ("Top 5 des agences immobilières à Paris", "Top 5 des agences immobilières au Maroc"),
    ("Studio Harcourt Paris", "Studio Harcourt Maroc"),
    ("AgenceImmoParis", "AgenceImmoMaroc"),
    ("sur Paris et l'Île-de-France", "sur Meknès et le Maroc"),
    ("sur Paris et l'île de france", "sur Meknès et le Maroc"),
    ("sur Paris et la région parisienne", "sur Meknès et le Maroc"),
    ("Paris et la région parisienne", "Meknès et le Maroc"),
    ("la région parisienne", "le Maroc"),
    ("Paris", "Meknès"), # Catch all remaining Paris
    ("France", "Maroc"),
    ("français", "marocain"),
    ("francais", "marocain"),
    ("île de france", "Meknès"),
    ("ile de france", "Meknès"),
    ("ile-de-france", "Meknès"),
]

for root, dirs, files in os.walk(search_dir):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                new_content = content
                for old, new in replacements:
                    # Ignore case for France / Paris catch-alls if needed, but doing exact match is safer first
                    new_content = new_content.replace(old, new)
                
                if content != new_content:
                    with open(path, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    print(f"Updated: {f}")
            except Exception as e:
                print(f"Error processing {path}: {e}")

print("Replacement complete.")
