"""
Master brand injection script for GCP Syndic.
Replaces the Avada header + footer in all 12 static HTML pages
with a clean, unified brand nav/footer bar consistent with the Next.js app.
"""

import os, re, glob

public_dir = 'public'
html_files = glob.glob(os.path.join(public_dir, '*.html'))

# ────────────────────────────────────────────────────────────
# 1. UNIFIED HEADER HTML (injected after <body ...>)
# ────────────────────────────────────────────────────────────
BRAND_HEADER = r"""
<style>
/* ── Hide original Avada header and footer ── */
#wrapper .fusion-header-wrapper,
.fusion-header-wrapper,
.fusion-header,
.fusion-sticky-header-wrapper,
.fusion-secondary-header,
.fusion-header-sticky-height,
.fusion-sliding-bar-area,
.fusion-tb-header,
/* Hide original Avada footer */
.fusion-footer,
.fusion-footer-widget-area,
.fusion-footer-copyright-area,
.fusion-tb-footer,
/* Hide any remaining nav bars that duplicate ours */
#nav,
.awb-sticky-header-wrapper {
    display: none !important;
}
/* Ensure body has no extra top-padding from old sticky header */
#wrapper, #main { margin-top: 0 !important; padding-top: 0 !important; }
</style>

<style>
/* ── GCP Syndic Unified Header Styles ── */
.gcp-header{position:sticky;top:0;z-index:9999;font-family:'Poppins','Segoe UI',sans-serif;background:#fff;box-shadow:0 2px 16px rgba(10,38,49,.09);transition:box-shadow .3s}

.gcp-main-nav{max-width:1380px;margin:0 auto;padding:0 24px;display:flex;align-items:center;justify-content:space-between;height:100px}
.gcp-logo img{height:80px;width:auto;object-fit:contain;display:block}
.gcp-nav-links{display:flex;align-items:center;height:100px;gap:4px}
.gcp-nav-links a,.gcp-nav-links button{display:flex;align-items:center;gap:5px;height:100%;padding:0 18px;color:#0a2631;font-size:13px;font-weight:600;letter-spacing:.04em;text-decoration:none;border:none;background:transparent;cursor:pointer;border-bottom:2px solid transparent;transition:color .2s,border-color .2s;white-space:nowrap}
.gcp-nav-links a:hover,.gcp-nav-links button:hover{color:#317bff;border-bottom-color:#317bff}
.gcp-nav-links a.gcp-cta{background:#317bff!important;color:#ffffff!important;-webkit-text-fill-color:#ffffff!important;border:none;padding:10px 24px;height:auto;font-size:11px!important;text-transform:uppercase;letter-spacing:.1em;font-weight:700!important;margin-left:12px;transition:background .2s,box-shadow .2s;text-indent:0!important;line-height:normal!important;opacity:1!important;visibility:visible!important;display:inline-block!important}
.gcp-nav-links a.gcp-cta:hover{background:#1a56cc;box-shadow:0 4px 16px rgba(49,123,255,.3)}
.gcp-dropdown{position:relative;height:100px;display:flex;align-items:center}
.gcp-dropdown-panel{display:none;position:absolute;top:100%;left:50%;transform:translateX(-50%);background:#fff;border-top:2px solid #317bff;box-shadow:0 12px 40px rgba(10,38,49,.15);z-index:10000;min-width:200px}
.gcp-dropdown:hover .gcp-dropdown-panel,.gcp-dropdown-panel:hover{display:block}
.gcp-dropdown-panel a{display:flex;align-items:center;gap:10px;padding:13px 20px;color:#0a2631;font-size:13px;font-weight:600;text-decoration:none;white-space:nowrap;transition:background .15s,color .15s;border-bottom:1px solid #f0f4f8}
.gcp-dropdown-panel a:last-child{border-bottom:none}
.gcp-dropdown-panel a:hover{background:#f5f7fa;color:#317bff}
.gcp-mega-panel{display:none;position:absolute;top:100%;left:50%;transform:translateX(-50%);background:#fff;border-top:2px solid #317bff;box-shadow:0 12px 40px rgba(10,38,49,.15);z-index:10000;width:820px;max-width:90vw}
.gcp-dropdown:hover .gcp-mega-panel,.gcp-mega-panel:hover{display:block}
.gcp-mega-grid{display:grid;grid-template-columns:repeat(5,1fr);border-bottom:1px solid #f0f4f8}
.gcp-mega-item{display:flex;flex-direction:column;align-items:center;text-align:center;padding:16px 12px;text-decoration:none;color:#0a2631;border-right:1px solid #f0f4f8;font-size:12px;font-weight:600;transition:background .15s,color .15s}
.gcp-mega-item:last-child{border-right:none}
.gcp-mega-item img{width:100%;aspect-ratio:4/3;object-fit:cover;margin-bottom:10px;transition:transform .4s}
.gcp-mega-item:hover{background:#f5f7fa;color:#317bff}
.gcp-mega-item:hover img{transform:scale(1.04)}
.gcp-mega-item small{display:block;color:#999;font-size:10px;font-weight:400;margin-top:3px}
.gcp-mega-footer{padding:10px 16px;background:#f9fafb;font-size:11px}
.gcp-mega-footer a{color:#317bff;text-decoration:none;font-weight:600}
.gcp-chevron{width:12px;height:12px;transition:transform .2s}
.gcp-dropdown:hover .gcp-chevron{transform:rotate(180deg)}
/* Mobile */
.gcp-hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:8px;background:transparent;border:none}
.gcp-hamburger span{display:block;width:22px;height:2px;background:#0a2631;border-radius:2px;transition:all .3s}
.gcp-mobile-menu{display:none;background:#fff;border-top:1px solid #f0f4f8;padding:0 24px 20px}
.gcp-mobile-menu.open{display:block}
.gcp-mobile-menu a,.gcp-mobile-menu button{display:block;width:100%;padding:14px 0;color:#0a2631;font-size:14px;font-weight:600;text-decoration:none;border-bottom:1px solid #f0f4f8;background:transparent;border-left:none;border-right:none;border-top:none;cursor:pointer;text-align:left}
.gcp-mobile-menu a:hover,.gcp-mobile-menu button:hover{color:#317bff}
.gcp-mobile-sub{display:none;padding:4px 0 8px 16px}
.gcp-mobile-sub.open{display:block}
.gcp-mobile-sub a{padding:9px 0;font-size:13px;font-weight:500;color:#555;border-bottom:none}
.gcp-mobile-cta{display:block!important;margin-top:16px;background:#317bff!important;color:#ffffff!important;-webkit-text-fill-color:#ffffff!important;text-align:center!important;padding:14px 0!important;font-size:12px!important;text-transform:uppercase;letter-spacing:.1em;font-weight:700!important;border:none!important;text-indent:0!important;line-height:normal!important;opacity:1!important;visibility:visible!important}
@media(max-width:1024px){.gcp-nav-links{display:none}.gcp-hamburger{display:flex}}
</style>

<header class="gcp-header" id="gcp-header">

  <!-- Main nav -->
  <div class="gcp-main-nav">
    <a href="/atrium.html" class="gcp-logo">
      <img src="/logo-transparent.png" alt="GCP Syndic" style="height:80px;width:auto;object-fit:contain;" />
    </a>
    <nav class="gcp-nav-links" aria-label="Navigation principale">
      <a href="/notre-maison.html">Notre maison</a>

      <!-- Nos métiers mega dropdown -->
      <div class="gcp-dropdown">
        <a href="/nos-metiers.html">
          Nos métiers
          <svg class="gcp-chevron" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7"/></svg>
        </a>
          <div class="gcp-mega-panel">
            <div class="gcp-mega-grid">
              <a href="/nos-metiers-syndic.html" class="gcp-mega-item">
                <img src="https://images.unsplash.com/photo-1486325212027-8081e485255e?w=300&q=75&auto=format&fit=crop" alt="Syndic" loading="lazy"/>
                Syndic de copropriété
                <small>L'expertise GCP Syndic</small>
              </a>
              <a href="/nos-metiers-location.html" class="gcp-mega-item">
                <img src="https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=300&q=75&auto=format&fit=crop" alt="Location" loading="lazy"/>
                Location
                <small>Louer en toute quiétude</small>
              </a>
              <a href="/nos-metiers-gestion-locative.html" class="gcp-mega-item">
                <img src="https://images.unsplash.com/photo-1554995207-c18c203602cb?w=300&q=75&auto=format&fit=crop" alt="Gestion" loading="lazy"/>
                Gestion locative
                <small>Gérer votre bien</small>
              </a>
              <a href="/nos-metiers-assurances.html" class="gcp-mega-item">
                <img src="https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=300&q=75&auto=format&fit=crop" alt="Assurances" loading="lazy"/>
                Assurances
                <small>Nos solutions sécurité</small>
              </a>
              <a href="/nos-metiers-vente.html" class="gcp-mega-item">
                <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=300&q=75&auto=format&fit=crop" alt="Vente" loading="lazy"/>
                Vente
                <small>Accompagnement sur-mesure</small>
              </a>
            </div>
            <div class="gcp-mega-footer"><a href="/nos-metiers.html">Voir tous nos métiers →</a></div>
          </div>
        </div>

        <!-- Nos biens dropdown -->
        <div class="gcp-dropdown">
          <button>
            Nos biens
            <svg class="gcp-chevron" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="gcp-dropdown-panel">
            <a href="/nos-biens-achat.html">🏠 Acheter</a>
            <a href="/nos-biens-location.html">🔑 Louer</a>
          </div>
        </div>

        <a href="/nous-rejoindre.html">Nous rejoindre</a>
        <a href="/contact.html" class="gcp-cta">Contact</a>
      </nav>

      <!-- Hamburger -->
      <button class="gcp-hamburger" aria-label="Menu" onclick="toggleMobileMenu(this)">
      <span></span><span></span><span></span>
    </button>
  </div>

  <!-- Mobile menu -->
  <div class="gcp-mobile-menu" id="gcp-mobile-menu">
    <a href="/notre-maison.html">Notre maison</a>
    <button onclick="this.nextElementSibling.classList.toggle('open')">Nos métiers ▾</button>
    <div class="gcp-mobile-sub">
      <a href="/nos-metiers-syndic.html">Syndic de copropriété</a>
      <a href="/nos-metiers-location.html">Location</a>
      <a href="/nos-metiers-gestion-locative.html">Gestion locative</a>
      <a href="/nos-metiers-assurances.html">Assurances</a>
      <a href="/nos-metiers-vente.html">Vente</a>
    </div>
    <button onclick="this.nextElementSibling.classList.toggle('open')">Nos biens ▾</button>
    <div class="gcp-mobile-sub">
      <a href="/nos-biens-achat.html">Acheter</a>
      <a href="/nos-biens-location.html">Louer</a>
    </div>
    <a href="/nous-rejoindre.html">Nous rejoindre</a>
    <a href="/contact.html" class="gcp-mobile-cta">Contact</a>
  </div>
</header>
<script>
function toggleMobileMenu(btn){
  var m=document.getElementById('gcp-mobile-menu');
  m.classList.toggle('open');
  var spans=btn.querySelectorAll('span');
  if(m.classList.contains('open')){
    spans[0].style.transform='rotate(45deg) translate(5px,5px)';
    spans[1].style.opacity='0';
    spans[2].style.transform='rotate(-45deg) translate(5px,-5px)';
  } else {
    spans[0].style.transform='';spans[1].style.opacity='';spans[2].style.transform='';
  }
}
</script>
"""

# ────────────────────────────────────────────────────────────
# 2. UNIFIED FOOTER HTML (injected before </body>)
# ────────────────────────────────────────────────────────────
BRAND_FOOTER = r"""
<style>
/* ── GCP Syndic Unified Footer Styles ── */
.gcp-footer{background:#0a2631;color:#fff;font-family:'Poppins','Segoe UI',sans-serif}

.gcp-footer-main{max-width:1380px;margin:0 auto;padding:56px 24px;display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:40px}
@media(max-width:1024px){.gcp-footer-main{grid-template-columns:1fr 1fr;gap:32px}}
@media(max-width:640px){.gcp-footer-main{grid-template-columns:1fr;gap:28px}}
.gcp-footer-logo img{height:52px;width:auto;object-fit:contain;filter:brightness(0) invert(1);margin-bottom:20px}
.gcp-footer-tagline{color:rgba(255,255,255,.5);font-size:13px;line-height:1.7;margin-bottom:20px}
.gcp-footer-social{display:flex;gap:10px}
.gcp-footer-social a{width:36px;height:36px;border-radius:50%;border:1px solid rgba(255,255,255,.2);display:flex;align-items:center;justify-content:center;color:#fff;text-decoration:none;transition:border-color .2s,background .2s;font-size:13px}
.gcp-footer-social a:hover{border-color:#317bff;background:#317bff}
.gcp-footer-col h4{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.15em;color:#fff;margin-bottom:20px;padding-bottom:12px;border-bottom:1px solid rgba(255,255,255,.1)}
.gcp-footer-col ul{list-style:none;padding:0;margin:0}
.gcp-footer-col ul li{margin-bottom:10px}
.gcp-footer-col ul li a{color:rgba(255,255,255,.55);font-size:13px;text-decoration:none;display:flex;align-items:center;gap:8px;transition:color .2s}
.gcp-footer-col ul li a::before{content:'';width:6px;height:6px;border-radius:50%;background:#317bff;flex-shrink:0;transition:transform .2s}
.gcp-footer-col ul li a:hover{color:#317bff}
.gcp-footer-col ul li a:hover::before{transform:scale(1.4)}
.gcp-footer-contact{display:flex;flex-direction:column;gap:12px}
.gcp-footer-contact-item{display:flex;align-items:flex-start;gap:10px;color:rgba(255,255,255,.55);font-size:13px}
.gcp-footer-contact-item svg{flex-shrink:0;color:#317bff;margin-top:2px}
.gcp-footer-contact-item a{color:rgba(255,255,255,.55);text-decoration:none;transition:color .2s}
.gcp-footer-contact-item a:hover{color:#317bff}
.gcp-footer-cta{display:inline-block!important;background:#317bff!important;color:#ffffff!important;-webkit-text-fill-color:#ffffff!important;text-decoration:none!important;font-size:11px!important;font-weight:700!important;text-transform:uppercase;letter-spacing:.12em;padding:12px 24px;margin-top:20px;transition:background .2s,box-shadow .2s;text-indent:0!important;line-height:normal!important;opacity:1!important;visibility:visible!important}
.gcp-footer-cta:hover{background:#1a56cc;box-shadow:0 4px 16px rgba(49,123,255,.35)}
.gcp-footer-bottom{border-top:1px solid rgba(255,255,255,.1);padding:18px 24px;max-width:1380px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;font-size:11px;color:rgba(255,255,255,.35)}
.gcp-footer-bottom a{color:rgba(255,255,255,.35);text-decoration:none;transition:color .2s}
.gcp-footer-bottom a:hover{color:#317bff}
.gcp-footer-bottom-links{display:flex;gap:20px}
</style>

<footer class="gcp-footer" id="gcp-footer">

  <!-- Main footer -->
  <div class="gcp-footer-main">
    <!-- Col 1: Logo -->
    <div>
      <div class="gcp-footer-logo">
        <img src="/logo-transparent.png" alt="GCP Syndic" />
      </div>
      <p class="gcp-footer-tagline">La gestion de la confiance.<br/>Votre partenaire immobilier de proximité au Maroc.</p>
      <div class="gcp-footer-social">
        <a href="#" aria-label="Facebook"><svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg></a>
        <a href="#" aria-label="LinkedIn"><svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></a>
        <a href="#" aria-label="Instagram"><svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg></a>
      </div>
    </div>

    <!-- Col 2: L'expertise -->
    <div class="gcp-footer-col">
      <h4>L'expertise GCP Syndic</h4>
      <ul>
        <li><a href="/nos-metiers-syndic.html">Syndic de copropriété</a></li>
        <li><a href="/nos-metiers-location.html">Location</a></li>
        <li><a href="/nos-metiers-gestion-locative.html">Gestion locative</a></li>
        <li><a href="/nos-metiers-assurances.html">Assurances</a></li>
        <li><a href="/nos-metiers-vente.html">Vente</a></li>
      </ul>
    </div>

    <!-- Col 3: Liens utiles -->
    <div class="gcp-footer-col">
      <h4>Liens utiles</h4>
      <ul>
        <li><a href="/notre-maison.html">Notre maison</a></li>
        <li><a href="/nos-biens-achat.html">Nos biens à vendre</a></li>
        <li><a href="/nos-biens-location.html">Nos biens en location</a></li>
        <li><a href="/nous-rejoindre.html">Nous rejoindre</a></li>
        <li><a href="/contact.html">Contact</a></li>
      </ul>
    </div>

    <!-- Col 4: Contact -->
    <div class="gcp-footer-col">
      <h4>Nous contacter</h4>
      <div class="gcp-footer-contact">
        <div class="gcp-footer-contact-item">
          <svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
          <a href="tel:+212662081784">+212 6 62 08 17 84</a>
        </div>
        <div class="gcp-footer-contact-item">
          <svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
          <a href="mailto:contact@gcp-syndic.ma">contact@gcp-syndic.ma</a>
        </div>
        <div class="gcp-footer-contact-item">
          <svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          <a href="https://maps.google.com/?q=GCP+Syndic+Meknes" target="_blank" rel="noopener" style="color:inherit;text-decoration:none;">Imm B8, Appt 8, 4ème étage, Belvue, Meknès 50000 →</a>
        </div>
      </div>
      <a href="/contact.html" class="gcp-footer-cta">Nous écrire →</a>
    </div>
  </div>

  <!-- Bottom bar -->
  <div style="border-top:1px solid rgba(255,255,255,.1);">
    <div class="gcp-footer-bottom">
      <p>© 2026 GCP Syndic — La gestion de la confiance. Tous droits réservés.</p>
      <div class="gcp-footer-bottom-links">
        <a href="/mentions-legales.html">Mentions légales</a>
        <a href="/politique-confidentialite.html">Politique de confidentialité</a>
      </div>
    </div>
  </div>
</footer>
"""

# ────────────────────────────────────────────────────────────
# 3. PROCESS EACH HTML FILE
# ────────────────────────────────────────────────────────────

AVADA_HEADER_PATTERNS = [
    # Full header wrapper
    r'<header[^>]*(?:fusion-header|fusion-sticky|awb-sticky)[^>]*>.*?</header>',
    r'<div[^>]*(?:fusion-header-wrapper|fusion-sticky-header-wrapper|awb-sticky-header)[^>]*>.*?</div>',
    # Secondary header bar
    r'<div[^>]*fusion-secondary-header[^>]*>.*?</div>',
]
AVADA_FOOTER_PATTERNS = [
    r'<footer[^>]*(?:fusion-footer|fusion-sliding)[^>]*>.*?</footer>',
    r'<div[^>]*(?:fusion-footer|fusion-sliding-bar|fusion-tb-footer)[^>]*>.*?</div>',
]

stats = {'processed': 0, 'skipped': 0}

for filepath in sorted(html_files):
    fname = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    original = html

    # ── Remove any previously injected GCP header/footer ──
    html = re.sub(r'<!-- GCP BRAND HEADER START -->.*?<!-- GCP BRAND HEADER END -->', '', html, flags=re.DOTALL)
    html = re.sub(r'<!-- GCP BRAND FOOTER START -->.*?<!-- GCP BRAND FOOTER END -->', '', html, flags=re.DOTALL)
    # Also remove inline style+script+header block we may have injected
    html = re.sub(r'<style>\s*/\* ── GCP Syndic Unified Header.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<style>\s*/\* ── GCP Syndic Unified Footer.*?</footer>', '', html, flags=re.DOTALL)

    # ── Fix Moroccan content ──
    # Replace all Paris/France references with Moroccan equivalents
    replacements_text = [
        ('Paris et la région parisienne', 'Meknès et les principales villes du Maroc'),
        ('la région parisienne', 'le Maroc'),
        ('Île-de-France', 'Maroc'),
        ("l'Île-de-France", 'le Maroc'),
        ('en Île-de-France', 'au Maroc'),
        ('Marseille', 'Casablanca'),
        ('France', 'Maroc'),
        ('française', 'marocaine'),
        ('français', 'marocain'),
        ('Paris', 'Meknès'),

        # Clean up leftover "AtriumNews" reference in footer CSS comment
        ("l'AtriumNews", "la Newsletter GCP Syndic"),
        ('AtriumNews', 'GCP Syndic Newsletter'),
        ('Rejoindre l\'AtriumNews', 'S\'inscrire à la Newsletter'),
        # Remove any French legal boilerplate phone numbers
        ('+33', '+212'),
        ('01 ', '+212 5 22 '),
    ]
    for old, new in replacements_text:
        html = html.replace(old, new)

    # ── Add loading=lazy to all below-fold images ──
    # Only images NOT in the first 2000 chars (likely above fold)
    above_fold = html[:2000]
    below_fold = html[2000:]
    below_fold = re.sub(r'(<img\b(?![^>]*loading=)[^>]*)(>)', r'\1 loading="lazy"\2', below_fold)
    html = above_fold + below_fold

    # ── Inject unified header after <body ...> ──
    body_match = re.search(r'(<body[^>]*>)', html, re.IGNORECASE)
    if body_match:
        pos = body_match.end()
        html = (
            html[:pos]
            + '\n<!-- GCP BRAND HEADER START -->'
            + BRAND_HEADER
            + '<!-- GCP BRAND HEADER END -->\n'
            + html[pos:]
        )

    # ── Inject unified footer before </body> ──
    close_body = re.search(r'</body>', html, re.IGNORECASE)
    if close_body:
        pos = close_body.start()
        html = (
            html[:pos]
            + '\n<!-- GCP BRAND FOOTER START -->'
            + BRAND_FOOTER
            + '<!-- GCP BRAND FOOTER END -->\n'
            + html[pos:]
        )

    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        stats['processed'] += 1
        print(f'  OK  {fname}')
    else:
        stats['skipped'] += 1
        print(f'  –  {fname} (no change)')

print(f"\nDone! Processed: {stats['processed']}, Skipped: {stats['skipped']}")
