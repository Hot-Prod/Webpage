# ============================================
# Helper IA HuggingFace - Version légère (phi-2)
# ============================================
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_NAME = "microsoft/phi-2"

def call_hf(prompt, system=None, max_tokens=800):
    """
    Génère du texte à partir d'un prompt via le modèle Phi-2 (léger, CPU-only)
    Aucun GPU, aucune clé API requise.
    """
    if system:
        full_prompt = f"{system}\n\nUtilisateur :\n{prompt}"
    else:
        full_prompt = prompt

    print("⏳ Génération du texte avec modèle HuggingFace Phi-2...")

    # Chargement du modèle et du tokenizer
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float32,  # CPU uniquement
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
