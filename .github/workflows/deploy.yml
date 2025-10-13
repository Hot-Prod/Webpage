#!/bin/bash
set -e
REPO_SSH="git@github.com:TON_USER/Hot-Prod.Webpage.git" # remplace par ton repo
mkdir -p hotprod-site
cp index.html CV_Laurent_Garnier_FR.pdf README.md hotprod-site/
cd hotprod-site
git init
git checkout -b main
git add .
git commit -m "Initial site HotProd - Laurent Garnier"
git remote add origin $REPO_SSH
git push -u origin main
echo "Fait. Ensuite: GitHub > Settings > Pages > Branch: main > / (root) > Save"
