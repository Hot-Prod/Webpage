import csv, openai

openai.api_key = "TA_CLE_API"

prompt = """
Crée 3 messages de connexion et 3 messages de relance pour des Directeurs Industrialisation
ou Responsables Production en France. Ton professionnel, concis, orienté résultats.
"""

response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

messages = response["choices"][0]["message"]["content"]
print("💬 Messages LinkedIn générés :\n")
print(messages)

# Sauvegarde dans fichier texte
with open("agents/messages_linkedin.txt", "w", encoding="utf-8") as f:
    f.write(messages)
