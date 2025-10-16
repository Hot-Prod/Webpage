# ============================================
# 🚀 Pipeline complet HotProd : PDF → Site bilingue
# ============================================
import os
import sys

commandes = [
    "python agents/agent_extract_pdf.py",       # Extraction du contenu depuis Hot-Prod.pdf
    "python agents/agent_generate_content.py",  # Génération IA FR/EN
    "python agents/agent_build_html.py",        # Construction des pages HTML
    "python agents/agent_index_root.py",        # Génération de l’index racine
    "python agents/agent_qa.py",                # Contrôle qualité du site
    "python agents/agent_deploy.py",            # Publication sur GitHub Pages
]

print("============================================")
print("🧠  Lancement du pipeline complet HotProd")
print("============================================")

for cmd in commandes:
    print(f"\n🚀 Exécution : {cmd}")
    result = os.system(cmd)
    if result != 0:
        print(f"⚠️  Erreur détectée dans : {cmd}")
        sys.exit(1)
    else:
        print(f"✅  Étape réussie : {cmd}")

print("\n🎯 Pipeline terminé avec succès !")
print("Le site est prêt et déployé sur GitHub Pages.")
