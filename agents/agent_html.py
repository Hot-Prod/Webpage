import openai, json

openai.api_key = "TA_CLE_API"

with open("agents/contenu.json", "r", encoding="utf-8") as f:
    contenu = f.read()

prompt = f"""
Convertis ce contenu JSON en fichier HTML complet (lang=fr), avec sections :
Accueil, Services, À propos, Témoignages, Contact.
Utilise Tailwind CDN. 
{contenu}
"""

response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

html = response["choices"][0]["message"]["content"]
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ index.html mis à jour automatiquement.")
