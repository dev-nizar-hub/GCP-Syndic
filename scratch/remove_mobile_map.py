"""
Remove the mobile agency map section (#z_carte_mobile) from atrium.html.
This is the section that shows a city map + "Voir toutes nos agences" button on mobile.
"""

with open('public/atrium.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The section starts with id="z_carte_mobile" on a fusion-fullwidth div
# and ends before the next fullwidth div (id="z_blog")
start_marker = '<div class="fusion-fullwidth fullwidth-box fusion-builder-row-11'
end_marker = '<div class="fusion-fullwidth fullwidth-box fusion-builder-row-12'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print('Markers not found, trying alternate approach')
    # Try searching for z_carte_mobile directly
    start_idx = html.find('id="z_carte_mobile"')
    if start_idx != -1:
        # find the opening div tag start
        start_idx = html.rfind('<div', 0, start_idx)
    end_idx = html.find('id="z_blog"')
    if end_idx != -1:
        end_idx = html.rfind('<div', 0, end_idx)

if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
    removed = html[start_idx:end_idx]
    new_html = html[:start_idx] + html[end_idx:]
    with open('public/atrium.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print('Removed ' + str(len(removed)) + ' characters of mobile map section')
    print('Done!')
else:
    print('Could not find section boundaries, idx:', start_idx, end_idx)
