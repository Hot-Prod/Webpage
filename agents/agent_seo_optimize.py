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
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    # Titre et description par défaut
    title_tag = soup.find("title")
    title = title_tag.text.strip() if title_tag else "HotProd — Industrialisation & Innovation"
    description = f"Découvrez les solutions HotProd : {title.lower()}."

    # --- META de base ---
    metas = {
        "description": description,
        "viewport": "width=device-width, initial-scale=1",
        "charset": "utf-8",
        "robots": "index,follow"
    }

    head = soup.head
    if not head:
        return

    for key, val in metas.items():
        if key == "charset":
            if not head.find("meta", attrs={"charset": True}):
                meta = soup.new_tag("meta", charset=val)
                head.insert(0, meta)
        else:
            tag = head.find("meta", attrs={"name": key})
            if tag:
                tag["content"] = val
            else:
                meta = soup.new_tag("meta", name=key, content=val)
                head.append(meta)

    # --- OpenGraph ---
    og_tags = {
        "og:title": title,
        "og:description": description,
        "og:type": "website",
        "og:url": f"{BASE_URL}/{os.path.relpath(file_path,'.')}",
        "og:image": f"{BASE_URL}/assets/hero-visual.png",
        "og:site_name": "HotProd"
    }

    for key, val in og_tags.items():
        tag = head.find("meta", attrs={"property": key})
        if tag:
            tag["content"] = val
        else:
            meta = soup.new_tag("meta", property=key, content=val)
            head.append(meta)

    # --- Twitter Card ---
    twitter_tags = {
        "twitter:card": "summary_large_image",
        "twitter:title": title,
        "twitter:description": description,
        "twitter:image": f"{BASE_URL}/assets/hero-visual.png",
    }

    for key, val in twitter_tags.items():
        tag = head.find("meta", attrs={"name": key})
        if tag:
            tag["content"] = val
        else:
            meta = soup.new_tag("meta", name=key, content=val)
            head.append(meta)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print(f"✅ SEO optimisé : {file_path}")


def run():
    for root, _, files in os.walk("."):
        for f in files:
            if f.endswith(".html") and not root.startswith("./.github"):
                path = os.path.join(root, f)
                optimize_html(path)

if __name__ == "__main__":
    run()
