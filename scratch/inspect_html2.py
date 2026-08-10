from bs4 import BeautifulSoup

with open('public/nos-biens-achat.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find a property card column - it wraps type_bien, lieu, surface_nbp
cards = soup.find_all('p', class_='type_bien')
print(f"Found {len(cards)} property cards")

# Print structure of first card
if cards:
    card = cards[0]
    parent_col = card.find_parent('div', class_='fusion-layout-column')
    if parent_col:
        print("\nColumn classes:", parent_col.get('class'))
        print("Column ID-like attrs:", {k:v for k,v in parent_col.attrs.items() if k != 'style'})

# Find the Valider button and the form
forms = soup.find_all('form', id=lambda x: x and 'accueil' in x)
print(f"\nForms found: {len(forms)}")
for form in forms:
    print("Form ID:", form.get('id'))
    # Print all selects
    selects = form.find_all('select')
    for s in selects:
        print("  Select ID:", s.get('id'), "name:", s.get('name'))
        opts = [o.get_text() for o in s.find_all('option')]
        print("  Options:", opts[:5], "...")
    
    # Check submit button
    btn = form.find('button', attrs={'type': 'submit'}) or form.find('input', attrs={'type': 'submit'}) or form.find(class_=lambda x: x and 'submit' in str(x).lower())
    print("  Submit element:", btn.get('class') if btn else "not found directly")
    
    # Print all buttons
    all_btns = form.find_all('button')
    print("  All buttons:", [b.get_text() for b in all_btns])
    
    # Print all inputs
    all_inputs = form.find_all('input', type='submit')
    print("  Submit inputs:", [i.get('value') for i in all_inputs])
