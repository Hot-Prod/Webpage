# ============================================
# Agent de génération de contenu IA - version robuste
# ============================================
import json, os
from agent_hf_helper import call_hf

# Charger les prompts
with open("agents/prompts.json", "r", encoding="utf-8") as f:
    prompts = json.load(f)

def nettoyer_sortie(raw_text: str) -> str:
    """
    Nettoie la sortie brute du modèle en supprimant les artefacts et formate en JSON.
    """
    text = raw_text.strip()
    if text.startswith("{") and text.endswith("}"):
        return text  # déjà JSON
    # Forcer un format JSON simple
    text = text.replace("\n", " ").replace("**", "").replace("```", "")
    return json.dumps({"texte": text}, ensure_ascii=False, indent=2)

def generer_contenu(langue: str, prompt_cle: str, system_cle: str, sortie_path: str):
    """
    Génére le contenu pour une langue donnée.
    """
    print(f"\n🧠 Génération du contenu ({langue}) via modèle IA...")
    try:
        out = call_hf(prompts[prompt_cle], system=prompts[system_cle])
        contenu = nettoyer_sortie(out)
        os.makedirs(os.path.dirname(sortie_path), exist_ok=True)
        with open(sortie_path, "w", encoding="utf-8") as f:
            f.write(contenu)
        print(f"✅ Contenu {langue.upper()} sauvegardé -> {sortie_path}")
    except Exception as e:
        print(f"❌ Erreur de génération {langue}: {e}")

# Génération FR et EN
generer_contenu("fr", "prompt_site_fr", "system_fr", "agents/results/contenu_fr.json")
generer_contenu("en", "prompt_site_en", "system_en", "agents/results/contenu_en.json")
