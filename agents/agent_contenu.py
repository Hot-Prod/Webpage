import openai, json

openai.api_key = "TA_CLE_API"

prompt = """
Tu es rédacteur expert pour HotProd. Génère le contenu en français du site web :
Accueil (accroche + 3 points clés)
4 services (titre, résumé, 3 bullets)
À propos (expérience, valeurs, vision)
Témoignage client
Retourne au format JSON.
"""

response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

data = response["choices"][0]["message"]["content"]
with open("agents/contenu.json", "w", encoding="utf-8") as f:
    f.write(data)

print("✅ Contenu généré → agents/contenu.json")
