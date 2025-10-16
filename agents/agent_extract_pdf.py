# ============================================
# Agent d'extraction de contenu PDF → JSON
# ============================================
import pdfplumber
import json, os, re

def extraire_pdf(pdf_path, output_json):
    print(f"📄 Extraction du texte depuis {pdf_path} ...")
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    # Nettoyage du texte
    text = re.sub(r"\n+", "\n", text.strip())
    text = text.replace("•", "- ").replace("–", "-")

    # Structure simple : détection des sections par titres
    sections = {}
    current = "Introduction"
    for line in text.split("\n"):
        if re.match(r"^[A-Z].{2,}$", line.strip()) and len(line.strip()) < 80:
            current = line.strip()
            sections[current] = ""
        else:
            sections[current] += line.strip() + " "

    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(sections, f, ensure_ascii=False, indent=2)

    print(f"✅ Extraction terminée : {output_json}")

if __name__ == "__main__":
    extraire_pdf("Hot-Prod.pdf", "agents/results/pdf_content.json")
