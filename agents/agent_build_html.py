import json, os, html
def build_page(data, lang="fr"):
    title = html.escape(data["home"]["title"])
    subtitle = html.escape(data["home"]["subtitle"])
    bullets = "".join(f"<li>{html.escape(b)}</li>" for b in data["home"]["bullets"])
    services_html = ""
    for s in data["services"]:
        services_html += f"<article class='bg-white p-6 rounded-lg shadow mb-4'><h4 class='font-semibold'>{html.escape(s['title'])}</h4><p class='text-slate-600'>{html.escape(s['summary'])}</p><ul class='list-disc pl-5 text-sm'>{''.join(f'<li>{html.escape(b)}</li>' for b in s['bullets'])}</ul></article>"
    about_html = "".join(f"<p class='text-slate-600'>{html.escape(p)}</p>" for p in data["about"]["paragraphs"])
    testimonial = data.get("testimonial",{})
    seo = data.get("seo",{})
    body = f"""<!doctype html>
<html lang="{lang}">
<head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{html.escape(seo.get('meta_title', title))}</title>
<meta name="description" content="{html.escape(seo.get('meta_description',''))}"/>
<link rel="canonical" href="https://hot-prod.github.io/Webpage/"/>
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head><body class='bg-slate-50 text-slate-900 antialiased'>
  <header class='bg-white border-b p-4'><div class='max-w-5xl mx-auto'><h1 class='text-lg font-bold'>HotProd – Laurent Garnier</h1></div></header>
  <main class='max-w-5xl mx-auto p-6'>
    <section id='home'><h2 class='text-3xl font-bold'>{title}</h2><p class='text-lg text-slate-600'>{subtitle}</p><ul class='list-disc pl-5'>{bullets}</ul></section>
    <section id='services' class='mt-8'><h3 class='text-2xl font-semibold'>Services</h3>{services_html}</section>
    <section id='about' class='mt-8'><h3 class='text-2xl font-semibold'>À propos</h3>{about_html}</section>
    <section id='testimonial' class='mt-8'><blockquote class='italic text-slate-600'>{html.escape(testimonial.get('quote',''))}</blockquote><div class='text-sm text-slate-500'>{html.escape(testimonial.get('name',''))} — {html.escape(testimonial.get('company',''))}</div></section>
  </main>
</body></html>"""
    return body

def main():
    for lang in ["fr","en"]:
        path = f"agents/results/contenu_{lang}.json"
        if not os.path.exists(path):
            print(f"⚠️ {path} manquant; générer d'abord le contenu.")
            continue
        data = json.load(open(path,"r",encoding="utf-8"))
        html_page = build_page(data, lang=lang if lang=="fr" else "en")
        out_dir = lang if lang!="fr" else "fr"
        os.makedirs(out_dir, exist_ok=True)
        with open(f"{out_dir}/index.html","w",encoding="utf-8") as f:
            f.write(html_page)
        print(f"✅ page {out_dir}/index.html générée")
if __name__=="__main__":
    main()
