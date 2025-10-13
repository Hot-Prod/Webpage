import json

with open("agents/contenu.json", "r", encoding="utf-8") as f:
    contenu = json.load(f)

html = f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"/><title>{contenu[home][title]}</title></head>
<body><h1>{contenu[home][title]}</h1><p>{contenu[home][subtitle]}</p></body></html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ index.html généré à partir du contenu JSON.")

