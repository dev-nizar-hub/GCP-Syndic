with open('public/demande-bien.html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'gcp-whatsapp-forms.js' not in html:
    html = html.replace('</body>', '<script defer src="/assets/gcp-whatsapp-forms.js"></script>\n</body>')
    with open('public/demande-bien.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Added whatsapp JS to demande-bien.html')
else:
    print('Already present')
