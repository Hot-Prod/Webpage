import json

with open("agents/contenu.json", "r", encoding="utf-8") as f:
    contenu = json.load(f)

html = f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"/><titre>{contenu["accueil"]["titre"]}</titre></head>
<body><h1>{contenu["accueil"]["titre"]}</h1><p>{contenu["accueil"]["sous_titre"]}</p></body></html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ index.html généré à partir du contenu JSON.")

