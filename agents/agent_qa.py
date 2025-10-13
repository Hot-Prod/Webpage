from bs4 import BeautifulSoup
with open("index.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

print("🔍 Vérification :")
print("Titre :", soup.title.text if soup.title else "❌ manquant")
print("H1 :", soup.find("h1").text if soup.find("h1") else "❌ manquant")
print("Meta description :", "OK" if soup.find("meta", {"name": "description"}) else "❌ absente")

