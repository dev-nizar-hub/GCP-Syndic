import re

# ── 1. CITIES (comprehensive Moroccan list) ────────────────────────────────
CITIES = [
    "Meknès", "Fès", "Rabat", "Casablanca", "Marrakech", "Tanger",
    "Agadir", "Kénitra", "Oujda", "El Jadida", "Ifrane", "Mohammedia",
    "Salé", "Témara", "Tétouan", "Béni Mellal", "Settat", "Khémisset",
    "Laâyoune", "Nador", "Taza", "Safi", "Essaouira", "Ouarzazate",
    "Errachidia", "Guelmim", "Al Hoceima", "Berrechid", "Khénifra",
    "Taourirt", "Inzegane", "Larache", "Ksar El Kébir", "Tiznit",
    "Dakhla", "Midelt", "Azrou", "Ifrane", "Séfrou", "Moulay Idriss Zerhoun",
    "Aïn Aouda", "Aïn Harrouda", "Benslimane", "Médiouna", "Mohammédia",
    "Bouznika", "Benguérir", "Youssoufia", "Sidi Kacem", "Sidi Slimane",
    "Souk El Arbaa", "Lqliâa", "Chichaoua", "Taroudant", "Biougra",
]
# Remove duplicates while preserving order
seen = set()
CITIES_DEDUP = []
for c in CITIES:
    if c not in seen:
        seen.add(c)
        CITIES_DEDUP.append(c)

def make_options(items, use_text_as_value=True):
    return ''.join(
        f'<option  value="{v}">{v}</option>'
        for v in items
    )

def make_options_numbered(items):
    """Use text as value (works fine for WhatsApp redirect forms)"""
    return make_options(items)

# ── 2. TYPES DE BIEN ──────────────────────────────────────────────────────
TYPES_ACHAT = [
    "Appartement", "Villa", "Maison", "Studio", "Duplex",
    "Riad", "Terrain", "Ferme", "Local commercial",
]

TYPES_LOCATION = [
    "Appartement", "Villa", "Maison", "Studio", "Duplex",
    "Triplex", "Riad", "Penthouse", "Maison mitoyenne",
    "Ferme", "Terrain", "Bureau", "Local commercial",
]

# ── 3. NOMBRE DE PIÈCES ───────────────────────────────────────────────────
PIECES = [
    "1 pièce", "2 pièces", "3 pièces", "4 pièces",
    "5 pièces", "6 pièces", "7 pièces et +", "Indifférent",
]

EMPTY_OPT = '<option  value="" selected=\'selected\'> </option>'


def replace_select_options(content, select_id, new_options_html):
    """Find select by id and replace all its options (keeps empty first option)."""
    # Match the select tag and all content up to </select>
    pattern = (
        r'(<select[^>]*id="' + re.escape(select_id) + r'"[^>]*>)'
        r'.*?'
        r'(</select>)'
    )
    def replacer(m):
        return m.group(1) + '\n\t\t' + EMPTY_OPT + new_options_html + '\t' + m.group(2)
    new_content, count = re.subn(pattern, replacer, content, flags=re.DOTALL)
    return new_content, count


# ── Apply to nos-biens-achat.html ─────────────────────────────────────────
with open('public/nos-biens-achat.html', 'r', encoding='utf-8') as f:
    achat = f.read()

achat, n1 = replace_select_options(achat, 'field_y68yj', make_options(CITIES_DEDUP))
achat, n2 = replace_select_options(achat, 'field_um9ky', make_options(TYPES_ACHAT))
achat, n3 = replace_select_options(achat, 'field_qfq1i', make_options(PIECES))

with open('public/nos-biens-achat.html', 'w', encoding='utf-8') as f:
    f.write(achat)

print(f"nos-biens-achat.html:")
print(f"  Localisation selects updated : {n1}")
print(f"  Type de bien selects updated : {n2}")
print(f"  Nombre de pièces updated     : {n3}")

# ── Apply to nos-biens-location.html ──────────────────────────────────────
with open('public/nos-biens-location.html', 'r', encoding='utf-8') as f:
    location = f.read()

location, m1 = replace_select_options(location, 'field_y68yjd28fa6c124', make_options(CITIES_DEDUP))
location, m2 = replace_select_options(location, 'field_um9ky312b5b1117', make_options(TYPES_LOCATION))
location, m3 = replace_select_options(location, 'field_71h9w', make_options(PIECES))

with open('public/nos-biens-location.html', 'w', encoding='utf-8') as f:
    f.write(location)

print(f"\nnos-biens-location.html:")
print(f"  Localisation selects updated : {m1}")
print(f"  Type de bien selects updated : {m2}")
print(f"  Nombre de pièces updated     : {m3}")

print("\nDone! All dropdowns updated.")
