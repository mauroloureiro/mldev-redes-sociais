"""Fotografias de fundo para as publicações MLDEV.

Fonte principal: API do Pexels (licença Pexels: uso comercial grátis, sem atribuição obrigatória).
A chave NUNCA vai para o repositório (é público): lê-se da variável de ambiente PEXELS_API_KEY
ou do ficheiro ~/.config/mldev/pexels.key.

Fallback: fotografias guardadas em marca/fotos/<pasta>/*.jpg (quando a API não estiver disponível).
Se não houver nenhuma fotografia, foto() devolve None e a publicação usa um fundo da marca (sem foto).

Uso:
    from fotos import foto
    f = foto("tired office worker paperwork stack", slug="post-16")
    # f = {"path": Path, "id": ..., "fotografo": ..., "url": ..., "fonte": "pexels"|"biblioteca"} ou None

As fotos usadas ficam em fotos_usadas.json (raiz do repo) para não se repetirem.
"""
import json, os, pathlib, random, urllib.parse, urllib.request

REPO = pathlib.Path(__file__).resolve().parent.parent
USADAS = REPO / "fotos_usadas.json"
BIBLIOTECA = REPO / "marca" / "fotos"
CACHE = pathlib.Path.home() / ".cache" / "mldev-fotos"


def _key():
    k = os.environ.get("PEXELS_API_KEY", "").strip()
    if not k:
        f = pathlib.Path.home() / ".config" / "mldev" / "pexels.key"
        if f.exists():
            k = f.read_text().strip()
    return k or None


def _usadas():
    return json.loads(USADAS.read_text()) if USADAS.exists() else []


def _marcar(entry):
    u = _usadas()
    u.append(entry)
    USADAS.write_text(json.dumps(u, ensure_ascii=False, indent=2) + "\n")


def pesquisar(query, n=15, orientation="square"):
    """Devolve a lista de fotos do Pexels (dicts da API) ou [] se não houver acesso."""
    key = _key()
    if not key:
        return []
    q = urllib.parse.urlencode({"query": query, "per_page": n, "orientation": orientation})
    req = urllib.request.Request(f"https://api.pexels.com/v1/search?{q}",
                                 headers={"Authorization": key, "User-Agent": "mldev-redes-sociais"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r).get("photos", [])
    except Exception as e:
        print("Pexels indisponível:", e)
        return []


def _descarregar(p, slug):
    CACHE.mkdir(parents=True, exist_ok=True)
    dest = CACHE / f"{slug}-pexels-{p['id']}.jpg"
    if not dest.exists():
        url = p["src"]["original"] + "?auto=compress&cs=tinysrgb&fit=crop&w=1600&h=1600"
        req = urllib.request.Request(url, headers={"User-Agent": "mldev-redes-sociais"})
        with urllib.request.urlopen(req, timeout=60) as r:
            dest.write_bytes(r.read())
    return dest


def foto(query, slug, pasta=None, escolha=0, orientation="square"):
    """Escolhe uma foto relacionada com `query` que ainda não tenha sido usada.
    escolha: índice entre os resultados ainda não usados (para experimentar alternativas).
    pasta: subpasta de marca/fotos/ a usar no fallback (ex.: "erp", "websites")."""
    usadas = {str(u.get("id")) for u in _usadas()}
    livres = [p for p in pesquisar(query, orientation=orientation) if str(p["id"]) not in usadas]
    if livres:
        p = livres[min(escolha, len(livres) - 1)]
        path = _descarregar(p, slug)
        entry = {"id": str(p["id"]), "fonte": "pexels", "query": query, "post": slug,
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
