#!/bin/bash
echo "🔄 Passage des agents vers Mistral (HuggingFace)..."
pip uninstall -y openai >/dev/null 2>&1
pip install transformers torch sentencepiece >/dev/null 2>&1

# agent_openai_helper devient agent_hf_helper.py
cat > agents/agent_hf_helper.py <<'PY'
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch, json

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"

def call_hf(prompt, system=None, max_tokens=800):
    if system:
        full_prompt = f"{system}\n\nUtilisateur:\n{prompt}"
    else:
        full_prompt = prompt
    print("⏳ Génération du texte avec modèle HuggingFace Mistral...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16, device_map="auto")
    inputs = tokenizer(full_prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=max_tokens, temperature=0.6)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("✅ Génération terminée.")
    return result
PY

# Mise à jour du script agent_generate_content pour utiliser HuggingFace
cat > agents/agent_generate_content.py <<'PY'
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
PY

# Workflow GitHub modifié pour HuggingFace
cat > .github/workflows/agents_run.yml <<'YML'
name: Agents HotProd - run (HuggingFace)
on:
  workflow_dispatch:
jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Installer dépendances
        run: |
          pip install transformers torch sentencepiece beautifulsoup4
      - name: Générer contenu & pages
        run: |
          python agents/agent_generate_content.py
          python agents/agent_build_html.py
          python agents/agent_index_root.py
          python agents/agent_qa.py
      - name: Upload pages générées
        uses: actions/upload-artifact@v4
        with:
          name: generated-pages
          path: |
            fr/index.html
            en/index.html
            agents/results/contenu_fr.json
            agents/results/contenu_en.json
YML

echo "✅ Migration vers Mistral (HuggingFace) terminée."
echo "➡️ Tu peux maintenant exécuter :"
echo "   bash agents/setup_hf.sh (déjà fait)"
echo "   python agents/agent_run_all.py"
echo "   ou lancer le workflow GitHub 'Agents HotProd - run (HuggingFace)'"
