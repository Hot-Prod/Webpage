import json
from agent_hf_helper import call_hf

prompts = json.load(open("agents/prompts.json", "r", encoding="utf-8"))

print("🧠 Génération du contenu via Mistral (gratuit)...")

out_fr = call_hf(prompts["prompt_site_fr"], system=prompts["system_fr"])
with open("agents/results/contenu_fr.json", "w", encoding="utf-8") as f:
    f.write(out_fr)
print("✅ Contenu FR généré -> agents/results/contenu_fr.json")

out_en = call_hf(prompts["prompt_site_en"], system=prompts["system_en"])
with open("agents/results/contenu_en.json", "w", encoding="utf-8") as f:
    f.write(out_en)
print("✅ Content EN generated -> agents/results/contenu_en.json")
