import glob

# 1. Update WhatsApp phone number in JS
js_file = 'public/assets/gcp-whatsapp-forms.js'
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

new_js = js_content.replace("const PHONE_NUMBER = '212662081784';", "const PHONE_NUMBER = '212708066188';")
if js_content != new_js:
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(new_js)
    print("Updated WhatsApp JS")

# 2. Update HTML files for emails and phone numbers
files = glob.glob('public/*.html')
count = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        html = fh.read()
    
    original = html
    
    # Replace email variations
    html = html.replace('contact@gcp-syndic.ma', 'contact@gcp.ma')
    html = html.replace('contact@gcpsyndic.ma', 'contact@gcp.ma')
    
    # Replace phone number linking: append the new number next to the old one
    # Note: Using a single string replace for the entire anchor tag
    old_phone_link = '<a href="tel:+212662081784">+212 6 62 08 17 84</a>'
    new_phone_links = '<a href="tel:+212662081784">+212 6 62 08 17 84</a><br><a href="tel:+212708066188">07 08 06 61 88</a>'
    html = html.replace(old_phone_link, new_phone_links)
    
    # Just in case there are single spaces or variations in the HTML
    # We will also try replacing specific text nodes if they exist without tags, though grep shows they are in anchor tags.

    if html != original:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(html)
        count += 1
        print('Updated: ' + f)

print('Total HTML files updated: ' + str(count))
