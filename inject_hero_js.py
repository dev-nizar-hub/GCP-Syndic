import glob
import re

HERO_JS = """
    <!-- GCP Hero Background Fix -->
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        // Avada stores the hero image in a CSS custom property --awb-background-image
        // When the browser parses the HTML, &quot; becomes " so getAttribute returns decoded string
        document.querySelectorAll('[style]').forEach(function(el) {
            var style = el.getAttribute('style') || '';
            if (style.indexOf('awb-background-image') === -1) return;
            // Match url("...") or url('...') or url(...)
            var match = style.match(/--awb-background-image\s*:\s*url\s*\(["']?([^"')]+)["']?\)/);
            if (match && match[1]) {
                var imgUrl = match[1];
                el.style.backgroundImage = "url('" + imgUrl + "')";
                el.style.backgroundSize = 'cover';
                el.style.backgroundPosition = 'center center';
                el.style.backgroundRepeat = 'no-repeat';
            }
        });
    });
    </script>
    <!-- /GCP Hero Background Fix -->
"""

html_files = glob.glob('public/*.html')
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    # Remove old injection
    html = re.sub(r'<!-- GCP Hero Background Fix -->.*?<!-- /GCP Hero Background Fix -->', '', html, flags=re.DOTALL)
    
    # Inject before </body>
    if '</body>' in html:
        html = html.replace('</body>', HERO_JS + '</body>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated hero background JS on all pages.")
