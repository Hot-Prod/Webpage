# ============================================
# Génération automatique du contenu à partir de pages_content.json
# ============================================
import json, os

source = "agents/results/pages_content.json"

with open(source, "r", encoding="utf-8") as f:
    data = json.load(f)

for langue in ["fr", "en"]:
    for page, content in data[langue].items():
        path = f"agents/results/{page}_{langue}.json"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"texte": content["texte"]}, f, ensure_ascii=False, indent=2)
        print(f"✅ {path} créé.")
