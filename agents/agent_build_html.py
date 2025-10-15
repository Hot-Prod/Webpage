# ============================================
# Génération HTML Pro & bilingue HotProd
# ============================================
import json, os

PAGES = [
    ("index", "Accueil", "Home"),
    ("services", "Services", "Services"),
    ("about", "À propos", "About"),
    ("testimonials", "Témoignages", "Testimonials"),
    ("contact", "Contact", "Contact"),
]

def charger_contenu(langue, page):
    path = f"agents/results/{page}_{langue}.json"
    if not os.path.exists(path):
        print(f"⚠️ Fichier manquant : {path}")
        return f"<p>Contenu non disponible pour {page} ({langue}).</p>"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data.get("texte", str(data))

def creer_nav(langue):
    links = []
    for p, fr, en in PAGES:
        label = fr if langue == "fr" else en
        links.append(f'<a href="{p}.html">{label}</a>')
    return " | ".join(links)

def creer_lang_switch(langue):
    if langue == "fr":
        return '<div class="lang-switch"><a href="../en/index.html">🇬🇧 English version</a></div>'
    else:
        return '<div class="lang-switch"><a href="../fr/index.html">🇫🇷 Version française</a></div>'

def creer_page(langue, page, contenu):
    dossier = f"{langue}"
    os.makedirs(dossier, exist_ok=True)
    path = f"{dossier}/{page}.html"

    titre = "HotProd – " + ("Conseil en industrialisation" if langue == "fr" else "Industrial Consulting")
    nav = creer_nav(langue)
    switch = creer_lang_switch(langue)

    html = f"""<!DOCTYPE html>
<html lang="{langue}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre}</title>
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<header>
  <h1>{titre}</h1>
  <nav>{nav}</nav>
  {switch}
</header>
<main>
{contenu}
</main>
<footer>
  <p>© 2025 HotProd — Laurent Garnier</p>
</footer>
</body>
</html>"""

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Page {langue}/{page}.html générée.")

def main():
    for page, _, _ in PAGES:
        for langue in ["fr", "en"]:
            contenu = charger_contenu(langue, page)
            creer_page(langue, page, contenu)

if __name__ == "__main__":
    main()
