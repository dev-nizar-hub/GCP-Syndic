import os
import random
import re
from bs4 import BeautifulSoup
import unicodedata

moroccan_cities = [
    "Casablanca", "Rabat", "Marrakech", "Tanger", "Fès",
    "Meknès", "Agadir", "Oujda", "Kénitra", "Tétouan",
    "Safi", "El Jadida", "Mohammedia", "Salé", "Témara"
]

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def moroccanize_properties(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    changed = False

    # Each property is a fusion-layout-column
    columns = soup.find_all('div', class_='fusion-layout-column')
    for col in columns:
        lieu_p = col.find('p', class_='lieu')
        if lieu_p:
            old_city = lieu_p.get_text().strip()
            
            # Skip if it's already a Moroccan city from our list (allow exact match or without accents)
            if any(strip_accents(m_city.lower()) == strip_accents(old_city.lower()) for m_city in moroccan_cities):
                continue
                
            new_city = random.choice(moroccan_cities)
            
            # Update the text
            lieu_p.string = new_city
            
            # Try to update the href link as well
            anchor = col.find('a', class_='fusion-column-anchor')
            if anchor and 'href' in anchor.attrs:
                href = anchor['href']
                # Try to replace the old city name (case insensitive, ignoring accents if possible, or just exact match in URL format)
                old_city_url = strip_accents(old_city).lower().replace(' ', '-').replace("'", '-')
                new_city_url = strip_accents(new_city).lower().replace(' ', '-').replace("'", '-')
                
                # If old city is in the URL, replace it
                if old_city_url in href:
                    anchor['href'] = href.replace(old_city_url, new_city_url)
                else:
                    # sometimes the old city might be slightly different in URL, e.g. "Cormeilles-en-Parisis" -> "cormeilles-en-parisis"
                    # We can use regex to replace the last word before the trailing slash if it looks like a city
                    # e.g., /annonce/vente-appartement-...-sartrouville/
                    pass
            
            changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Updated properties in {os.path.basename(filepath)}")
    else:
        print(f"No changes needed in {os.path.basename(filepath)}")

# Run on both property pages
moroccanize_properties('public/nos-biens-achat.html')
moroccanize_properties('public/nos-biens-location.html')
