import glob

def remove_immodvisor():
    files = glob.glob('public/nos-metiers-*.html')
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        start_str = 'id="z_avis"'
        pos = html.find(start_str)
        if pos != -1:
            div_start = html.rfind('<div', 0, pos)
            
            end_script_pos = html.find('fetch(\'https://api-reviews.immodvisor.com', pos)
            if end_script_pos != -1:
                end_script_close = html.find('</script>', end_script_pos)
                
                search_start = end_script_close + 9
                for _ in range(4): # Usually 4 closing divs: column > wrapper > text block > ??
                    search_start = html.find('</div>', search_start) + 6
                
                remove_start = div_start
                remove_end = search_start
                
                new_html = html[:remove_start] + html[remove_end:]
                
                # Also, we should adjust the width of the remaining column since we removed the 19% z_avis column.
                # The remaining column has class fusion-builder-column-9. We can change its width from 66.666666666667% to 100% or similar if needed.
                # Actually, leaving it as is might just leave a blank space where the widget was, which is fine, or we can just remove it and see.
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_html)
                print(f'Removed from {filepath}')

if __name__ == "__main__":
    remove_immodvisor()
