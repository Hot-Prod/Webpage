# Orchestrator: génère contenu -> pages -> QA -> commit
import os
print("1) Générer contenu via OpenAI (2 langues)...")
os.system("python agents/agent_generate_content.py")
print("2) Construire pages HTML...")
os.system("python agents/agent_build_html.py")
print("3) Générer index racine...")
os.system("python agents/agent_index_root.py")
print("4) QA...")
os.system("python agents/agent_qa.py")
print("5) Commit/Push (optionnel)...")
print("Exécute: python agents/agent_deploy.py pour push si tout OK.")
