import os
from bs4 import BeautifulSoup

public_dir = 'public'

# Expanded list of Moroccan cities
moroccan_cities = [
    "Agadir", "Al Hoceïma", "Béni Mellal", "Berkane", "Berrechid", 
    "Casablanca", "Chefchaouen", "Dakhla", "El Jadida", "Errachidia", 
    "Essaouira", "Fès", "Guelmim", "Ifrane", "Kénitra", "Khemisset", 
    "Khenifra", "Khouribga", "Laâyoune", "Larache", "Marrakech", 
    "Meknès", "Mohammedia", "Nador", "Ouarzazate", "Oujda", "Rabat", 
    "Safi", "Salé", "Sefrou", "Settat", "Sidi Kacem", "Tanger", 
    "Taroudant", "Taza", "Témara", "Tétouan", "Tiznit", "Zagora"
]

property_types = [
    "Appartement", "Villa", "Maison", "Studio", "Duplex",
    "Riad", "Garage", "Terrain", "Bureau", "Local commercial"
]

room_numbers = [
    "1 pièce", "2 pièces", "3 pièces", "4 pièces", "5 pièces", "5+ pièces"
]

def create_options(soup, values):
    options = [soup.new_tag('option', value="")]
    options[0].string = " "
    options[0]['selected'] = "selected"
    for val in values:
        opt = soup.new_tag('option', value=val)
        opt.string = val
        options.append(opt)
    return options

def fix_forms_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    changed = False

    # Find all select elements inside frm_form_field
    fields = soup.find_all('div', class_='frm_form_field')
    for field in fields:
        label = field.find('label', class_='frm_primary_label')
        select = field.find('select')
        
        if label and select:
            text = label.get_text(strip=True).lower()
            
            if 'ville' in text or 'localisation' in text:
                select.clear()
                for opt in create_options(soup, sorted(moroccan_cities)):
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
        print(f"Fixed dropdowns in {os.path.basename(filepath)}")
    else:
        print(f"No dropdowns found in {os.path.basename(filepath)}")

for filename in os.listdir(public_dir):
    if filename.endswith('.html'):
        fix_forms_in_file(os.path.join(public_dir, filename))
