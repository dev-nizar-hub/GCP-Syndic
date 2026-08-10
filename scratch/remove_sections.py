import re

def remove_sections():
    with open('public/notre-maison.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the start of row-10 (Notre histoire)
    row10_start = html.find('fusion-builder-row-10 fusion-flex-container')
    if row10_start == -1:
        print('Error: fusion-builder-row-10 not found')
        return

    # Find the opening <div class="fusion-fullwidth... before row10_start
    remove_start = html.rfind('<div class="fusion-fullwidth', 0, row10_start)
    if remove_start == -1:
        print('Error: Could not find opening div for row 10')
        return

    # Find the start of row-13 (last row of Notre direction)
    row13_start = html.find('fusion-builder-row-13 fusion-flex-container')
    if row13_start == -1:
        print('Error: fusion-builder-row-13 not found')
        return
        
    # Find the end of the row-13 block. 
    # Let's find the next fusion-fullwidth div after row-13 if it exists.
    next_fullwidth = html.find('<div class="fusion-fullwidth', row13_start + 50)
    
    if next_fullwidth != -1 and next_fullwidth < html.find('</main>'):
        remove_end = next_fullwidth
    else:
        # If there are no more fullwidth divs, remove until just before </main>
        remove_end = html.rfind('</div>', 0, html.find('</main>'))
        
    if remove_end == -1:
         print('Error: Could not determine end of removal area')
         return

    print(f'Removing from {remove_start} to {remove_end}')
    
    new_html = html[:remove_start] + html[remove_end:]
    
    with open('public/notre-maison.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
        
    print('Successfully removed sections.')

if __name__ == '__main__':
    remove_sections()
