import os
import glob

public_dir = "public"
html_files = glob.glob(os.path.join(public_dir, '*.html'))

SCRIPT_TAG = '<script src="/assets/gcp-chatbot.js" defer></script>'

injected = []
already  = []

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'gcp-chatbot.js' in content:
        already.append(os.path.basename(filepath))
        continue

    # Insert just before </body>
    if '</body>' in content:
        content = content.replace('</body>', f'\n{SCRIPT_TAG}\n</body>', 1)
    else:
        content += f'\n{SCRIPT_TAG}\n'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    injected.append(os.path.basename(filepath))

print(f"Injected into {len(injected)} files:")
for f in injected: print(' +', f)

if already:
    print(f"\nAlready had chatbot ({len(already)} files):")
    for f in already: print(' =', f)

print("\nDone!")
