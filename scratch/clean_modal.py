import os
import re

files = ['public/nos-biens-achat.html', 'public/nos-biens-location.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The injected code started at:
    # <!-- GCP Custom Modal --> 
    # Or maybe just `<div id="gcp-overlay"`
    # Let's find the start of the injected modal/CSS
    idx1 = content.find('<!-- GCP Custom Modal -->')
    if idx1 != -1:
        content = content[:idx1] + '\n</body>\n</html>'
    else:
        # It might start with `<div id="gcp-results-area"` or something? 
        # Wait, the code I injected was usually right before </body>
        idx2 = content.find('<style id="gcp-filter-style">')
        if idx2 != -1:
            content = content[:idx2] + '\n</body>\n</html>'
        else:
            # Let's just find where it starts being weird
            pass
            
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
