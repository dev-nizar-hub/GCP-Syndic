import re
with open('public/nos-biens-achat.html', 'r', encoding='utf-8') as f:
    content = f.read()
m = re.search(r'id="field_y68yj".*?</select>', content, re.DOTALL)
if m:
    options = re.findall(r'value="([^"]+)"', m.group(0))
    print('Cities in nos-biens-achat dropdown:')
    for o in options:
        print(' -', o)
