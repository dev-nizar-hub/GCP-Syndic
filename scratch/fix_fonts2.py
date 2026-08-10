import os
import re
import urllib.request

css_file = r'public\assets\wp-content\uploads\fusion-styles\d4b3e86c72293cd64c0323ffe10deda8.min.css'

with open(css_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all font URLs pointing to atrium-gestion.fr
urls = re.findall(r'url\([\'"]?(//atrium-gestion\.fr[^)\'"]+\.(?:woff2?|eot|ttf|svg)[^)\'"]*)[\'"]?\)', content)

# Remove duplicates and clean up
clean_urls = []
for u in set(urls):
    u = u.strip("'\"")
    clean_urls.append('https:' + u.split('?')[0].split('#')[0]) # Add https: and remove query params

clean_urls = list(set(clean_urls))

print(f"Found {len(clean_urls)} font URLs to download.")

for url in clean_urls:
    # Determine local path
    local_path = url.replace('https://atrium-gestion.fr', 'public/assets')
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    if not os.path.exists(local_path):
        print(f"Downloading {url}...")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                with open(local_path, 'wb') as out_file:
                    out_file.write(response.read())
            print(f"  -> Saved to {local_path}")
        except Exception as e:
            print(f"  -> Failed to download: {e}")
    else:
        print(f"Already exists: {local_path}")

print("Done downloading remaining fonts!")
