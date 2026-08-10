import os
import glob

html_files = glob.glob('public/*.html')

replacements = {
    '10 implantations en Ile-de-France': 'Le syndic de r&eacute;f&eacute;rence',
    'Pour une v&eacute;ritable expertise locale': 'Une expertise locale au Maroc',
    'Pour une véritable expertise locale': 'Une expertise locale au Maroc',
    
    'Une culture familiale': 'Un service professionnel',
    'Et une volont&eacute; d&apos;ind&eacute;pendance': 'Transparence et rigueur',
    "Et une volonté d'indépendance": 'Transparence et rigueur',
    
    'Pour entretenir votre patrimoine': 'Pour valoriser votre patrimoine',
    
    'La satisfaction de nos clients au coeur de nos valeurs': 'Votre satisfaction au coeur de nos priorit&eacute;s',
    'La satisfaction de nos clients au coeur de nos valeurs': 'Votre satisfaction au coeur de nos priorités'
}

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    original = html
    for old, new in replacements.items():
        html = html.replace(old, new)
        
    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated {filepath}")
