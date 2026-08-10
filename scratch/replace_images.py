import re

files = ['public/nos-biens-achat.html', 'public/nos-biens-location.html']

# Nice Unsplash images for different property types
images = {
    'Appartement': 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=600&q=80',
    'Studio': 'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=600&q=80',
    'Parking': 'https://images.unsplash.com/photo-1506521781263-d8422e82f27a?w=600&q=80',
    'Garage': 'https://images.unsplash.com/photo-1605814524823-380d32bb57a7?w=600&q=80',
    'default': 'https://images.unsplash.com/photo-1580587771525-78b9dba3b914?w=600&q=80' # Nice house
}

def replace_card_images(html):
    # The structure is:
    # <div class="... gcp-pc" ... data-type="Appartement" ...>
    #   ...
    #   <a class="fusion-column-anchor" href="/demande-bien.html?...&img=https%3A//reseausdpf.staticlbi.com/...">
    #   ...
    #   <img ... src="https://reseausdpf.staticlbi.com/..." />
    
    # We will use regex to find each gcp-pc card and replace the reseausdpf links inside it
    
    # Find all cards
    card_pattern = re.compile(r'(<div[^>]*gcp-pc[^>]*data-type="([^"]+)"[^>]*>.*?)(?=<!-- card end or next card -->|<div[^>]*gcp-pc)', re.IGNORECASE | re.DOTALL)
    
    # Wait, splitting by `<div[^>]*gcp-pc` is tricky in regex.
    # Instead, we can just replace all reseausdpf images globally, but to map them to the type, 
    # let's iterate through the HTML and keep track of the last seen data-type.
    
    out_html = ""
    current_type = 'default'
    
    # We can split by `<div ` and process chunks
    chunks = html.split('<div ')
    
    for i in range(len(chunks)):
        chunk = chunks[i]
        
        # Check if this div sets a new data-type
        type_match = re.search(r'data-type="([^"]+)"', chunk)
        if type_match and 'gcp-pc' in chunk:
            current_type = type_match.group(1)
            
        # Replace image src
        chunk = re.sub(r'src="https://reseausdpf\.staticlbi\.com/[^"]+"', f'src="{images.get(current_type, images["default"])}"', chunk)
        
        # Replace the img= URL parameter in the link
        # The link looks like: href="/demande-bien.html?city=...&img=https%3A//reseausdpf.staticlbi.com/..."
        # We need to URL encode the unsplash URL
        from urllib.parse import quote
        encoded_url = quote(images.get(current_type, images["default"]), safe='')
        chunk = re.sub(r'(&img=)https(?:%3A|:)//reseausdpf\.staticlbi\.com/[^"]*', r'\1' + encoded_url, chunk)
        
        chunks[i] = chunk
        
    return '<div '.join(chunks)

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    new_html = replace_card_images(html)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_html)
        
    print('Replaced images in', fpath)
