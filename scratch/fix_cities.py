import re

moroccan_cities = [
    ('Meknès', 'Meknès'),
    ('Casablanca', 'Casablanca'),
    ('Rabat', 'Rabat'),
    ('Marrakech', 'Marrakech'),
    ('Agadir', 'Agadir'),
    ('Tanger', 'Tanger'),
    ('Fès', 'Fès'),
    ('Oujda', 'Oujda'),
    ('Kénitra', 'Kénitra'),
    ('Salé', 'Salé'),
    ('Témara', 'Témara'),
    ('Mohammedia', 'Mohammedia'),
    ('Settat', 'Settat'),
    ('El Jadida', 'El Jadida'),
    ('Béni Mellal', 'Béni Mellal'),
    ('Tétouan', 'Tétouan'),
]

# Build option HTML - Meknès first
new_options = ''.join(
    f'<option  value="{val}">{label}</option>'
    for val, label in moroccan_cities
)

# Pattern matches the full options block between empty-option and closing </select>
pattern = r'(<option\s+value=""\s+selected=.selected.\s*>\s*</option>).*?(?=\t</select>)'
replacement = r'\g<1>' + new_options

files = [
    'public/nos-biens-achat.html',
    'public/nos-biens-location.html',
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Count replacements
    matches = len(re.findall(pattern, content, flags=re.DOTALL))
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f'{filepath}: replaced {matches} dropdown(s) with Moroccan cities only (Meknès first)')
