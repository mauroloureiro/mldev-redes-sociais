"""Corre no GitHub Actions (autorizado pelo Mauro a 15/11/2026).
Lê fotos/pedidos.json  -> [{"slug": "post-16", "query": "messy office desk paperwork", "n": 6}, ...]
e grava candidatas em fotos/candidatas/<slug>/NN.jpg + meta.json (fonte, autor, link, licença).
Fontes: Pixabay (secret PIXABAY_API_KEY), Pexels (secret PEXELS_API_KEY), senão Openverse (sem chave; só CC0/domínio público).
"""
import io, json, os, pathlib, urllib.parse, urllib.request
from PIL import Image, ImageOps

REPO = pathlib.Path(__file__).resolve().parent.parent
PED = REPO / "fotos" / "pedidos.json"
OUT = REPO / "fotos" / "candidatas"
UA = {"User-Agent": "mldev-redes-sociais/1.0 (github actions)"}

def get_json(url, headers=None):
    req = urllib.request.Request(url, headers={**UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.load(r)

def pixabay(q, n):
    k = os.environ.get("PIXABAY_API_KEY")
    if not k: return []
    d = get_json("https://pixabay.com/api/?" + urllib.parse.urlencode({"key": k, "q": q, "image_type": "photo",
        "per_page": max(n * 2, 10), "safesearch": "true", "min_width": 1200, "min_height": 1080}))
    return [{"dl": h["largeImageURL"], "fonte": "pixabay", "autor": h.get("user"), "link": h.get("pageURL"),
             "licenca": "Pixabay Content License", "desc": h.get("tags")} for h in d.get("hits", [])]

def pexels(q, n):
    k = os.environ.get("PEXELS_API_KEY")
    if not k: return []
    d = get_json("https://api.pexels.com/v1/search?" + urllib.parse.urlencode({"query": q, "per_page": max(n * 2, 10),
        "orientation": "square"}), {"Authorization": k})
    return [{"dl": p["src"]["large2x"], "fonte": "pexels", "autor": p.get("photographer"), "link": p.get("url"),
             "licenca": "Pexels License", "desc": p.get("alt")} for p in d.get("photos", [])]

def openverse(q, n):
    d = get_json("https://api.openverse.org/v1/images/?" + urllib.parse.urlencode({"q": q, "license": "cc0,pdm",
        "page_size": max(n * 3, 20), "mature": "false"}))
    res = d.get("results", [])
    print("openverse:", q, "->", len(res), "resultados")
    out = []
    for r in res:
        if (r.get("width") or 1200) >= 900 and (r.get("height") or 1000) >= 700:
            out.append({"dl": r["url"], "fonte": "openverse/" + (r.get("source") or ""), "autor": r.get("creator"),
                        "link": r.get("foreign_landing_url"), "licenca": (r.get("license") or "").upper(), "desc": r.get("title")})
    return out

def main():
    pedidos = json.loads(PED.read_text()) if PED.exists() else []
    for p in pedidos:
        slug, q, n = p["slug"], p["query"], int(p.get("n", 6))
        d = OUT / slug
        if (d / "meta.json").exists():
            continue
        cands = []
        for f in (pixabay, pexels, openverse):
            try:
                cands = f(q, n)
            except Exception as e:
                print(f.__name__, "falhou:", e)
            if cands: break
        d.mkdir(parents=True, exist_ok=True)
        meta = []
        for c in cands:
            if len(meta) >= n: break
            try:
                req = urllib.request.Request(c["dl"], headers=UA)
                with urllib.request.urlopen(req, timeout=60) as r:
                    im = ImageOps.exif_transpose(Image.open(io.BytesIO(r.read()))).convert("RGB")
                im = ImageOps.fit(im, (1400, 1400), Image.LANCZOS)
                name = f"{len(meta)+1:02d}.jpg"
                im.save(d / name, "JPEG", quality=80)
                meta.append({**{k: v for k, v in c.items() if k != "dl"}, "ficheiro": name, "url_original": c["dl"]})
            except Exception as e:
                print("download falhou:", c.get("dl"), e)
        if not meta:
            print(slug, "sem fotos — não grava, para se poder repetir")
            continue
        (d / "meta.json").write_text(json.dumps({"query": q, "candidatas": meta}, ensure_ascii=False, indent=2) + "\n")
        print(slug, q, "->", len(meta), "fotos")

if __name__ == "__main__":
    main()
