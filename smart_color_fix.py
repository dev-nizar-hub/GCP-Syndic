import re
import glob
import math

# Brand palette
WHITE     = (255, 255, 255)
DARK_BLUE = (10,  38,  49)
BLUE      = (49,  123, 255)
BRAND     = [WHITE, DARK_BLUE, BLUE]
BRAND_HEX = ['#ffffff', '#0a2631', '#317bff']

def hex_to_rgb(h):
    h = h.lstrip('#')
    if len(h) == 3:
        h = ''.join(c*2 for c in h)
    if len(h) != 6:
        return None
    try:
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    except:
        return None

def closest(hex_code):
    rgb = hex_to_rgb(hex_code)
    if rgb is None:
        return hex_code
    dists = [math.sqrt(sum((a-b)**2 for a,b in zip(rgb, brand))) for brand in BRAND]
    return BRAND_HEX[dists.index(min(dists))]

def replace_in_style_attrs(html):
    """
    Only replace hex colors that appear INSIDE style="..." attribute values.
    This avoids corrupting any visible text content.
    """
    def replace_style(m):
        style_content = m.group(1)
        # Replace all hex codes within this style string
        def repl_hex(hm):
            return closest(hm.group(0))
        new_style = re.sub(r'#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}\b', repl_hex, style_content)
        # Also replace rgb(r,g,b) inside style
        def repl_rgb(rm):
            r,g,b = int(rm.group(1)),int(rm.group(2)),int(rm.group(3))
            rgb = (r,g,b)
            dists = [math.sqrt(sum((a-b_)**2 for a,b_ in zip(rgb, brand))) for brand in BRAND]
            return BRAND_HEX[dists.index(min(dists))]
        new_style = re.sub(r'rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)', repl_rgb, new_style)
        return f' style="{new_style}"'
    
    # Match style="..." attributes  
    html = re.sub(r' style="([^"]*)"', replace_style, html)
    return html

def replace_in_style_blocks(html):
    """
    Replace hex colors inside <style>...</style> blocks (not in text content).
    """
    def replace_block(m):
        block = m.group(0)
        def repl_hex(hm):
            return closest(hm.group(0))
        block = re.sub(r'#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}\b', repl_hex, block)
        def repl_rgb(rm):
            r,g,b = int(rm.group(1)),int(rm.group(2)),int(rm.group(3))
            rgb = (r,g,b)
            dists = [math.sqrt(sum((a-b_)**2 for a,b_ in zip(rgb, brand))) for brand in BRAND]
            return BRAND_HEX[dists.index(min(dists))]
        block = re.sub(r'rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)', repl_rgb, block)
        return block
    
    # Match <style>...</style> blocks
    html = re.sub(r'<style[^>]*>.*?</style>', replace_block, html, flags=re.DOTALL)
    return html

html_files = glob.glob('public/*.html')
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    original = html
    html = replace_in_style_blocks(html)
    html = replace_in_style_attrs(html)
    
    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Updated: {filepath}')
    else:
        print(f'No change: {filepath}')

print('\nDone. Only style="" attributes and <style> blocks were modified - text content is safe.')
