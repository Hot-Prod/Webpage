# ============================================
# Helper IA HuggingFace - version ultra légère
# ============================================
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# 💡 modèle très léger (~1.1B paramètres)
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

def call_hf(prompt, system=None, max_tokens=400):
    """
    Génère du texte à partir d'un prompt via TinyLlama (CPU only, rapide)
    """
    if system:
        full_prompt = f"{system}\n\nUtilisateur :\n{prompt}"
    else:
        full_prompt = prompt

    print("⏳ Génération du texte avec modèle TinyLlama...")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        dtype=torch.float32,  # CPU uniquement
    )

    inputs = tokenizer(full_prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        temperature=0.7,
        do_sample=True,
    )

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("✅ Génération terminée.")
    return result
