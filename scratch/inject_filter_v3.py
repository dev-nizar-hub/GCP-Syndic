#!/usr/bin/env python3
"""
Fix 3 issues:
1. Remove duplicate 'Nouvelle recherche' filter (hide via JS)
2. Move results area to appear BEFORE footer (using DOM insertion)
3. Show all 4-city properties on page load by default
"""

import re, json

WHATSAPP = '212XXXXXXXXX'
ACTIVE_CITIES = ['Meknès', 'Kénitra', 'Tanger', 'Oujda']

IMGS = {
    'apt':    'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=480&q=80',
    'villa':  'https://images.unsplash.com/photo-1613977257363-707ba9348227?w=480&q=80',
    'riad':   'https://images.unsplash.com/photo-1577493340887-b7bfff550145?w=480&q=80',
    'studio': 'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=480&q=80',
    'maison': 'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=480&q=80',
    'penth':  'https://images.unsplash.com/photo-1560184897-ae75f418493e?w=480&q=80',
    'duplex': 'https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=480&q=80',
    'land':   'https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=480&q=80',
}

def p(id, type, titre, pieces, surface, quartier, prix_a, prix_l, img_key):
    return {"id": id, "type": type, "titre": titre, "pieces": pieces,
            "surface": surface, "quartier": quartier,
            "prix_achat": prix_a, "prix_location": prix_l, "img": IMGS[img_key]}

PROPERTIES = {
    "Meknès": [
        p("mk1","Appartement","Appartement 3 pièces - Hamria",3,85,"Hamria","750 000 MAD","4 500 MAD/mois","apt"),
        p("mk2","Villa","Villa standing 5 pièces - Haut Agdal",5,220,"Haut Agdal","2 200 000 MAD","15 000 MAD/mois","villa"),
        p("mk3","Studio","Studio moderne centre-ville",1,38,"Centre-ville","380 000 MAD","2 800 MAD/mois","studio"),
        p("mk4","Maison","Maison familiale 4 pièces - Hay Salam",4,140,"Hay Salam","1 100 000 MAD","7 000 MAD/mois","maison"),
        p("mk5","Appartement","Appartement résidence sécurisée Al Menzeh",2,65,"Al Menzeh","580 000 MAD","3 500 MAD/mois","penth"),
        p("mk6","Riad","Riad authentique en Médina",6,280,"Médina","1 800 000 MAD","12 000 MAD/mois","riad"),
        p("mk7","Duplex","Duplex moderne 3 pièces - Hay Salam",3,110,"Hay Salam","950 000 MAD","6 000 MAD/mois","duplex"),
        p("mk8","Terrain","Terrain constructible 500m² - Route Ifrane",0,500,"Route d'Ifrane","650 000 MAD","N/A","land"),
    ],
    "Kénitra": [
        p("kn1","Appartement","Appartement 2 pièces - Cité Bassatine",2,65,"Cité Bassatine","620 000 MAD","3 800 MAD/mois","apt"),
        p("kn2","Villa","Villa 4 pièces - Quartier Administratif",4,190,"Quartier Administratif","1 900 000 MAD","13 000 MAD/mois","villa"),
        p("kn3","Studio","Studio centre-ville Kénitra",1,32,"Centre-ville","350 000 MAD","2 500 MAD/mois","studio"),
        p("kn4","Duplex","Duplex Résidence Oued Sebou",3,110,"Oued Sebou","980 000 MAD","6 000 MAD/mois","duplex"),
        p("kn5","Appartement","Grand appartement lumineux 3 pièces",3,88,"Quartier Hassan","720 000 MAD","4 200 MAD/mois","penth"),
        p("kn6","Maison","Maison avec jardin 4 pièces",4,150,"Hay Bitat","1 100 000 MAD","7 500 MAD/mois","maison"),
    ],
    "Tanger": [
        p("tg1","Appartement","Appartement vue mer - Malabata",3,95,"Malabata","950 000 MAD","6 000 MAD/mois","penth"),
        p("tg2","Villa","Villa luxe 5 pièces - California",5,280,"California","3 500 000 MAD","22 000 MAD/mois","villa"),
        p("tg3","Riad","Riad Médina de Tanger 6 pièces",6,320,"Médina","2 200 000 MAD","15 000 MAD/mois","riad"),
        p("tg4","Studio","Studio vue mer - Bou Khalf",1,40,"Bou Khalf","420 000 MAD","3 200 MAD/mois","studio"),
        p("tg5","Penthouse","Penthouse front de mer 4 pièces",4,160,"Front de mer","2 800 000 MAD","18 000 MAD/mois","apt"),
        p("tg6","Appartement","Appartement moderne 2 pièces - Centre",2,72,"Centre","750 000 MAD","4 800 MAD/mois","apt"),
        p("tg7","Maison","Maison 4 pièces vue détroit",4,165,"Cap Spartel","1 500 000 MAD","9 500 MAD/mois","maison"),
    ],
    "Oujda": [
        p("oj1","Appartement","Appartement 2 pièces - Centre-ville",2,72,"Centre-ville","550 000 MAD","3 200 MAD/mois","apt"),
        p("oj2","Maison","Maison familiale - Hay Al Qods",4,145,"Hay Al Qods","950 000 MAD","6 500 MAD/mois","maison"),
        p("oj3","Villa","Villa résidence privée 5 pièces",5,200,"Complexe résidentiel","1 700 000 MAD","11 000 MAD/mois","villa"),
        p("oj4","Studio","Studio Nouveau Centre",1,35,"Nouveau Centre","320 000 MAD","2 200 MAD/mois","studio"),
        p("oj5","Appartement","Appartement 3 pièces - Quartier Lazaret",3,84,"Quartier Lazaret","680 000 MAD","4 000 MAD/mois","apt"),
        p("oj6","Duplex","Duplex moderne 3 pièces - Hay Al Wafa",3,115,"Hay Al Wafa","920 000 MAD","5 800 MAD/mois","duplex"),
    ],
}

# ─── CSS ────────────────────────────────────────────────────────────────
CSS = """<style id="gcp-filter-style">
#gcp-results-area{max-width:1200px;margin:0 auto;padding:30px 20px 60px}
/* Fix select borders that got wiped */
.frm_pro_form select { border: 1px solid #c8d4e0 !important; border-radius: 6px !important; padding: 10px !important; background: #fff !important; }
.frm_pro_form .frm_button_submit { background: #317bff !important; color: #fff !important; border-radius: 6px !important; border: none !important; padding: 10px 24px !important; }
/* Completely hide old properties */
.fusion-builder-column-11 { display: none !important; }
/* Hide rich snippet text that leaked */
.rich-snippet-hidden { display: none !important; }

.gcp-results-title{font-family:'Raleway','Poppins',sans-serif;font-size:20px;font-weight:700;color:#0a2631;margin-bottom:6px}
.gcp-results-sub{font-size:13px;color:#8a9bb0;margin-bottom:20px}
.gcp-results-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:24px}
.gcp-prop-card{background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 2px 14px rgba(10,38,49,.08);cursor:pointer;transition:transform .22s,box-shadow .22s;border:1px solid #e8edf4}
.gcp-prop-card:hover{transform:translateY(-5px);box-shadow:0 10px 32px rgba(10,38,49,.16)}
.gcp-prop-card img{width:100%;height:200px;object-fit:cover;display:block}
.gcp-prop-body{padding:16px 18px 18px}
.gcp-prop-city{font-size:10px;font-weight:700;letter-spacing:.5px;text-transform:uppercase;color:#8a9bb0;margin-bottom:4px}
.gcp-prop-badge{display:inline-block;background:#e8f0fe;color:#317bff;font-size:10px;font-weight:700;letter-spacing:.5px;text-transform:uppercase;padding:3px 10px;border-radius:20px;margin-bottom:8px}
.gcp-prop-title{font-family:'Raleway','Poppins',sans-serif;font-weight:700;font-size:15px;color:#0a2631;margin-bottom:5px;line-height:1.35}
.gcp-prop-meta{font-size:12px;color:#8a9bb0;margin-bottom:10px}
.gcp-prop-price{font-family:'Raleway','Poppins',sans-serif;font-size:17px;font-weight:800;color:#317bff;margin-bottom:14px}
.gcp-prop-btn{display:block;width:100%;background:#317bff;color:#fff;border:none;padding:11px;border-radius:8px;font-size:12px;font-weight:700;cursor:pointer;text-align:center;transition:background .2s;font-family:'Raleway','Poppins',sans-serif;text-transform:uppercase;letter-spacing:.5px}
.gcp-prop-btn:hover{background:#1a56cc}
.gcp-coming-soon{text-align:center;padding:70px 20px;background:linear-gradient(135deg,#f0f5ff,#e8edf9);border-radius:16px;margin:30px 0}
.gcp-coming-soon .cs-emoji{font-size:64px;margin-bottom:18px}
.gcp-coming-soon h3{font-family:'Raleway','Poppins',sans-serif;font-size:24px;font-weight:800;color:#0a2631;margin-bottom:10px}
.gcp-coming-soon p{color:#8a9bb0;font-size:15px;max-width:420px;margin:0 auto 20px;line-height:1.7}
.gcp-notify-btn{display:inline-block;background:#317bff;color:#fff;padding:12px 28px;border-radius:8px;font-weight:700;font-size:13px;cursor:pointer;border:none;font-family:inherit;transition:background .2s}
.gcp-notify-btn:hover{background:#1a56cc}
.gcp-no-results{text-align:center;padding:50px 20px}
.gcp-no-results h3{font-size:18px;font-weight:700;color:#0a2631;margin-bottom:8px}
.gcp-no-results p{color:#8a9bb0;font-size:14px}
/* City section label */
.gcp-city-section{margin-bottom:40px}
.gcp-city-label{display:flex;align-items:center;gap:10px;margin-bottom:16px;padding-bottom:10px;border-bottom:2px solid #e8edf4}
.gcp-city-label h3{font-family:'Raleway','Poppins',sans-serif;font-size:16px;font-weight:700;color:#0a2631;margin:0}
.gcp-city-label span{font-size:12px;color:#8a9bb0}
/* Modal */
.gcp-overlay{display:none;position:fixed;inset:0;background:rgba(10,38,49,.6);z-index:999999;align-items:center;justify-content:center;padding:20px}
.gcp-overlay.open{display:flex}
.gcp-modal{background:#fff;border-radius:16px;max-width:500px;width:100%;overflow:hidden;box-shadow:0 24px 64px rgba(10,38,49,.28);animation:gcp-up .28s ease}
@keyframes gcp-up{from{transform:translateY(28px);opacity:0}to{transform:translateY(0);opacity:1}}
.gcp-modal-hdr{background:linear-gradient(135deg,#0a2631,#1a3d4f);color:#fff;padding:22px 24px;display:flex;align-items:flex-start;justify-content:space-between;gap:12px}
.gcp-modal-hdr h3{margin:0;font-family:'Raleway','Poppins',sans-serif;font-size:17px;font-weight:700;line-height:1.3}
.gcp-modal-hdr p{margin:4px 0 0;font-size:12px;color:#90b8cc}
.gcp-x{background:rgba(255,255,255,.15);border:none;color:#fff;width:30px;height:30px;border-radius:50%;font-size:16px;cursor:pointer;flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:background .2s}
.gcp-x:hover{background:rgba(255,255,255,.3)}
.gcp-modal-prop{background:#f5f8ff;padding:14px 24px;display:flex;gap:14px;align-items:center;border-bottom:1px solid #e8edf4}
.gcp-modal-prop img{width:78px;height:58px;object-fit:cover;border-radius:8px;flex-shrink:0}
.gcp-modal-prop .mtype{font-size:10px;font-weight:700;text-transform:uppercase;color:#317bff;letter-spacing:.5px}
.gcp-modal-prop .mtitle{font-size:13px;font-weight:700;color:#0a2631;margin:2px 0}
.gcp-modal-prop .mprice{font-size:14px;font-weight:800;color:#317bff}
.gcp-modal-body{padding:22px 24px}
.gcp-modal-body h4{margin:0 0 16px;font-size:13px;font-weight:700;color:#0a2631}
.gcp-f{margin-bottom:13px}
.gcp-f label{display:block;font-size:11px;font-weight:700;color:#5a7490;margin-bottom:5px;text-transform:uppercase;letter-spacing:.5px}
.gcp-f input{width:100%;padding:11px 14px;border:1.5px solid #d1dce8;border-radius:8px;font-size:14px;color:#0a2631;background:#f8fafc;outline:none;transition:border-color .2s,box-shadow .2s;font-family:inherit;box-sizing:border-box}
.gcp-f input:focus{border-color:#317bff;box-shadow:0 0 0 3px rgba(49,123,255,.12);background:#fff}
.gcp-wa-btn{width:100%;padding:14px;background:linear-gradient(135deg,#25D366,#128C7E);color:#fff;border:none;border-radius:8px;font-size:14px;font-weight:700;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:8px;transition:opacity .2s;font-family:inherit;margin-top:6px}
.gcp-wa-btn:hover{opacity:.9}
</style>"""

MODAL_HTML = """
<div id="gcp-results-area"></div>
<div class="gcp-overlay" id="gcp-overlay">
  <div class="gcp-modal" id="gcp-modal">
    <div class="gcp-modal-hdr">
      <div><h3>Demande d'information</h3><p id="gcp-m-sub"></p></div>
      <button class="gcp-x" onclick="gcpCloseModal()">&#x2715;</button>
    </div>
    <div class="gcp-modal-prop">
      <img id="gcp-m-img" src="" alt="">
      <div>
        <div class="mtype" id="gcp-m-type"></div>
        <div class="mtitle" id="gcp-m-name"></div>
        <div class="mprice" id="gcp-m-price"></div>
      </div>
    </div>
    <div class="gcp-modal-body">
      <h4>Remplissez vos coordonnees pour etre contacte :</h4>
      <div class="gcp-f"><label>Nom complet *</label><input id="gcp-nom" type="text" placeholder="Votre nom et prenom" required></div>
      <div class="gcp-f"><label>Telephone / WhatsApp *</label><input id="gcp-tel" type="tel" placeholder="+212 6XX XXX XXX" required></div>
      <div class="gcp-f"><label>Email (optionnel)</label><input id="gcp-email" type="email" placeholder="votre@email.com"></div>
      <button class="gcp-wa-btn" onclick="gcpSendWA()">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
        Envoyer via WhatsApp
      </button>
    </div>
  </div>
</div>"""

def make_js(page_type):
    props_json  = json.dumps(PROPERTIES, ensure_ascii=False)
    price_key   = 'prix_achat' if page_type == 'achat' else 'prix_location'
    sel_city    = 'item_meta[290]'  if page_type == 'achat' else 'item_meta[565]'
    sel_type    = 'item_meta[291]'  if page_type == 'achat' else 'item_meta[566]'
    sel_pieces  = 'item_meta[569]'  if page_type == 'achat' else 'item_meta[570]'

    return f"""<script>
(function(){{
  var PROPS   = {props_json};
  var ACTIVE  = {json.dumps(ACTIVE_CITIES, ensure_ascii=False)};
  var PRICE   = '{price_key}';
  var WA      = '{WHATSAPP}';
  var PAGE    = '{page_type}';
  var S_CITY  = 'select[name="{sel_city}"]';
  var S_TYPE  = 'select[name="{sel_type}"]';
  var S_PIEC  = 'select[name="{sel_pieces}"]';
  var curProp = null;

  function getVal(s){{ var e=document.querySelector(s); return e?e.value:''; }}

  function matchPieces(pp, sel){{
    if(!sel||sel===''||sel.includes('Indiff')) return true;
    if(sel.includes('+')) return pp>=7;
    var n=parseInt(sel); return isNaN(n)||pp===n;
  }}

  function makeCard(p){{
    var price = p[PRICE]!=='N/A' ? '<div class="gcp-prop-price">'+p[PRICE]+'</div>' : '';
    var pcs   = p.pieces>0 ? p.pieces+' pièce'+(p.pieces>1?'s':'') : 'Terrain';
    var data  = encodeURIComponent(JSON.stringify(p));
    return '<div class="gcp-prop-card" onclick="gcpOpenModal(decodeURIComponent(\''+data+'\'))">'
      +'<img src="'+p.img+'" alt="'+p.titre+'" loading="lazy">'
      +'<div class="gcp-prop-body">'
      +'<span class="gcp-prop-badge">'+p.type+'</span>'
      +'<div class="gcp-prop-title">'+p.titre+'</div>'
      +'<div class="gcp-prop-meta">'+p.surface+' m² &middot; '+pcs+' &middot; '+p.quartier+'</div>'
      +price
      +'<button class="gcp-prop-btn">Je suis interesse(e)</button>'
      +'</div></div>';
  }}

  function renderAll(){{
    var area = document.getElementById('gcp-results-area');
    var html = '';
    ACTIVE.forEach(function(city){{
      var props = PROPS[city]||[];
      if(!props.length) return;
      html += '<div class="gcp-city-section">'
        +'<div class="gcp-city-label"><h3>'+city+'</h3><span>'+props.length+' bien'+(props.length>1?'s':'')+' disponible'+(props.length>1?'s':'')+'</span></div>'
        +'<div class="gcp-results-grid">'+props.map(makeCard).join('')+'</div>'
        +'</div>';
    }});
    area.innerHTML = html;
    area.style.display='block';
  }}

  function renderFiltered(city, type, pieces){{
    var area = document.getElementById('gcp-results-area');
    if(!city){{ renderAll(); return; }}
    if(ACTIVE.indexOf(city)===-1){{
      area.innerHTML='<div class="gcp-coming-soon"><div class="cs-emoji">&#x1F3D7;</div><h3>'+city+' &mdash; Bientot disponible !</h3><p>Nos equipes travaillent a referencer les meilleurs biens de cette ville. Revenez bientot !</p><button class="gcp-notify-btn" onclick="gcpNotify(\''+city+'\')">Me notifier quand disponible</button></div>';
      area.style.display='block';
      area.scrollIntoView({{behavior:'smooth',block:'start'}});
      return;
    }}
    var filtered=(PROPS[city]||[]).filter(function(p){{
      return (!type||p.type===type) && matchPieces(p.pieces,pieces);
    }});
    if(!filtered.length){{
      area.innerHTML='<div class="gcp-no-results"><h3>Aucun bien disponible</h3><p>Aucun resultat pour ces criteres a '+city+'. Essayez d\'autres filtres.</p></div>';
    }} else {{
      area.innerHTML='<div class="gcp-city-section">'
        +'<div class="gcp-city-label"><h3>'+city+'</h3><span>'+filtered.length+' resultat'+(filtered.length>1?'s':'')+'</span></div>'
        +'<div class="gcp-results-grid">'+filtered.map(makeCard).join('')+'</div>'
        +'</div>';
    }}
    area.style.display='block';
    area.scrollIntoView({{behavior:'smooth',block:'start'}});
  }}

  window.gcpOpenModal = function(jsonStr){{
    var p=JSON.parse(jsonStr); curProp=p;
    document.getElementById('gcp-m-sub').textContent   = p.quartier+' \u00b7 '+p.surface+' m\u00b2';
    document.getElementById('gcp-m-type').textContent  = p.type;
    document.getElementById('gcp-m-name').textContent  = p.titre;
    document.getElementById('gcp-m-price').textContent = p[PRICE];
    document.getElementById('gcp-m-img').src           = p.img;
    document.getElementById('gcp-nom').value='';
    document.getElementById('gcp-tel').value='';
    document.getElementById('gcp-email').value='';
    document.getElementById('gcp-overlay').classList.add('open');
    document.body.style.overflow='hidden';
  }};

  window.gcpCloseModal = function(){{
    document.getElementById('gcp-overlay').classList.remove('open');
    document.body.style.overflow='';
  }};

  window.gcpSendWA = function(){{
    var nom=document.getElementById('gcp-nom').value.trim();
    var tel=document.getElementById('gcp-tel').value.trim();
    var email=document.getElementById('gcp-email').value.trim();
    if(!nom||!tel){{alert('Merci de remplir votre nom et votre telephone.'); return;}}
    var p=curProp;
    var lbl=PAGE==='achat'?'Achat':'Location';
    
    var msg='\u2302 Demande de '+lbl+' - GCP Syndic\\n\\n'
      +'📍 Bien : '+p.titre+'\\n'
      +'🏷️ Type : '+p.type+'\\n'
      +'📐 Surface : '+p.surface+' m\u00b2\\n'
      +'📌 Quartier : '+p.quartier+'\\n'
      +'💰 Prix : '+p[PRICE]+'\\n\\n'
      +'👤 Nom : '+nom+'\\n'
      +'📞 Telephone : '+tel
      +(email?'\\n📧 Email : '+email:'');
    window.open('https://wa.me/'+WA+'?text='+encodeURIComponent(msg),'_blank');
    gcpCloseModal();
  }};

  window.gcpNotify = function(city){{
    var nom=prompt('Votre nom ?'); if(!nom) return;
    var tel=prompt('Votre numero WhatsApp ?'); if(!tel) return;
    var msg='🔔 Notification disponibilite GCP Syndic\\n\\nBonjour, je souhaite etre informe(e) pour '+city+'.\\n\\n👤 Nom : '+nom+'\\n📞 Tel : '+tel;
    window.open('https://wa.me/'+WA+'?text='+encodeURIComponent(msg),'_blank');
  }};

  document.getElementById('gcp-overlay').addEventListener('click',function(e){{
    if(e.target===this) gcpCloseModal();
  }});

  document.addEventListener('DOMContentLoaded',function(){{
    // 1. Hide the Nouvelle recherche section (id="tr1") + its sibling form
    var tr1 = document.getElementById('tr1');
    if(tr1){{
      var col = tr1.closest('.fusion-layout-column');
      if(col) col.style.display='none';
      // Hide the next form container sibling
      var next = col ? col.nextElementSibling : null;
      while(next){{
        if(next.querySelector('#form_accueil-acheter,#form_accueil-louer,[id^="frm_form_21"],[id^="frm_form_22"]')){{
          next.style.display='none'; break;
        }}
        next = next.nextElementSibling;
      }}
    }}

    // 2. Move #gcp-results-area to appear RIGHT AFTER the main content wrapper
    //    (before footer). We insert it after #z_autres_annonces or its parent.
    var area    = document.getElementById('gcp-results-area');
    var anchor  = document.getElementById('z_autres_annonces');
    if(anchor && area){{
      // Walk up to the top fusion-layout-column wrapper
      var wrapper = anchor.closest('.fusion-layout-column');
      if(wrapper && wrapper.parentNode){{
        wrapper.parentNode.insertBefore(area, wrapper.nextSibling);
      }}
      anchor.style.display='none';
    }}

    // 3. Intercept only the FIRST Valider button
    var firstBtn = document.querySelector('.frm_button_submit');
    if(firstBtn){{
      firstBtn.addEventListener('click', function(e){{
        e.preventDefault(); e.stopPropagation();
        renderFiltered(getVal(S_CITY), getVal(S_TYPE), getVal(S_PIEC));
      }});
    }}

    // 4. Show all on load
    renderAll();
  }});
}})();
</script>"""

# ─── INJECT INTO BOTH FILES ──────────────────────────────────────────────────
def inject(filepath, page_type):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove any previously injected gcp-filter blocks to avoid duplication
    content = re.sub(r'<style id="gcp-filter-style">.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div id="gcp-results-area"[^>]*>.*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="gcp-overlay".*?</div>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script>\s*\(function\(\)\{.*?\}\)\(\);\s*</script>', '', content, flags=re.DOTALL)

    # Inject before </body>
    inject_block = CSS + MODAL_HTML + make_js(page_type)
    content = content.replace('</body>', inject_block + '\n</body>', 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated: {filepath}")

inject('public/nos-biens-achat.html', 'achat')
inject('public/nos-biens-location.html', 'location')
print("Done!")
