from bs4 import BeautifulSoup

with open('public/nos-biens-achat.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# The grid div has no class - check what its parent is and what it contains
grid = soup.find(id='gcp-properties-grid')
if grid:
    print("Grid parent tag:", grid.parent.name if grid.parent else "none")
    print("Grid parent classes:", grid.parent.get('class') if grid.parent else "none")
    
    # Count direct children columns
    children = [c for c in grid.children if hasattr(c, 'get')]
    print("Direct div children in grid:", len(children))
    
    # Check the GCP custom injected style block
    all_styles = soup.find_all('style')
    for s in all_styles:
        txt = s.string or ''
        if 'gcp-property-card' in txt or 'Valider' in txt:
            print("\nGCP injected style found:")
            print(txt[:600].encode('ascii','replace').decode('ascii'))
