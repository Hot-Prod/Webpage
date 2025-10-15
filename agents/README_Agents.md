# Agents HotProd - mode automatisé (Codespaces / GitHub Actions)

Workflow:
1. Configurer secret GitHub: OPENAI_API_KEY (ou exporter la variable en local).
2. Dans Codespaces: run -> python agents/agent_run_all.py
3. Le script génère:
   - agents/results/contenu_fr.json
   - agents/results/contenu_en.json
   - fr/index.html
   - en/index.html
   - index.html (page d'accueil avec choix langue)
4. Vérifier logs, puis commit/push si ok.
