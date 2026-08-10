import os
import urllib.request

fonts = [
    'awb-icons.woff',
    'awb-icons.ttf',
    'awb-icons.svg'
]

base_url = 'https://atrium-gestion.fr/wp-content/themes/Avada/includes/lib/assets/fonts/icomoon/'
local_dir = 'public/assets/wp-content/themes/Avada/includes/lib/assets/fonts/icomoon'

os.makedirs(local_dir, exist_ok=True)

for font in fonts:
    url = base_url + font
    local_path = os.path.join(local_dir, font)
    print(f"Downloading {url}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(local_path, 'wb') as out_file:
                out_file.write(response.read())
        print(f"  -> Saved to {local_path}")
    except Exception as e:
        print(f"  -> Failed to download: {e}")
