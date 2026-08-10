from bs4 import BeautifulSoup

with open('public/nos-biens-achat.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Print first 5 property cards in detail
cards = soup.find_all('p', class_='type_bien')
for i, card in enumerate(cards[:6]):
    lieu = card.find_next_sibling('p', class_='lieu')
    surf_p = card.find_next_sibling('p', class_='surface_nbp')
    nbp = surf_p.find('span', class_='nbp') if surf_p else None
    surface = surf_p.find('span', class_='surface') if surf_p else None
    
    print(f"Card {i+1}:")
    print(f"  type: {card.get_text(strip=True)}")
    print(f"  lieu: {lieu.get_text(strip=True) if lieu else 'N/A'}")
    print(f"  surface: {surface.get_text(strip=True) if surface else 'N/A'}")
    print(f"  nbp: {nbp.get_text(strip=True) if nbp else 'N/A'}")
    
    # Get the parent column
    parent = card.find_parent('div', class_='fusion-layout-column')
    if parent:
        print(f"  col classes: {parent.get('class')}")
    print()
