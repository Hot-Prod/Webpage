# ============================================
# Construction des pages HTML à partir du contenu IA
# ============================================
import json, os

def charger_contenu(path):
    if not os.path.exists(path):
        print(f"⚠️ Fichier manquant : {path}")
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict) and "texte" in data:
                return data["texte"]
            return str(data)
    except Exception as e:
        print(f"❌ Erreur JSON dans {path}: {e}")
        return None

def creer_page(langue, contenu):
    dossier = f"{langue}"
    os.makedirs(dossier, exist_ok=True)
    path = f"{dossier}/index.html"
    html = f"""<!DOCTYPE html>
<html lang="{langue}">
<head>
<meta charset="utf-8">
<title>HotProd - {langue.upper()}</title>
</head>
<body>
<h1>HotProd</h1>
<div>{contenu}</div>
</body>
</html>"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Page {langue}/index.html générée.")

def main():
    contenu_fr = charger_contenu("agents/results/contenu_fr.json")
    contenu_en = charger_contenu("agents/results/contenu_en.json")
    if contenu_fr: creer_page("fr", contenu_fr)
    if contenu_en: creer_page("en", contenu_en)

if __name__ == "__main__":
    main()
