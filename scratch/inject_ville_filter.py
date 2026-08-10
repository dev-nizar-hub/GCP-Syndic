"""
Inject URL-parameter auto-filter into nos-biens-achat.html and nos-biens-location.html.
"""

FILTER_JS = """
  // Auto-filter from URL parameter ?ville=CityName (set by map pins on the homepage)
  var _params = new URLSearchParams(window.location.search);
  var _villeParam = _params.get("ville");
  if(_villeParam){
    var _decodedVille = decodeURIComponent(_villeParam);
    var _cityEl = document.querySelector('select[id^="field_y68yj"]');
    if(_cityEl){
      for(var _i=0;_i<_cityEl.options.length;_i++){
        if(_cityEl.options[_i].value === _decodedVille){ _cityEl.value = _decodedVille; break; }
      }
    }
    var _cards = document.querySelectorAll(".gcp-pc[data-city]");
    var _GCP_ACTIVE = typeof GCP_ACTIVE_CITIES !== "undefined" ? GCP_ACTIVE_CITIES : [];
    var _visible = 0;
    _cards.forEach(function(card){
      var cc = card.getAttribute("data-city") || "";
      if(cc === _decodedVille){ _visible++; }
      else{ card.classList.add("gcp-hidden"); card.style.setProperty("display","none","important"); }
    });
    if(_GCP_ACTIVE.length > 0 && _GCP_ACTIVE.indexOf(_decodedVille) === -1){
      _cards.forEach(function(card){ card.classList.add("gcp-hidden"); card.style.setProperty("display","none","important"); });
      if(typeof gcpGetOrCreateBanner === "function"){
        var _bCss = "display:inline-block;background:#00205b;color:#fff;padding:14px 36px;border-radius:8px;text-decoration:none;font-weight:600;font-size:1rem;";
        var _csHtml = "<div style='max-width:600px;margin:0 auto;background:linear-gradient(135deg,#f8f9ff,#e8f0fe);border-radius:16px;padding:60px 40px;box-shadow:0 8px 32px rgba(0,80,200,0.1);'><img src='/logo-transparent.png' style='height:120px;margin-bottom:24px;'/><h2 style='color:#00205b;font-size:2rem;margin-bottom:16px;'>Bient\\u00f4t disponible</h2><p style='color:#555;font-size:1.1rem;line-height:1.7;margin-bottom:32px;'>GCP Syndic arrive bient\\u00f4t dans <strong>"+_decodedVille+"</strong>\\u00a0!</p><a href='/contact.html' style='"+_bCss+"'>Nous contacter</a></div>";
        var _csEl = gcpGetOrCreateBanner("gcp-coming-soon", _csHtml);
        _csEl.classList.remove("gcp-hidden"); _csEl.style.setProperty("display","block","important");
      }
    } else if(_visible === 0 && typeof gcpGetOrCreateBanner === "function"){
      var _nrHtml = "<div style='max-width:500px;margin:0 auto;'><div style='font-size:48px;margin-bottom:16px;'>&#128269;</div><h3 style='color:#00205b;font-size:1.5rem;margin-bottom:12px;'>Aucun r\\u00e9sultat trouv\\u00e9</h3><p style='color:#777;font-size:1rem;'>Aucun bien ne correspond \\u00e0 <strong>"+_decodedVille+"</strong> pour le moment.</p></div>";
      var _nrEl = gcpGetOrCreateBanner("gcp-no-results", _nrHtml);
      _nrEl.classList.remove("gcp-hidden"); _nrEl.style.setProperty("display","block","important");
    }
    setTimeout(function(){
      var _section = document.querySelector(".gcp-pc[data-city]");
      if(_section) _section.scrollIntoView({behavior:"smooth", block:"start"});
    }, 300);
  }
"""

files = [
    'public/nos-biens-achat.html',
    'public/nos-biens-location.html',
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    if '_villeParam' in html:
        print('Already patched: ' + fpath)
        continue

    # Find closing of the DOMContentLoaded listener
    # Pattern: the forEach ends with   });\n});\n
    # The final }); closes the addEventListener callback
    
    needle_end = '  });\n});\n'
    pos = html.find(needle_end)
    if pos == -1:
        needle_end = '  });\r\n});\r\n'
        pos = html.find(needle_end)
    
    if pos == -1:
        print('Pattern not found in: ' + fpath)
        continue
    
    # Insert before the final }); which closes addEventListener  
    # needle_end starts with '  });' (forEach close) then closes addEventListener with '});'
    # We want to insert after the forEach close but before the addEventListener close
    
    # Split: inject FILTER_JS just before the closing });\n of addEventListener
    inner_close = pos + len(needle_end) - len('});\n')
    if html[inner_close:inner_close+3] != '});':
        inner_close = pos + len(needle_end) - len('});\r\n')
    
    new_html = html[:inner_close] + FILTER_JS + html[inner_close:]
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print('Patched: ' + fpath)
