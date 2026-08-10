import os

files = ['public/nos-biens-achat.html', 'public/nos-biens-location.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    idx = c.find('id="tr1"')
    if idx == -1:
        print(f"NOT FOUND in {f}")
        continue
        
    start = c.rfind('<div class="fusion-layout-column', 0, idx)
    end = c.find('</form>', idx) + 7
    
    # After </form>, there are some closing divs for the column:
    # </div>\n</div></div></div></div>
    # Let's find the first '<div class="fusion-layout-column' after </form> OR the end of the row.
    # Actually, we can just find the string `\n</div>\n\n</div></div></div></div></div>` which is line 782-784.
    
    end_divs = c.find('</div>\n\n</div></div></div></div></div>', end)
    if end_divs != -1:
        chunk = c[start:end_divs + 7] # remove up to </div>\n
        
        # Verify chunk looks correct
        print(f"Removing {len(chunk)} chars from {f}")
        
        new_c = c.replace(chunk, '')
        
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(new_c)
        print(f"Saved {f}")
    else:
        print("Could not find end divs")
