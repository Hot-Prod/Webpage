from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

print("✅ Vérification du site :")
print("Meta description :", "OK" if soup.find("meta", {"name": "description"}) else "❌")
print("Balise H1 :", soup.find("h1").text if soup.find("h1") else "❌")
print("Formulaire :", "OK" if soup.find("form") else "❌")
