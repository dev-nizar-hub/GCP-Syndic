import os
import random
from bs4 import BeautifulSoup
import unicodedata

public_dir = 'public'

# The 4 cities where GCP Syndic operates (from the map)
gcp_cities = ["Meknès", "Kénitra", "Tanger", "Oujda"]

property_types = [
    "Appartement", "Villa", "Maison", "Studio", "Duplex",
    "Riad", "Garage", "Terrain", "Bureau", "Local commercial"
]

room_numbers = [
    "1 pièce", "2 pièces", "3 pièces", "4 pièces", "5 pièces", "5+ pièces"
]

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def create_options(soup, values):
    options = [soup.new_tag('option', value="")]
    options[0].string = " "
    options[0]['selected'] = "selected"
    for val in values:
        opt = soup.new_tag('option', value=val)
        opt.string = val
        options.append(opt)
    return options

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    changed = False

    # 1. Update the actual properties to only be in these 4 cities
    columns = soup.find_all('div', class_='fusion-layout-column')
    for col in columns:
        lieu_p = col.find('p', class_='lieu')
        if lieu_p:
            new_city = random.choice(gcp_cities)
            lieu_p.string = new_city
            
            # update href
            anchor = col.find('a', class_='fusion-column-anchor')
            if anchor and 'href' in anchor.attrs:
                href = anchor['href']
                # Try to replace the old city name (case insensitive, ignoring accents if possible, or just exact match in URL format)
                # Since we don't know the exact old city, we can just look for any of the expanded moroccan cities in the URL and replace it
                all_moroccan_cities = [
                    "agadir", "al-hoceima", "beni-mellal", "berkane", "berrechid", 
                    "casablanca", "chefchaouen", "dakhla", "el-jadida", "errachidia", 
                    "essaouira", "fes", "guelmim", "ifrane", "kenitra", "khemisset", 
                    "khenifra", "khouribga", "laayoune", "larache", "marrakech", 
                    "meknes", "mohammedia", "nador", "ouarzazate", "oujda", "rabat", 
                    "safi", "sale", "sefrou", "settat", "sidi-kacem", "tanger", 
                    "taroudant", "taza", "temara", "tetouan", "tiznit", "zagora"
                ]
                new_city_url = strip_accents(new_city).lower().replace(' ', '-').replace("'", '-')
                for mc in all_moroccan_cities:
                    if mc in href:
                        anchor['href'] = href.replace(mc, new_city_url)
                        break
            changed = True

    # 2. Update the dropdown filters to only include these 4 cities
    fields = soup.find_all('div', class_='frm_form_field')
    for field in fields:
        label = field.find('label', class_='frm_primary_label')
        select = field.find('select')
        
        if label and select:
            text = label.get_text(strip=True).lower()
            
            if 'ville' in text or 'localisation' in text:
                select.clear()
                for opt in create_options(soup, sorted(gcp_cities)):
                    select.append(opt)
                changed = True
                
            elif 'type' in text:
                select.clear()
                for opt in create_options(soup, property_types):
                    select.append(opt)
                changed = True
                
            elif 'nombre' in text or 'pièce' in text:
                select.clear()
                for opt in create_options(soup, room_numbers):
                    select.append(opt)
                changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Updated {os.path.basename(filepath)}")
    else:
        print(f"No changes for {os.path.basename(filepath)}")


# Process all HTML files
for filename in os.listdir(public_dir):
    if filename.endswith('.html'):
        process_file(os.path.join(public_dir, filename))
