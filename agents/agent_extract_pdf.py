# agents/agent_extract_pdf.py
import sys
import subprocess
import importlib

def ensure_package(pkg_name, import_name=None):
    import_name = import_name or pkg_name
    try:
        return importlib.import_module(import_name)
    except Exception:
        print(f"➡️ Le module {import_name} est absent. Installation en cours : {pkg_name}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-cache-dir", pkg_name])
        return importlib.import_module(import_name)

# Assurer pdfplumber et ses dépendances
pdfplumber = ensure_package("pdfplumber")
# pdfplumber dépend de pillow et pdfminer.six ; pip install s'en charge en général.

# Maintenant le reste du script
import json, os, re

def extraire_pdf(pdf_path):
    print(f"📄 Extraction du texte depuis {pdf_path} ...")
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    text = re.sub(r"\n+", "\n", text.strip())
    return text

def sauvegarder_json(outpath, obj):
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    with open(outpath, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    print(f"✅ Fichier sauvegardé : {outpath}")

if __name__ == "__main__":
    src_pdf = "Hot-Prod.pdf"
    out_json = "agents/results/pdf_content.json"
    if not os.path.exists(src_pdf):
        print(f"❌ PDF introuvable: {src_pdf}. Place le PDF à la racine du repo.")
        sys.exit(1)
    texte = extraire_pdf(src_pdf)
    # structure simple : mettre tout le texte sous "raw"
    sauvegarder_json(out_json, {"raw": texte})
