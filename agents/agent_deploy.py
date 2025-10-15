import os
# commit generated pages and push
os.system("git add fr/index.html en/index.html index.html")
os.system('git commit -m "Auto: generate fr/en pages from agents" || echo "no changes to commit"')
os.system("git push origin main")
print("✅ commit/push done (si changements).")
