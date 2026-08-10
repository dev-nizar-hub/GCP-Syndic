from bs4 import BeautifulSoup
with open('public/nos-biens-achat.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

btn = soup.find('button', class_='frm_button_submit')
parents = []
p = btn
while p and p.name != '[document]':
    parents.append(p.name + (f" (class: {p.get('class')})" if p.get('class') else ""))
    p = p.parent

for p in parents:
    print(p)
