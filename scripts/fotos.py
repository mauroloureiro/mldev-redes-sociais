"""Fotografias de fundo para as publicações MLDEV.

Fontes (por esta ordem):
  1. API do Pixabay — chave em PIXABAY_API_KEY (licença Pixabay: uso comercial grátis, sem atribuição obrigatória).
  2. API do Pexels  — chave em PEXELS_API_KEY (pedidos de chave estavam em pausa em 11/2026).
As chaves NUNCA vão para o repositório (é público): vêm de variáveis de ambiente
ou de ~/.config/mldev/pixabay.key / pexels.key.

Fallback: fotografias guardadas em marca/fotos/<pasta>/*.jpg (quando a API não estiver disponível).
Se não houver nenhuma fotografia, foto() devolve None e a publicação usa um fundo da marca (sem foto).

Uso:
    from fotos import foto
    f = foto("tired office worker paperwork stack", slug="post-16")
    # f = {"path": Path, "id": ..., "fotografo": ..., "url": ..., "fonte": "pixabay"|"pexels"|"biblioteca"} ou None

As fotos usadas ficam em fotos_usadas.json (raiz do repo) para não se repetirem.
"""
import json, os, pathlib, random, urllib.parse, urllib.request

REPO = pathlib.Path(__file__).resolve().parent.parent
USADAS = REPO / "fotos_usadas.json"
BIBLIOTECA = REPO / "marca" / "fotos"
CACHE = pathlib.Path.home() / ".cache" / "mldev-fotos"


def _key(nome="pexels"):
    k = os.environ.get(f"{nome.upper()}_API_KEY", "").strip()
    if not k:
        f = pathlib.Path.home() / ".config" / "mldev" / f"{nome}.key"
        if f.exists():
            k = f.read_text().strip()
    return k or None


def _pixabay(query, n=20):
    """Resultados do Pixabay normalizados para o formato usado aqui."""
    key = _key("pixabay")
    if not key:
        return []
    q = urllib.parse.urlencode({"key": key, "q": query, "image_type": "photo", "per_page": n,
                                "safesearch": "true", "min_width": 1080, "min_height": 1080, "order": "popular"})
    try:
        req = urllib.request.Request(f"https://pixabay.com/api/?{q}", headers={"User-Agent": "mldev-redes-sociais"})
        with urllib.request.urlopen(req, timeout=30) as r:
            hits = json.load(r).get("hits", [])
    except Exception as e:
        print("Pixabay indisponível:", e)
        return []
    return [{"id": f"pixabay-{h['id']}", "fonte": "pixabay", "download": h.get("largeImageURL"),
             "photographer": h.get("user"), "url": h.get("pageURL"), "alt": h.get("tags")} for h in hits]


def _usadas():
    return json.loads(USADAS.read_text()) if USADAS.exists() else []


def _marcar(entry):
    u = _usadas()
    u.append(entry)
    USADAS.write_text(json.dumps(u, ensure_ascii=False, indent=2) + "\n")


def pesquisar(query, n=15, orientation="square"):
    """Devolve fotos (Pixabay primeiro, depois Pexels) ou [] se não houver acesso."""
    r = _pixabay(query)
    if r:
        return r
    key = _key("pexels")
    if not key:
        return []
    q = urllib.parse.urlencode({"query": query, "per_page": n, "orientation": orientation})
    req = urllib.request.Request(f"https://api.pexels.com/v1/search?{q}",
                                 headers={"Authorization": key, "User-Agent": "mldev-redes-sociais"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            fotos = json.load(r).get("photos", [])
    except Exception as e:
        print("Pexels indisponível:", e)
        return []
    return [{"id": str(p["id"]), "fonte": "pexels", "photographer": p.get("photographer"), "url": p.get("url"),
             "alt": p.get("alt"), "download": p["src"]["original"] + "?auto=compress&cs=tinysrgb&fit=crop&w=1600&h=1600"}
            for p in fotos]


def _descarregar(p, slug):
    CACHE.mkdir(parents=True, exist_ok=True)
    dest = CACHE / f"{slug}-{p['fonte']}-{p['id']}.jpg"
    if not dest.exists():
        req = urllib.request.Request(p["download"], headers={"User-Agent": "mldev-redes-sociais"})
        with urllib.request.urlopen(req, timeout=60) as r:
            dest.write_bytes(r.read())
    return dest


def foto(query, slug, pasta=None, escolha=0, orientation="square"):
    """Escolhe uma foto relacionada com `query` que ainda não tenha sido usada.
    escolha: índice entre os resultados ainda não usados (para experimentar alternativas).
    pasta: subpasta de marca/fotos/ a usar no fallback (ex.: "erp", "websites")."""
    usadas = {str(u.get("id")) for u in _usadas()}
    livres = [p for p in pesquisar(query, orientation=orientation) if str(p["id"]) not in usadas and p.get("download")]
    if livres:
        p = livres[min(escolha, len(livres) - 1)]
        path = _descarregar(p, slug)
        entry = {"id": str(p["id"]), "fonte": p["fonte"], "query": query, "post": slug,
                 "fotografo": p.get("photographer"), "url": p.get("url"), "alt": p.get("alt")}
        _marcar(entry)
        return {**entry, "path": path}
    # fallback: biblioteca local
    dirs = [BIBLIOTECA / pasta] if pasta else []
    dirs.append(BIBLIOTECA)
    for d in dirs:
        if d.exists():
            cands = [f for f in sorted(d.rglob("*")) if f.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp")
                     and str(f.relative_to(REPO)) not in usadas]
            if cands:
                f = cands[escolha % len(cands)] if escolha else random.choice(cands)
                entry = {"id": str(f.relative_to(REPO)), "fonte": "biblioteca", "query": query, "post": slug}
                _marcar(entry)
                return {**entry, "path": f}
    print("Sem fotografia disponível para:", query)
    return None
