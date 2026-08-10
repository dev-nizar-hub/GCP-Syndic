import re

html_file = 'public/atrium.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the old guesses with the newly calculated precise coordinates
replacements = {
    'style="left:51%;top:5%;" title="Tanger"': 'style="left:56.5%;top:5%;" title="Tanger"',
    'style="left:48%;top:20%;" title="Kénitra"': 'style="left:51.5%;top:17%;" title="Kénitra"',
    'style="left:52%;top:25%;" title="Meknès"': 'style="left:58.0%;top:20%;" title="Meknès"',
    'style="left:88%;top:18%;" title="Oujda"': 'style="left:81.5%;top:13.5%;" title="Oujda"'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated pin coordinates.")
