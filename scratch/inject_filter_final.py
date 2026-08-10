from bs4 import BeautifulSoup

# The JS - global function, not wrapped in IIFE
FILTER_JS = """
<script>
var GCP_ACTIVE_CITIES = ["Mekn\u00e8s", "K\u00e9nitra", "Tanger", "Oujda"];

function gcpRunFilter(btn) {
    // Walk up to the closest form to get this form's selects
    var form = btn.closest ? btn.closest('form') : btn.parentElement;
    while (form && form.tagName !== 'FORM') { form = form.parentElement; }

    var cityVal  = form ? (form.querySelector('select[id^="field_y68yj"]') || {}).value || "" : "";
    var typeVal  = form ? (form.querySelector('select[id^="field_um9ky"]') || {}).value || "" : "";
    var roomsVal = form ? (form.querySelector('select[id^="field_qfq1i"]') || {}).value || "" : "";

    cityVal  = cityVal.replace(/\s+/g, ' ').trim();
    typeVal  = typeVal.replace(/\s+/g, ' ').trim();
    roomsVal = roomsVal.replace(/\s+/g, ' ').trim();

    var cards       = document.querySelectorAll('.gcp-property-card');
    var grid        = document.getElementById('gcp-properties-grid');
    var comingSoon  = document.getElementById('gcp-coming-soon');
    var noResults   = document.getElementById('gcp-no-results');

    if (!grid) { return; }

    // Hide banners
    if (comingSoon) comingSoon.style.display = 'none';
    if (noResults)  noResults.style.display  = 'none';
    grid.style.display = '';

    // City not in active list → Coming Soon
    if (cityVal && GCP_ACTIVE_CITIES.indexOf(cityVal) === -1) {
        cards.forEach(function(c) { c.style.display = 'none'; });
        grid.style.display = 'none';
        if (comingSoon) comingSoon.style.display = 'block';
        return;
    }

    // Filter cards
    var visible = 0;
    cards.forEach(function(card) {
        var cardCity  = (card.getAttribute('data-city')  || "").trim();
        var cardType  = (card.getAttribute('data-type')  || "").trim();
        var cardRooms = (card.getAttribute('data-rooms') || "").replace(/\u00a0/g,' ').trim();

        var cityOk  = !cityVal  || cardCity === cityVal;
        var typeOk  = !typeVal  || cardType === typeVal;
        var roomsOk = true;
        if (roomsVal) {
            if (roomsVal === "5+ pi\u00e8ces") {
                var m = cardRooms.match(/(\\d+)/);
                roomsOk = m ? parseInt(m[1]) >= 5 : false;
            } else {
                roomsOk = cardRooms === roomsVal;
            }
        }

        if (cityOk && typeOk && roomsOk) {
            card.style.display = '';
            visible++;
        } else {
            card.style.display = 'none';
        }
    });

    if (visible === 0) {
        grid.style.display = 'none';
        if (noResults) noResults.style.display = 'block';
    }
}
</script>
"""

COMING_SOON_HTML = """<div id="gcp-coming-soon" style="display:none;text-align:center;padding:80px 20px;"><div style="max-width:600px;margin:0 auto;background:linear-gradient(135deg,#f8f9ff,#e8f0fe);border-radius:16px;padding:60px 40px;box-shadow:0 8px 32px rgba(0,80,200,0.1);"><div style="font-size:64px;margin-bottom:24px;">&#128640;</div><h2 style="color:#00205b;font-size:2rem;margin-bottom:16px;">Bient&ocirc;t disponible</h2><p style="color:#555;font-size:1.1rem;line-height:1.7;margin-bottom:32px;">GCP Syndic arrive dans cette ville ! Nous travaillons activement &agrave; l&rsquo;expansion de notre portefeuille immobilier.<br><br>Revenez bient&ocirc;t ou contactez-nous pour &ecirc;tre inform&eacute; en priorit&eacute;.</p><a href="/contact.html" style="display:inline-block;background:#00205b;color:#fff;padding:14px 36px;border-radius:8px;text-decoration:none;font-weight:600;font-size:1rem;">Nous contacter</a></div></div>"""

NO_RESULTS_HTML = """<div id="gcp-no-results" style="display:none;text-align:center;padding:60px 20px;"><div style="max-width:500px;margin:0 auto;"><div style="font-size:48px;margin-bottom:16px;">&#128269;</div><h3 style="color:#00205b;font-size:1.5rem;margin-bottom:12px;">Aucun r&eacute;sultat trouv&eacute;</h3><p style="color:#777;font-size:1rem;">Aucun bien ne correspond &agrave; votre recherche pour le moment.<br>Essayez de modifier vos crit&egrave;res ou revenez bient&ocirc;t.</p></div></div>"""


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # ── 1. Remove old injected JS (if any) ──────────────────────────────────
    for tag in soup.find_all('script'):
        if tag.string and ('gcpRunFilter' in tag.string or 'runFilter' in tag.string or 'GCP_ACTIVE' in tag.string):
            tag.decompose()

    # Remove old banners
    for bid in ['gcp-coming-soon', 'gcp-no-results']:
        old = soup.find(id=bid)
        if old:
            old.decompose()

    # ── 2. Wire up the Valider buttons directly in HTML ──────────────────────
    for btn in soup.find_all('button', class_='frm_button_submit'):
        btn['onclick'] = 'gcpRunFilter(this); return false;'
        btn['type'] = 'button'   # prevent actual form submit

    # ── 3. Mark each property column with data attributes ───────────────────
    for card_type_el in soup.find_all('p', class_='type_bien'):
        lieu_el  = card_type_el.find_next_sibling('p', class_='lieu')
        surf_p   = card_type_el.find_next_sibling('p', class_='surface_nbp')
        nbp_el   = surf_p.find('span', class_='nbp') if surf_p else None

        city  = lieu_el.get_text(strip=True) if lieu_el else ""
        ptype = card_type_el.get_text(strip=True)
        rooms = nbp_el.get_text(strip=True).replace('\xa0', ' ').strip() if nbp_el else ""

        parent_col = card_type_el.find_parent('div', class_='fusion-layout-column')
        if parent_col:
            parent_col['data-city']  = city
            parent_col['data-type']  = ptype
            parent_col['data-rooms'] = rooms
            classes = parent_col.get('class', [])
            if 'gcp-property-card' not in classes:
                classes.append('gcp-property-card')
            parent_col['class'] = classes

    # ── 4. Wrap properties grid with ID ─────────────────────────────────────
    first_card = soup.find('div', class_='gcp-property-card')
    if first_card:
        row = first_card.parent
        if row and row.get('id') != 'gcp-properties-grid':
            row['id'] = 'gcp-properties-grid'

    # ── 5. Insert banners before the grid ───────────────────────────────────
        grid = soup.find(id='gcp-properties-grid')
        if grid:
            cs = BeautifulSoup(COMING_SOON_HTML, 'html.parser')
            nr = BeautifulSoup(NO_RESULTS_HTML, 'html.parser')
            grid.insert_before(cs)
            grid.insert_before(nr)

    # ── 6. Inject global JS before </body> ───────────────────────────────────
    body = soup.find('body')
    if body:
        js = BeautifulSoup(FILTER_JS, 'html.parser')
        body.append(js)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Done: {filepath}")


process_file('public/nos-biens-achat.html')
process_file('public/nos-biens-location.html')
