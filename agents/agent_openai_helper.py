# Helper pour appeler l'API OpenAI (utilise OPENAI_API_KEY env var)
import os, json
def call_openai(prompt, system=None, model="gpt-4o-mini", max_tokens=1000, temperature=0.2):
    key = os.environ.get("OPENAI_API_KEY","")
    if not key:
        raise RuntimeError("OPENAI_API_KEY non défini. Exporte la clé ou configure GitHub Secret.")
    try:
        import openai
    except Exception as e:
        raise RuntimeError("Lib openai manquante. Installer pip install openai") from e
    openai.api_key = key
    messages=[]
    if system:
        messages.append({"role":"system","content":system})
    messages.append({"role":"user","content":prompt})
    resp = openai.ChatCompletion.create(model=model, messages=messages, max_tokens=max_tokens, temperature=temperature)
    return resp["choices"][0]["message"]["content"]
