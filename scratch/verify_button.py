from bs4 import BeautifulSoup
with open('public/nos-biens-achat.html', 'r', encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')
btns = soup.find_all('button', class_='frm_button_submit')
for b in btns:
    s = str(b)[:300].encode('ascii', errors='replace').decode('ascii')
    print(s)
    print()
