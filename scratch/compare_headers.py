import re

def extract_gcp_header(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    m = re.search(r'<header class="gcp-header".*?</header>', content, re.DOTALL)
    if m:
        return m.group(0)
    return 'NOT FOUND'

ref  = extract_gcp_header('public/atrium.html')
cont = extract_gcp_header('public/contact.html')

# Extract nav hrefs and text
def get_links(html):
    return re.findall(r'href="([^"]+)"[^>]*>([^<]{1,60})', html)

print('=== REFERENCE (atrium.html) nav hrefs ===')
for href, text in get_links(ref):
    print(f'  {href:50s} | {text.strip()[:50]}')

print()
print('=== CONTACT (contact.html) nav hrefs ===')
for href, text in get_links(cont):
    print(f'  {href:50s} | {text.strip()[:50]}')

print()
# Logo check
for label, html in [('atrium', ref), ('contact', cont)]:
    m = re.search(r'gcp-logo.*?src="([^"]+)"', html, re.DOTALL)
    print(f'Logo {label}: {m.group(1) if m else "NOT FOUND"}')

print()
print(f'Header length atrium : {len(ref)} chars')
print(f'Header length contact: {len(cont)} chars')
print()
if ref == cont:
    print('IDENTICAL headers')
else:
    print('DIFFERENT headers - finding first difference...')
    for i, (a, b) in enumerate(zip(ref, cont)):
        if a != b:
            print(f'First diff at char {i}:')
            print(f'  atrium : {repr(ref[max(0,i-60):i+60])}')
            print(f'  contact: {repr(cont[max(0,i-60):i+60])}')
            break
