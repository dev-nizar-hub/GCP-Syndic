import os
import re
import glob
import math

# Brand palette
BRAND_COLORS = {
    'white':      (255, 255, 255),
    'dark_blue':  (10,  38,  49),
    'blue':       (49,  123, 255),
}

def hex_to_rgb(h):
    h = h.lstrip('#')
    if len(h) == 3:
        h = ''.join(c*2 for c in h)
    try:
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    except:
        return None

def rgb_distance(c1, c2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))

def closest_brand_color(hex_code):
    rgb = hex_to_rgb(hex_code)
    if rgb is None:
        return hex_code
    best = min(BRAND_COLORS.items(), key=lambda item: rgb_distance(rgb, item[1]))
    name, col = best
    return '#{:02x}{:02x}{:02x}'.format(*col)

def replace_hex_colors(text):
    def replacer(m):
        return closest_brand_color(m.group(0))
    return re.sub(r'#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}\b', replacer, text)

def replace_rgb_colors(text):
    def replacer(m):
        r, g, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
        rgb = (r, g, b)
        best_name, best_col = min(BRAND_COLORS.items(), key=lambda item: rgb_distance(rgb, item[1]))
        return '#{:02x}{:02x}{:02x}'.format(*best_col)
    return re.sub(r'rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)', replacer, text)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    original = content
    content = replace_hex_colors(content)
    content = replace_rgb_colors(content)
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")

# Process Avada fusion CSS
avada_css = glob.glob('public/assets/wp-content/themes/Avada/**/*.css', recursive=True)
for f in avada_css:
    process_file(f)

# Process fusion-styles
fusion_css = glob.glob('public/assets/wp-content/uploads/fusion-styles/**/*.css', recursive=True)
for f in fusion_css:
    process_file(f)

# Process formidable plugin CSS
formidable_css = glob.glob('public/assets/wp-content/plugins/**/*.css', recursive=True)
for f in formidable_css:
    process_file(f)

print("\nDone! Avada & plugin CSS color enforcement complete.")
