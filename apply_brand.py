import os
import glob
import re

html_files = glob.glob('public/*.html')

css_injection = """
    <style>
        :root {
            --awb-color1: #0a2631 !important;
            --awb-color2: #317bff !important;
            --awb-active-color: #317bff !important;
            --primary-color: #317bff !important;
            --dark-color: #0a2631 !important;
        }
        
        /* Enforce Dark Blue on headers and footers */
        .fusion-header, .fusion-header-wrapper, .fusion-footer {
            background-color: #0a2631 !important;
        }
        
        /* Enforce Blue on buttons and primary links */
        .fusion-button, .fusion-button-wrapper a, .awb-menu__main-a:hover {
            background-color: #317bff !important;
            border-color: #317bff !important;
        }
        
        /* Typography overrides to match PDF intent */
        * {
            --awb-fusion-font-family-typography: 'Josefin Sans', sans-serif !important;
            --h1_typography-font-family: 'Josefin Sans', sans-serif !important;
            --h2_typography-font-family: 'Josefin Sans', sans-serif !important;
            --h3_typography-font-family: 'Josefin Sans', sans-serif !important;
            --h4_typography-font-family: 'Josefin Sans', sans-serif !important;
            --body_typography-font-family: 'Raleway', sans-serif !important;
        }
        
        body, p, li, td, .fusion-text, input, textarea, select, label {
            font-family: 'Raleway', sans-serif !important;
        }
        
        h1, h2, h3, h4, h5, h6, .fusion-title-heading, .menu-text, .awb-menu__main-a, .awb-menu__sub-a, .fusion-button-text {
            font-family: 'Josefin Sans', sans-serif !important;
        }
    </style>
"""

# Regex patterns for the old logos
old_logos = [
    r'/assets/wp-content/uploads/2022/03/picto-atrium\.png',
    r'/assets/wp-content/uploads/2024/12/picto-atrium\.jpg',
    r'/assets/wp-content/uploads/2021/02/marqueur\.png',
    r'logo/Gestion\s*copropriété\.png',
    r'logo/Gestion%20copropri%C3%A9t%C3%A9\.png',
    r'logo/logo-gcp\.jpeg',
    r'logo-gcp\.jpeg',
    r'logo/Gestion\s*copropriété\s*Blue\s*White\s*BG\.jpg\.jpeg',
    r'logo/Gestion%20copropri%C3%A9t%C3%A9%20Blue%20White%20BG\.jpg\.jpeg'
]

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace old logos with /logo.png
    for pattern in old_logos:
        html = re.sub(pattern, '/logo.png', html, flags=re.IGNORECASE)
    
    # Also catch any raw /assets/wp-content/uploads/2022/03/picto-atrium.png without leading slash if present
    html = html.replace('assets/wp-content/uploads/2022/03/picto-atrium.png', '/logo.png')
    
    # Inject CSS before </head>
    if '<style>' not in html or '--awb-color1: #0a2631' not in html:
        html = html.replace('</head>', f'{css_injection}</head>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Successfully applied brand visual identity to all HTML files.")
