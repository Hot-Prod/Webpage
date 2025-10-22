#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HotProd – Optimisation automatique SEO
Ajoute ou met à jour les balises <meta>, <title>, OpenGraph et Twitter Card.
"""

import os
from bs4 import BeautifulSoup

BASE_URL = "https://hot-prod.github.io/Webpage"

def optimize_html(file_path: str):
    """Optimise les balises meta et Open Graph d'un fichier HTML"""
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    # Récupérer ou définir le titre
    title_tag = soup.find("title")
    title = title_tag.text.strip() if title_tag else "HotProd — Industrialisation & Innovation"
    description = f"Découvrez les solutions HotProd : {title.lower()}."

    # Balises META de base
    metas = {
        "description": description,
        "viewport": "width=device-width, initial-scale=1",
        "robots": "index,follow"
    }

    head = soup.head
    if not head:
        return

    # Ajouter ou corriger les balises <meta>
    for key, val in metas.items():
        tag = head.find("meta", attrs={"name": key})
        if tag:
            tag["content"] = val
        else:
            meta = soup.new_tag("meta")
            meta["name"] = key
            meta["content"] = val
            head.append(meta)

    # Open Graph
    og_tags = {
        "og:title": title,
        "og:description": description,
        "og:type": "website",
        "og:url": f"{BASE_URL}/{os.path.relpath(file_path, '.')}",
        "og:image": f"{BASE_URL}/assets/hero-visual.png",
        "og:site_name": "HotProd"
    }

    for key, val in og_tags.items():
        tag = head.find("meta", attrs={"property": key})
        if tag:
            tag["content"] = val
        else:
            meta = soup.new_tag("meta")
            meta["property"] = key
            meta["content"] = val
            head.append(meta)

    # Twitter Cards
    twitter_tags = {
        "twitter:card": "summary_large_image",
        "twitter:title": title,
        "twitter:description": description,
        "twitter:image": f"{BASE_URL}/assets/hero-visual.png"
    }

    for key, val in twitter_tags.items():
        tag = head.find("meta", attrs={"name": key})
        if tag:
            tag["content"] = val
        else:
            meta = soup.new_tag("meta")
            meta["name"] = key
            meta["content"] = val
            head.append(meta)

    # Réécriture du fichier
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print(f"✅ SEO optimisé : {file_path}")


def run():
    """Parcourt tous les fichiers HTML et les optimise"""
    for root, _, files in os.walk("."):
        for f in files:
            if f.endswith(".html") and not root.startswith("./.github"):
                path = os.path.join(root, f)
                try:
                    optimize_html(path)
                except Exception as e:
                    print(f"⚠️ Erreur sur {path}: {e}")


if __name__ == "__main__":
    run()
