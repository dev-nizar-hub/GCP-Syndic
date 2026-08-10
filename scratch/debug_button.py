from bs4 import BeautifulSoup

with open('public/nos-biens-achat.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the Valider button
btns = soup.find_all('button', class_='frm_button_submit')
print(f"Found {len(btns)} Valider buttons")
for btn in btns:
    print("\nButton HTML:", btn)
    form = btn.find_parent('form')
    if form:
        print("Parent form ID:", form.get('id'))
        print("Parent form action:", form.get('action'))
    else:
        print("No parent form found!")
    
    # Check if it's inside our expected selects
    container = btn.find_parent('div', class_='frm_fields_container')
    print("In frm_fields_container:", container is not None)
    
    # Print siblings/nearby selects
    form_parent = btn.find_parent('form')
    if form_parent:
        selects = form_parent.find_all('select')
        print("Selects in form:", [s.get('id') for s in selects])
