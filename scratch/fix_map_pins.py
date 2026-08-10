html_file = 'public/atrium.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the map section and replace it entirely
import re

# Match from the comment to the closing </div> of the outer map container
pattern = re.compile(
    r'  <!-- Static Map with clickable animated pins? -->.*?  </div>',
    re.DOTALL
)

new_section = '''  <!-- Static Map with clickable animated pins -->
  <div style="border-radius:12px;overflow:hidden;box-shadow:0 4px 30px rgba(10,38,49,0.12);background:#fff;padding:20px;">
    <!-- Inner wrapper sized to image so pin percentages map directly to image coordinates -->
    <div style="position:relative;display:block;width:100%;">
      <img src="/maroc-map.png" alt="Nos agences GCP Syndic au Maroc"
           style="width:100%;height:auto;display:block;" />

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
          background:#0a2631;color:#fff;padding:4px 10px;border-radius:4px;font-size:13px;font-weight:600;
          font-family:'Poppins',sans-serif;margin-top:4px;white-space:nowrap;opacity:0;transition:opacity .2s;pointer-events:none;
        }
        .gcp-map-pin:hover .gcp-pin-tooltip { opacity:1 !important; }
      </style>

      <!-- Tanger: top-center of Morocco territory -->
      <a href="#" class="gcp-map-pin" style="left:64.5%;top:9.8%;" title="Tanger">
        <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" style="filter:drop-shadow(0 4px 8px rgba(0,0,0,0.35));"><path fill="#317bff" d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle fill="#fff" cx="12" cy="9" r="3"/></svg>
        <span class="gcp-pin-tooltip">Tanger</span>
      </a>

      <!-- Kenitra: west coast, Rabat-Sale-Kenitra region -->
      <a href="#" class="gcp-map-pin" style="left:53%;top:19.5%;" title="Kenitra">
        <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" style="filter:drop-shadow(0 4px 8px rgba(0,0,0,0.35));"><path fill="#317bff" d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle fill="#fff" cx="12" cy="9" r="3"/></svg>
        <span class="gcp-pin-tooltip">K\u00e9nitra</span>
      </a>

      <!-- Meknes: inland in the Fes-Meknes region -->
      <a href="#" class="gcp-map-pin" style="left:64%;top:24.5%;" title="Meknes">
        <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" style="filter:drop-shadow(0 4px 8px rgba(0,0,0,0.35));"><path fill="#317bff" d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle fill="#fff" cx="12" cy="9" r="3"/></svg>
        <span class="gcp-pin-tooltip">Mekn\u00e8s</span>
      </a>

      <!-- Oujda: far east, L'Oriental region near Algeria border -->
      <a href="#" class="gcp-map-pin" style="left:85%;top:24%;" title="Oujda">
        <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" style="filter:drop-shadow(0 4px 8px rgba(0,0,0,0.35));"><path fill="#317bff" d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle fill="#fff" cx="12" cy="9" r="3"/></svg>
        <span class="gcp-pin-tooltip">Oujda</span>
      </a>

    </div>
  </div>'''

new_content, n = pattern.subn(new_section, content, count=1)
print(f"Replaced {n} occurrences")

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)
