#!/bin/bash

# Script de sauvegarde Git pour Codespaces

echo "📦 Sauvegarde du travail en cours..."

# Étape 1 : Vérifie les fichiers modifiés
git status

# Étape 2 : Ajoute tous les fichiers modifiés
git add .

# Étape 3 : Demande un message de commit à l'utilisateur
read -p "📝 Message de commit : " commit_message

# Étape 4 : Crée le commit
git commit -m "$commit_message"

# Étape 5 : Pousse les modifications vers GitHub
git push

echo "✅ Sauvegarde terminée avec succès !"


