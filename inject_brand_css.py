import glob
import re

OVERRIDE_CSS = """
    <!-- GCP Brand Color Override -->
    <style id="gcp-brand-override">
        /* ===== FORCE 3-COLOR PALETTE EVERYWHERE ===== */
        
        /* Background overrides */
        *,
        *::before,
        *::after {
            border-color: #0a2631 !important;
        }
        
        /* === DARK BLUE: headers, footers, dark sections === */
        .fusion-header-wrapper,
        .fusion-header,
        .fusion-sticky-header-wrapper,
        .fusion-secondary-header,
        .fusion-footer,
        .fusion-footer-widget-area,
        .fusion-footer-copyright-area,
        #wrapper .fusion-footer-widget-area,
        .fusion-sliding-bar-area,
        .awb-sticky .fusion-header-wrapper,
        [style*="background-color:#05161d"],
        [style*="background-color:#0a2631"],
        [style*="background-color:#2a2e38"],
        [style*="background-color:#313131"],
        [style*="background-color:#333"],
        [style*="background-color:#212121"],
        [style*="background-color:#000"],
        [style*="--awb-bg-color:#05161d"],
        [style*="--awb-bg-color:#0a2631"],
        [style*="--awb-background-color:#0a2631"] {
            background-color: #0a2631 !important;
        }
        
        .fusion-header-wrapper *,
        .fusion-header *,
        .fusion-footer *,
        .fusion-footer-widget-area * {
            color: #ffffff !important;
        }
        
        /* === WHITE: main content areas, card backgrounds === */
        body,
        #wrapper,
        .fusion-page-title-bar,
        .post-content,
        .fusion-layout-column .fusion-column-wrapper,
        .fusion-fullwidth.fusion-section-1,
        .fusion-row {
            background-color: #ffffff !important;
        }

        /* All text defaults */
        body, p, li, span, div, td, th, label, a:not(.fusion-button) {
            color: #0a2631 !important;
        }
        
        /* === BLUE: all buttons, links, accents === */
        a:not(.fusion-button):hover,
        .fusion-button,
        .fusion-button-wrapper a,
        .fusion-button.button-default,
        .fusion-button.button-medium,
        .fusion-button.button-large,
        .fusion-button.button-xlarge,
        input[type="submit"],
        button[type="submit"],
        .awb-menu__main-a:hover,
        .awb-menu__main-a.current-menu-item,
        .fusion-tabs .nav-tabs > li.active > a,
        h1 a:hover, h2 a:hover, h3 a:hover {
            background-color: #317bff !important;
            color: #ffffff !important;
            border-color: #317bff !important;
        }
        
        /* Headings in blue */
        h1, h2, h3, h4, h5, h6 {
            color: #0a2631 !important;
        }
        
        /* SVG icons -- force color */
        svg path, svg circle, svg rect, svg polygon {
            fill: #317bff !important;
        }
        
        /* Override ALL inline background colors in style attributes */
        [style*="background-color:#cf2e2e"],
        [style*="background-color:#db182a"],
        [style*="background-color:#e10707"],
        [style*="background-color:#ff6900"],
        [style*="background-color:#00d084"],
        [style*="background-color:#fcb900"],
        [style*="background-color:#9b51e0"],
        [style*="background-color:#0693e3"],
        [style*="background-color:#3b5998"],
        [style*="background-color:#0077b5"] {
            background-color: #317bff !important;
        }
        
        /* Force all light gray / off-white to white */
        [style*="background-color:#f6f6f6"],
        [style*="background-color:#f2f2f2"],
        [style*="background-color:#f9f9f9"],
        [style*="background-color:#e6e6e6"],
        [style*="background-color:#eee"],
        [style*="background-color:#ebebeb"],
        [style*="background-color:#e8e8e8"],
        .fusion-content-boxes .fusion-content-box-button,
        .fusion-content-box-wrapper {
            background-color: #ffffff !important;
        }
        
        /* Inline color text overrides */
        [style*="color:#cf2e2e"],
        [style*="color:#db182a"],
        [style*="color:#e10707"],
        [style*="color:#ff6900"],
        [style*="color:#317bff"],
        [style*="color:#0693e3"],
        [style*="color:#0077b5"],
        [style*="color:#3b5998"] {
            color: #317bff !important;
        }
        
        /* Borders */
        .fusion-content-box-wrapper,
        .fusion-panel,
        input, select, textarea {
            border-color: #0a2631 !important;
        }
        
        input, select, textarea {
            background-color: #ffffff !important;
            color: #0a2631 !important;
        }
        
        /* Section backgrounds with images keep their images */
        .fusion-fullwidth[style*="background-image"] {
            background-color: transparent !important;
        }
        
        /* Highlighted titles */
        .fusion-title .fusion-title-heading,
        .fusion-title-size-one, .fusion-title-size-two,
        .fusion-title-size-three, .fusion-title-size-four {
            color: #0a2631 !important;
        }
        
        /* Active/hover nav menu items */
        .awb-menu__main-li:hover .awb-menu__main-a,
        .awb-menu__main-li.current-menu-item .awb-menu__main-a,
        .awb-menu__main-li.current-menu-ancestor .awb-menu__main-a {
            color: #317bff !important;
            background-color: transparent !important;
        }
    </style>
    <!-- /GCP Brand Color Override -->
"""

html_files = glob.glob('public/*.html')
updated = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove any previous override injection
    html = re.sub(r'<!-- GCP Brand Color Override -->.*?<!-- /GCP Brand Color Override -->', '', html, flags=re.DOTALL)
    
    # Inject before </head>
    if '</head>' in html:
        html = html.replace('</head>', OVERRIDE_CSS + '</head>')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    updated += 1
    print(f"Injected: {filepath}")

print(f"\nDone! Injected brand override CSS into {updated} pages.")
