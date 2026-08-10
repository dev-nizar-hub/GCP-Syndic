with open('public/nos-biens-achat.html', 'r', encoding='utf-8') as f:
    content = f.read()
print('File length:', len(content))
print('type_bien occurrences:', content.count('type_bien'))
print('lieu occurrences:', content.count('class="lieu"'))
print('Valider occurrences:', content.count('Valider'))
print('field_y68yj occurrences:', content.count('field_y68yj'))
print('surface_nbp occurrences:', content.count('surface_nbp'))
print('fusion-layout-column occurrences:', content.count('fusion-layout-column'))
# Find a snippet around "lieu"
idx = content.find('class="lieu"')
if idx != -1:
    print('\nSample around lieu:', content[idx-100:idx+200])
