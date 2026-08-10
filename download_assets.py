import os
import re
import urllib.request
from urllib.parse import urlparse

# File containing all unique URLs found in atrium.html
links_file = 'scratch_links.txt'
base_dir = 'public/assets'

if not os.path.exists(base_dir):
    os.makedirs(base_dir)

# Read the links
with open(links_file, 'r', encoding='utf-8') as f:
    urls = f.read().splitlines()

# We only want to download actual assets, not HTML pages
asset_extensions = ('.css', '.js', '.jpg', '.jpeg', '.png', '.svg', '.gif', '.webp', '.woff', '.woff2', '.ttf')

success_count = 0
fail_count = 0

for url in urls:
    # Some URLs have query parameters like ?ver=1.2.3, we need to strip them for checking extensions
    parsed = urlparse(url)
    path = parsed.path
    
    # Check if it's an asset we should download
    if not path.lower().endswith(asset_extensions):
        continue
        
    # Create the local path
    # Remove leading slash for os.path.join
    local_path = os.path.join(base_dir, path.lstrip('/'))
    local_dir = os.path.dirname(local_path)
    
    if not os.path.exists(local_dir):
        os.makedirs(local_dir, exist_ok=True)
        
    if not os.path.exists(local_path):
        try:
            # Need to provide a user agent, some WP sites block default urllib
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
                data = response.read()
                out_file.write(data)
            print(f"Downloaded: {path}")
            success_count += 1
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            fail_count += 1
    else:
        print(f"Already exists: {path}")

print(f"\nDownload complete. Success: {success_count}, Failed: {fail_count}")
