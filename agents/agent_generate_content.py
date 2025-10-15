import json, os
from agent_openai_helper import call_openai
prompts = json.load(open("agents/prompts.json","r",encoding="utf-8"))
# Français
out_fr = call_openai(prompts["prompt_site_fr"], system=prompts["system_fr"])
with open("agents/results/contenu_fr.json","w",encoding="utf-8") as f:
    f.write(out_fr)
print("✅ contenu FR généré -> agents/results/contenu_fr.json")
# English
out_en = call_openai(prompts["prompt_site_en"], system=prompts["system_en"])
with open("agents/results/contenu_en.json","w",encoding="utf-8") as f:
    f.write(out_en)
print("✅ content EN generated -> agents/results/contenu_en.json")
