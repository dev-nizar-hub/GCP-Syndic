import re

html_file = 'public/atrium.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Instead of a giant exact string, we'll use regex to match the map block
# The block starts at <!-- Static Map with clickable animated pin -->
# and ends at </div> just before </div></div></div></div></div><div class="fusion-fullwidth...

pattern = re.compile(r'<!-- Static Map with clickable animated pin -->.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)

new_map_section = '''<!-- Static Map with clickable animated pins -->
  <div style="position:relative;border-radius:12px;overflow:hidden;box-shadow:0 4px 30px rgba(10,38,49,0.12);display:block;background:#fff;padding:20px;">
    <!-- The map photo -->
    <img src="/maroc-map.png" alt="Nos agences GCP Syndic au Maroc"
         style="width:100%;height:auto;max-height:800px;object-fit:contain;display:block;margin:0 auto;" />

    <style>
      .gcp-map-pin {
        position:absolute;
        transform:translate(-50%,-100%);
        text-decoration:none;
        display:flex;
        flex-direction:column;
        align-items:center;
        cursor:pointer;
        z-index:10;
        transition:transform .2s;
      }
      .gcp-map-pin:hover { transform:translate(-50%,-110%) !important; }
      .gcp-map-pin .gcp-pin-tooltip {
        background:#0a2631;color:#fff;padding:4px 10px;border-radius:4px;font-size:13px;font-weight:600;font-family:'Poppins',sans-serif;margin-top:4px;white-space:nowrap;opacity:0;transition:opacity .2s;pointer-events:none;
      }
      .gcp-map-pin:hover .gcp-pin-tooltip { opacity:1 !important; }
    </style>

    <!-- Tanger Pin -->
    <a href="#" class="gcp-map-pin" style="left:51%;top:5%;" title="Tanger">
      <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" style="filter:drop-shadow(0 4px 8px rgba(0,0,0,0.35));"><path fill="#317bff" d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle fill="#fff" cx="12" cy="9" r="3"/></svg>
      <span class="gcp-pin-tooltip">Tanger</span>
    </a>
    
    <!-- Kénitra Pin -->
    <a href="#" class="gcp-map-pin" style="left:48%;top:20%;" title="Kénitra">
      <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" style="filter:drop-shadow(0 4px 8px rgba(0,0,0,0.35));"><path fill="#317bff" d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle fill="#fff" cx="12" cy="9" r="3"/></svg>
      <span class="gcp-pin-tooltip">Kénitra</span>
    </a>

    <!-- Meknès Pin -->
    <a href="#" class="gcp-map-pin" style="left:52%;top:25%;" title="Meknès">
      <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" style="filter:drop-shadow(0 4px 8px rgba(0,0,0,0.35));"><path fill="#317bff" d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle fill="#fff" cx="12" cy="9" r="3"/></svg>
      <span class="gcp-pin-tooltip">Meknès</span>
    </a>

    <!-- Oujda Pin -->
    <a href="#" class="gcp-map-pin" style="left:88%;top:18%;" title="Oujda">
      <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" style="filter:drop-shadow(0 4px 8px rgba(0,0,0,0.35));"><path fill="#317bff" d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle fill="#fff" cx="12" cy="9" r="3"/></svg>
      <span class="gcp-pin-tooltip">Oujda</span>
    </a>

  </div>
</div></div></div></div></div>'''

content, count = pattern.subn(new_map_section, content)
print(f"Replaced {count} occurrences")

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
