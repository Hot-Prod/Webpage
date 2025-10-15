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
