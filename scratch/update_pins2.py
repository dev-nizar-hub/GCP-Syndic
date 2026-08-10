import re

html_file = 'public/atrium.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the previous incorrect coordinates with the new estimates
replacements = {
    'style="left:56.5%;top:5%;" title="Tanger"': 'style="left:57%;top:23%;" title="Tanger"',
    'style="left:51.5%;top:17%;" title="Kénitra"': 'style="left:54%;top:28%;" title="Kénitra"',
    'style="left:58.0%;top:20%;" title="Meknès"': 'style="left:59%;top:32%;" title="Meknès"',
    'style="left:81.5%;top:13.5%;" title="Oujda"': 'style="left:68%;top:27%;" title="Oujda"'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated pin coordinates.")
