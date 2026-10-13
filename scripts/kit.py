"""Kit visual MLDEV (estilo v3) para gerar publicações 1080x1080.
Uso: from kit import *  -> GRAIN, GRAIN_DARK, CRUMPLE, logo_html(cor), footer(fg, btn_bg, btn_fg), render(dict, pasta_saida)
Fontes: descarregadas automaticamente via `npm pack` para ~/.cache/mldev-fonts na primeira execução.
"""
import base64, pathlib, subprocess, tarfile
from playwright.sync_api import sync_playwright

REPO = pathlib.Path(__file__).resolve().parent.parent
MARCA = REPO / "marca"
FONTS = pathlib.Path.home() / ".cache" / "mldev-fonts"

def _ensure_fonts():
    FONTS.mkdir(parents=True, exist_ok=True)
    for pkg, ver in (("montserrat", "5.3.0"), ("jetbrains-mono", "5.3.0")):
        d = FONTS / f"fontsource-{pkg}-{ver}"
        if not d.exists():
            subprocess.run(["npm", "pack", f"@fontsource/{pkg}@{ver}"], cwd=FONTS, check=True, capture_output=True)
            d.mkdir()
            with tarfile.open(FONTS / f"fontsource-{pkg}-{ver}.tgz") as t:
                t.extractall(d)
_ensure_fonts()

def font(path):
    return base64.b64encode((FONTS / path).read_bytes()).decode()

M = "fontsource-montserrat-5.3.0/package/files/montserrat-latin-{}-normal.woff2"
J = "fontsource-jetbrains-mono-5.3.0/package/files/jetbrains-mono-latin-{}-normal.woff2"
FONT_CSS = "".join(
    f"@font-face{{font-family:'Montserrat';font-weight:{w};src:url(data:font/woff2;base64,{font(M.format(w))}) format('woff2');}}"
    for w in (500, 700, 800, 900)
) + "".join(
    f"@font-face{{font-family:'JB';font-weight:{w};src:url(data:font/woff2;base64,{font(J.format(w))}) format('woff2');}}"
    for w in (500, 700)
)


def logo_html(color):
    name = "logobranco.svg" if color.lower() in ("#fff", "#ffffff") else "logopreto.svg"
    b = base64.b64encode((MARCA / name).read_bytes()).decode()
    return f'<img class="logo-img" src="data:image/svg+xml;base64,{b}">'

GRAIN = ("data:image/svg+xml;utf8," +
    "<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>"
    "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/>"
    "<feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 0.09 0'/></filter>"
    "<rect width='100%' height='100%' filter='url(%23n)'/></svg>")
CRUMPLE = ("data:image/svg+xml;utf8," +
    "<svg xmlns='http://www.w3.org/2000/svg' width='1080' height='1080'>"
    "<filter id='c'><feTurbulence type='fractalNoise' baseFrequency='0.006' numOctaves='5' seed='7'/>"
    "<feDiffuseLighting lighting-color='%23ffffff' surfaceScale='3.2'><feDistantLight azimuth='45' elevation='58'/></feDiffuseLighting>"
    "<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  -0.55 0 0 0 0.5'/></filter>"
    "<rect width='100%' height='100%' filter='url(%23c)'/></svg>")
GRAIN_DARK = GRAIN.replace("0 0 0 0 1  0 0 0 0 1  0 0 0 0 1", "0 0 0 0 0  0 0 0 0 0  0 0 0 0 0")

BASE_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1080px}
.post{position:relative;width:1080px;height:1080px;overflow:hidden;font-family:'Montserrat';padding:64px 72px}
.top{display:flex;justify-content:space-between;align-items:center;position:relative;z-index:3}
.logo-img{height:50px;display:block}
.logo-txt{font-weight:900;font-size:34px;letter-spacing:-1px}
.tag{font-family:'JB';font-weight:500;font-size:19px;letter-spacing:2px;text-transform:uppercase}
h1{position:relative;z-index:3;font-weight:900;text-transform:uppercase;line-height:.9;letter-spacing:-3px}
.foot{position:absolute;left:72px;right:72px;bottom:60px;display:flex;align-items:center;justify-content:space-between;z-index:3}
.cta{display:flex;align-items:center;gap:22px}
.btn{width:76px;height:76px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.cta b{display:block;font-weight:800;font-size:25px}
.cta span{display:block;font-family:'JB';font-weight:500;font-size:20px;margin-top:4px}
.tel{font-family:'JB';font-weight:700;font-size:21px;text-align:right}
.tel small{display:block;font-family:'Montserrat';font-weight:500;font-size:14px;opacity:.6;margin-top:4px}
.grain{position:absolute;inset:0;z-index:1;pointer-events:none}
"""

def arrow(color):
    return f'<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

def footer(fg, btn_bg, btn_fg):
    return f"""<div class="foot" style="color:{fg}">
  <div class="cta"><div class="btn" style="background:{btn_bg}">{arrow(btn_fg)}</div>
  <div><b>Pede a tua proposta gratuita</b><span>mldev.pt/contactos</span></div></div>
  <div class="tel">+351 231 109 068<small>chamada para a rede fixa nacional</small></div></div>"""


def render(posts, out_dir):
    """posts: {"nome-ficheiro": "<div class='post'>...</div>"}; grava PNG 1080x1080 em out_dir."""
    out = pathlib.Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1080})
        for name, body in posts.items():
            pg.set_content(f"<html><head><style>{FONT_CSS}{BASE_CSS}</style></head><body>{body}</body></html>")
            pg.wait_for_timeout(400)
            pg.screenshot(path=str(out / f"{name}.png"), clip={"x": 0, "y": 0, "width": 1080, "height": 1080})
            print("ok", name)
        b.close()
