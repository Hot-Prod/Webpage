from bs4 import BeautifulSoup
import os,json
def check(file):
    if not os.path.exists(file):
        return f"❌ {file} absent"
    s = open(file,encoding="utf-8").read()
    soup = BeautifulSoup(s,"html.parser")
    title = soup.title.text if soup.title else "MISSING"
    h1 = soup.find("h2").text if soup.find("h2") else "MISSING"
    meta = bool(soup.find("meta",{"name":"description"}))
    return f"OK {file} -> title:'{title[:60]}', h2:'{h1[:60]}', meta:{meta}"
for f in ["fr/index.html","en/index.html","index.html"]:
    print(check(f))
