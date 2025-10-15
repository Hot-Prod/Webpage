# ============================================
# Script complet d'automatisation des agents IA HotProd
# ============================================
import os

commandes = [
    "python agents/agent_generate_content.py",
    "python agents/agent_build_html.py",
    "python agents/agent_index_root.py",
    "python agents/agent_qa.py",
    "python agents/agent_deploy.py",
]

for cmd in commandes:
    print(f"\n🚀 Exécution : {cmd}")
    code = os.system(cmd)
    if code != 0:
        print(f"⚠️ Erreur rencontrée dans : {cmd}")
        break
    else:
        print(f"✅ Étape terminée : {cmd}")
