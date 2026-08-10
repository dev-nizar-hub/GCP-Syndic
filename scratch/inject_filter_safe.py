"""
Surgical filter injector - uses regex string manipulation only.
Never re-serializes the HTML, so the Avada CSS grid layout is preserved perfectly.
"""
import re
import random

# ── City / dropdown data ────────────────────────────────────────────────────
ACTIVE_CITIES = ["Meknès", "Kénitra", "Tanger", "Oujda"]

ALL_MOROCCAN_CITIES = sorted([
    "Agadir", "Al Hoceïma", "Béni Mellal", "Berkane", "Berrechid",
    "Casablanca", "Chefchaouen", "Dakhla", "El Jadida", "Errachidia",
    "Essaouira", "Fès", "Guelmim", "Ifrane", "Kénitra", "Khemisset",
    "Khenifra", "Khouribga", "Laâyoune", "Larache", "Marrakech",
    "Meknès", "Mohammedia", "Nador", "Ouarzazate", "Oujda", "Rabat",
    "Safi", "Salé", "Sefrou", "Settat", "Sidi Kacem", "Tanger",
    "Taroudant", "Taza", "Témara", "Tétouan", "Tiznit", "Zagora"
])

PROPERTY_TYPES = [
    "Appartement", "Villa", "Maison", "Studio", "Duplex",
    "Riad", "Garage", "Terrain", "Bureau", "Local commercial"
]

ROOM_NUMBERS = [
    "1 pièce", "2 pièces", "3 pièces", "4 pièces", "5 pièces", "5+ pièces"
]

# ── The JS filter block ─────────────────────────────────────────────────────
FILTER_JS = """\
<script>
var GCP_ACTIVE_CITIES=["Mekn\\u00e8s","K\\u00e9nitra","Tanger","Oujda"];

function gcpGetOrCreateBanner(id, innerHtml){
  var el=document.getElementById(id);
  if(!el){
    el=document.createElement("div");
    el.id=id;
    el.className="gcp-hidden";
    el.style.cssText="text-align:center;padding:60px 20px;";
    el.innerHTML=innerHtml;
    // Insert BEFORE the first real property card's grandparent (the fullwidth section)
    var firstCard=document.querySelector(".gcp-pc[data-city]");
    if(firstCard){
      var row=firstCard.parentElement;
      if(row&&row.parentElement) row.parentElement.insertBefore(el,row);
      else document.body.appendChild(el);
    } else {
      document.body.appendChild(el);
    }
  }
  return el;
}

function gcpRunFilter(btn){
  var form=btn;
  while(form&&!(form.classList&&form.classList.contains("frm-show-form")))form=form.parentElement;
  var cityEl=form?form.querySelector('select[id^="field_y68yj"]'):null;
  var typeEl=form?form.querySelector('select[id^="field_um9ky"]'):null;
  var roomsEl=form?form.querySelector('select[id^="field_qfq1i"]'):null;
  var city=cityEl?cityEl.value||"":"";
  var type=typeEl?typeEl.value||"":"";
  var rooms=roomsEl?roomsEl.value||"":"";
  city=city.trim();type=type.trim();rooms=rooms.replace(/\\u00a0/g," ").trim();
  var cards=document.querySelectorAll(".gcp-pc[data-city]");
  var cs=gcpGetOrCreateBanner("gcp-coming-soon","<div style='max-width:600px;margin:0 auto;background:linear-gradient(135deg,#f8f9ff,#e8f0fe);border-radius:16px;padding:60px 40px;box-shadow:0 8px 32px rgba(0,80,200,0.1);'><img src='/logo-transparent.png' alt='GCP Syndic' style='height:120px;margin-bottom:24px;'/><h2 style='color:#00205b;font-size:2rem;margin-bottom:16px;'>Bient&ocirc;t disponible</h2><p style='color:#555;font-size:1.1rem;line-height:1.7;margin-bottom:32px;'>GCP Syndic arrive dans cette ville&nbsp;! Nous travaillons activement &agrave; l&rsquo;expansion de notre portefeuille immobilier.<br><br>Revenez bient&ocirc;t ou contactez-nous pour &ecirc;tre inform&eacute; en priorit&eacute;.</p><a href='/contact.html' style='display:inline-block;background:#00205b;color:#fff;padding:14px 36px;border-radius:8px;text-decoration:none;font-weight:600;font-size:1rem;'>Nous contacter</a></div>");
  var nr=gcpGetOrCreateBanner("gcp-no-results","<div style='max-width:500px;margin:0 auto;'><div style='font-size:48px;margin-bottom:16px;'>&#128269;</div><h3 style='color:#00205b;font-size:1.5rem;margin-bottom:12px;'>Aucun r&eacute;sultat trouv&eacute;</h3><p style='color:#777;font-size:1rem;'>Aucun bien ne correspond &agrave; votre recherche pour le moment.<br>Essayez de modifier vos crit&egrave;res ou revenez bient&ocirc;t.</p></div>");
  cs.classList.add("gcp-hidden");cs.style.setProperty("display","none","important");
  nr.classList.add("gcp-hidden");nr.style.setProperty("display","none","important");
  cards.forEach(function(c){c.classList.remove("gcp-hidden");c.style.removeProperty("display");});
  if(city&&GCP_ACTIVE_CITIES.indexOf(city)===-1){
    cards.forEach(function(c){c.classList.add("gcp-hidden");c.style.setProperty("display","none","important");});
    cs.classList.remove("gcp-hidden");cs.style.setProperty("display","block","important");
    return;
  }
  var visible=0;
  cards.forEach(function(card){
    var cc=card.getAttribute("data-city")||"";
    var ct=card.getAttribute("data-type")||"";
    var cr=(card.getAttribute("data-rooms")||"").replace(/\\u00a0/g," ").trim();
    var cok=!city||cc===city;
    var tok=!type||ct===type;
    var rok=true;
    if(rooms){
      if(rooms==="5+ pi\\u00e8ces"){var m=cr.match(/(\\d+)/);rok=m?parseInt(m[1])>=5:false;}
      else rok=cr===rooms;
    }
    if(cok&&tok&&rok){visible++;}
    else{card.classList.add("gcp-hidden");card.style.setProperty("display","none","important");}
  });
  if(visible===0){nr.classList.remove("gcp-hidden");nr.style.setProperty("display","block","important");}
}
</script>
<style>.gcp-hidden{display:none!important;}</style>"""


def build_city_options():
    parts = ['<option selected="selected" value=""> </option>']
    for c in ALL_MOROCCAN_CITIES:
        parts.append(f'<option value="{c}">{c}</option>')
    return ''.join(parts)


def build_type_options():
    parts = ['<option selected="selected" value=""> </option>']
    for t in PROPERTY_TYPES:
        parts.append(f'<option value="{t}">{t}</option>')
    return ''.join(parts)


def build_rooms_options():
    parts = ['<option selected="selected" value=""> </option>']
    for r in ROOM_NUMBERS:
        parts.append(f'<option value="{r}">{r}</option>')
    return ''.join(parts)


def inject(filepath, active_city_list):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # ── 1. Replace city dropdown options ─────────────────────────────────
    # The select has id="field_y68yj" — replace its content
    html = re.sub(
        r'(<select[^>]*id="field_y68yj"[^>]*>)(.*?)(</select>)',
        lambda m: m.group(1) + build_city_options() + m.group(3),
        html, flags=re.DOTALL
    )

    # ── 2. Replace type dropdown options ─────────────────────────────────
    html = re.sub(
        r'(<select[^>]*id="field_um9ky"[^>]*>)(.*?)(</select>)',
        lambda m: m.group(1) + build_type_options() + m.group(3),
        html, flags=re.DOTALL
    )

    # ── 3. Replace rooms dropdown options ─────────────────────────────────
    html = re.sub(
        r'(<select[^>]*id="field_qfq1i"[^>]*>)(.*?)(</select>)',
        lambda m: m.group(1) + build_rooms_options() + m.group(3),
        html, flags=re.DOTALL
    )

    # ── 4. Reassign all property card cities to the 4 active cities ──────
    def replace_lieu(m):
        city = random.choice(active_city_list)
        return f'<p class="lieu">{city}</p>'

    html = re.sub(r'<p class="lieu">.*?</p>', replace_lieu, html)

    # ── 5. Add data-city/type/rooms attributes to each property column ────
    # Strategy: after each match of class="lieu">CITY</p>, look up 2 siblings
    # We do this by processing each fusion-layout-column block that contains "type_bien"
    
    def add_data_attrs(m):
        block = m.group(0)
        # Extract type
        type_m = re.search(r'<p class="type_bien">(.*?)</p>', block)
        # Extract lieu
        lieu_m = re.search(r'<p class="lieu">(.*?)</p>', block)
        # Extract nbp
        nbp_m  = re.search(r'<span class="nbp">(.*?)</span>', block)

        ptype = type_m.group(1).strip() if type_m else ""
        city  = lieu_m.group(1).strip() if lieu_m else ""
        rooms = nbp_m.group(1).strip()  if nbp_m  else ""

        # Add data attrs and gcp-pc class to the opening tag
        # The opening tag is the first <div class="fusion-layout-column ...">
        def patch_opening_tag(tag_m):
            tag = tag_m.group(0)
            # Only add gcp-pc if this block is a real property card
            if ptype or city:
                tag = tag.rstrip('>')
                tag += f' data-city="{city}" data-type="{ptype}" data-rooms="{rooms}">'
                tag = tag.replace('fusion-column-inner-bg-wrapper',
                                  'fusion-column-inner-bg-wrapper gcp-pc', 1)
            return tag

        block = re.sub(
            r'<div class="fusion-layout-column[^>]*fusion-column-inner-bg-wrapper[^>]*>',
            patch_opening_tag, block, count=1
        )
        return block

    # Match each complete property column (they contain type_bien class)
    html = re.sub(
        r'<div class="fusion-layout-column[^"]*fusion-column-inner-bg-wrapper[^"]*"[^>]*>.*?(?=<div class="fusion-layout-column|$)',
        add_data_attrs, html, flags=re.DOTALL
    )

    # ── 6. Fix Valider buttons (prevent form submit, call JS) ─────────────
    html = re.sub(
        r'<button class="frm_button_submit([^"]*)" type="submit">Valider</button>',
        r'<button class="frm_button_submit\1" type="button" onclick="gcpRunFilter(this);return false;">Valider</button>',
        html
    )

    # ── 6b. Remove <form> tags entirely to disable Formidable AJAX submit JS ──
    html = re.sub(r'<form\b([^>]*)>', r'<div\1>', html)
    html = re.sub(r'</form>', r'</div>', html)

    # ── 6c. Remove the entire "Nouvelle recherche" section ───────────────────
    # It starts at a fusion-layout-column with id "fusion-builder-column-12"
    # and ends with </div></div></div></div></div> a few lines later.
    # Use a precise string marker to cut it out.
    marker_start = '<div class="fusion-layout-column fusion_builder_column fusion-builder-column-12'
    marker_end   = '</div></div></div></div></div>\n</div>\n</div>\n</section>'
    if marker_start in html:
        s = html.index(marker_start)
        e = html.find(marker_end, s)
        if e != -1:
            html = html[:s] + '</div></div></div></div></div>\n</div>\n</div>\n</section>' + html[e + len(marker_end):]

    # ── 7. Inject JS just before </body> ──────────────────────────────────
    # Remove old injections first
    html = re.sub(r'<div id="gcp-coming-soon".*?</div>\s*</div>', '', html, flags=re.DOTALL)
    html = re.sub(r'<div id="gcp-no-results".*?</div>\s*</div>', '', html, flags=re.DOTALL)
    html = re.sub(r'<script>\s*var GCP_ACTIVE_CITIES.*?</script>\s*<style>.*?</style>', '', html, flags=re.DOTALL)

    # JS creates and positions banners dynamically at runtime
    html = html.replace('</body>', FILTER_JS + '\n</body>', 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Done: {filepath}")


inject('public/nos-biens-achat.html',    ACTIVE_CITIES)
inject('public/nos-biens-location.html', ACTIVE_CITIES)
