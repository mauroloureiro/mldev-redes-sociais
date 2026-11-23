"""Semana 08 (23 a 27/11/2026): F2 Carrossel (módulo de produção) · F13 Comparação (à medida vs pronto-a-usar) · F6 Sondagem (pagamentos).
Uso: python3 scripts/semana08.py
"""
import sys, pathlib, os
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from kit import *

REPO = pathlib.Path(__file__).resolve().parent.parent
OUT = REPO / "imagens" / "semana-08"
F = pathlib.Path(os.environ.get("MLDEV_FOTOS", REPO / "fotos" / "candidatas"))  # fotos apagadas do repo depois de usadas
SKY, BLUE, NAVY, PAPER = "#4EC2F9", "#103CE7", "#172041", "#ECECE8"

CSS = """
<style>
.mono{font-family:'JB';font-weight:700}
.dots{display:flex;gap:10px}
.dots i{display:block;width:14px;height:14px;border-radius:50%;background:rgba(255,255,255,.28)}
.dots i.on{background:#4EC2F9;width:40px;border-radius:8px}
.cell{font-size:29px;font-weight:700;line-height:1.2;padding:22px 26px;display:flex;align-items:center;gap:16px}
.opt{flex:1;background:rgba(255,255,255,.97);color:#0a0a0a;border-radius:26px;padding:30px 26px 32px;box-shadow:0 18px 46px rgba(0,0,20,.35)}
.opt .k{width:66px;height:66px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:34px;color:#fff;margin-bottom:22px}
.opt p{font-size:30px;font-weight:800;line-height:1.15;letter-spacing:-.5px}
</style>
"""

def dots(n, on):
    return '<div class="dots">' + "".join(f'<i class="{"on" if i == on else ""}"></i>' for i in range(n)) + "</div>"

# ---------- 19 · F2 Carrossel · módulo de produção ----------
cover = f"""{CSS}<div class="post" style="color:#fff">
{foto_bg(F/'post-19'/'02.jpg', 'base', pos='center 30%')}
<div class="top"><span class="tag" style="color:#dfe4f5">Produção · guarda para depois</span>{logo_html('#fff')}</div>
<div style="position:absolute;z-index:3;left:72px;right:72px;bottom:64px">
 <h1 style="font-size:100px;text-transform:none;letter-spacing:-4px;line-height:.98">“Onde está<br>a encomenda?”</h1>
 <div style="font-size:52px;font-weight:900;letter-spacing:-1.5px;color:{SKY};margin-top:18px">“Algures na fábrica.”</div>
 <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-top:44px;padding-top:28px;border-top:2px solid rgba(255,255,255,.25)">
  <div style="font-size:30px;font-weight:700;line-height:1.25;max-width:620px">3 sinais de que a tua produção precisa de um sistema</div>
  <div class="mono" style="font-size:22px;color:#dfe4f5">desliza →</div>
 </div>
</div></div>"""

SINAIS = [
    ("01", "As ordens de fabrico andam <span style='color:" + SKY + "'>em papel.</span>",
     "Passam de mão em mão, ganham rasuras e ninguém tem a certeza de qual é a versão certa."),
    ("02", "Para saber em que fase está uma encomenda, <span style='color:" + SKY + "'>alguém tem de ir lá ver.</span>",
     "O cliente fica à espera ao telefone enquanto se percorre a fábrica à procura de uma resposta."),
    ("03", "A matéria-prima acaba <span style='color:" + SKY + "'>sem ninguém avisar.</span>",
     "Só se descobre quando a máquina para e o prazo prometido ao cliente já está em risco."),
]

def sinal(i, num, titulo, texto):
    return f"""{CSS}<div class="post" style="background:{NAVY};color:#fff">
<div class="grain" style="background-image:url(&quot;{GRAIN}&quot;);opacity:.45"></div>
<div style="position:absolute;z-index:2;right:40px;top:-60px;font-family:'JB';font-weight:700;font-size:460px;line-height:1;color:transparent;-webkit-text-stroke:3px rgba(78,194,249,.35)">{num}</div>
<div class="top"><span class="tag" style="color:{SKY}">Sinal {int(num)} de 3</span></div>
<div style="position:absolute;z-index:3;left:72px;right:110px;top:420px">
 <div style="font-weight:900;font-size:70px;line-height:1.04;letter-spacing:-2.5px">{titulo}</div>
 <div style="font-size:32px;font-weight:600;line-height:1.4;margin-top:34px;color:#c9d0ea;max-width:820px">{texto}</div>
</div>
<div style="position:absolute;z-index:3;left:72px;right:72px;bottom:64px;display:flex;justify-content:space-between;align-items:center">
 {dots(5, i)}{logo_html('#fff')}
</div></div>"""

fecho = f"""{CSS}<div class="post" style="color:#fff">
{foto_bg(F/'post-19-b'/'03.jpg', 'escuro', pos='center')}
<div style="position:relative;z-index:3;display:flex;justify-content:center">{logo_html('#fff')}</div>
<div style="position:absolute;z-index:3;left:72px;right:72px;top:190px;text-align:center">
 <div class="tag" style="color:{SKY};margin-bottom:26px">A solução</div>
 <div style="font-weight:900;font-size:76px;line-height:1.02;letter-spacing:-3px">Um módulo de produção põe a fábrica <span style="color:{SKY}">no ecrã.</span></div>
 <div style="display:flex;justify-content:center;gap:14px;flex-wrap:wrap;margin-top:44px">
  <span style="background:#fff;color:#0a0a0a;font-weight:800;font-size:26px;padding:14px 24px;border-radius:40px">Ordens de fabrico</span>
  <span style="background:#fff;color:#0a0a0a;font-weight:800;font-size:26px;padding:14px 24px;border-radius:40px">Fase de cada encomenda</span>
  <span style="background:#fff;color:#0a0a0a;font-weight:800;font-size:26px;padding:14px 24px;border-radius:40px">Ligado aos stocks</span>
 </div>
 <div style="font-size:28px;font-weight:600;margin-top:30px;color:#e3e7f3">Em tempo real, no computador ou no telemóvel.</div>
</div>
{footer('#fff', SKY, '#0a0a0a')}
</div>"""

p19 = {"post-19-producao-carrossel-1": cover}
for i, (n, t, x) in enumerate(SINAIS, start=1):
    p19[f"post-19-producao-carrossel-{i+1}"] = sinal(i, n, t, x)
p19["post-19-producao-carrossel-5"] = fecho

# ---------- 20 · F13 Comparação · à medida vs pronto-a-usar ----------
ROWS = [
    ("A empresa adapta-se ao programa", "O programa adapta-se à empresa"),
    ("Menus cheios de coisas que ninguém usa", "Só os módulos de que precisas"),
    ("Um Excel ao lado para o que falta", "Liga-se ao que já usas"),
    ("Esperas que o fornecedor mude", "Cresce quando a empresa cresce"),
]
X = '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#8a8a86" stroke-width="3" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'
V = '<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5l5 5L20 6.5"/></svg>'
rows = "".join(
    f"""<div style="display:flex;border-top:2px solid #d4d4ce">
 <div class="cell" style="width:50%;color:#6b6b66"><span style="flex:0 0 30px">{X}</span>{a}</div>
 <div class="cell" style="width:50%;background:{BLUE};color:#fff"><span style="flex:0 0 30px">{V}</span>{b}</div></div>"""
    for a, b in ROWS)
p20 = f"""{CSS}<div class="post" style="background:{PAPER};color:#0a0a0a">
<div class="grain" style="background-image:url(&quot;{CRUMPLE}&quot;);opacity:.6"></div>
<div class="top"><span class="tag" style="color:{BLUE}">Software de gestão</span>{logo_html('#000')}</div>
<div style="position:relative;z-index:3;margin-top:46px;font-weight:900;font-size:66px;line-height:1.02;letter-spacing:-2.5px">Pagas um programa que a equipa <span style="color:{BLUE}">contorna com Excel?</span></div>
<div style="position:absolute;z-index:3;left:72px;right:72px;top:420px">
 <div style="display:flex;font-family:'JB';font-weight:700;font-size:21px;letter-spacing:2px;text-transform:uppercase">
  <div style="width:50%;padding:0 26px 14px;color:#6b6b66">Pronto-a-usar</div>
  <div style="width:50%;padding:14px 26px;background:#0a0a0a;color:#fff">À medida</div>
 </div>
 {rows}
</div>
<div style="position:absolute;z-index:3;left:72px;right:72px;bottom:56px;display:flex;justify-content:space-between;align-items:flex-end">
 <div style="font-size:23px;font-weight:600;color:#44443f;max-width:720px;line-height:1.35">Nem sempre a resposta é à medida. Mas, se o Excel ao lado já é permanente, vale a pena falarmos.</div>
 <div class="mono" style="font-size:21px;color:#44443f">mldev.pt</div>
</div></div>"""

# ---------- 21 · F6 Sondagem · pagamentos ----------
p21 = f"""{CSS}<div class="post" style="color:#fff">
{foto_bg(F/'post-21-b'/'02.jpg', 'navy', pos='center 40%')}
<div class="top"><span class="tag" style="color:{SKY}">Sondagem de sexta</span>{logo_html('#fff')}</div>
<div style="position:relative;z-index:3;margin-top:70px;text-align:center">
 <div style="font-size:34px;font-weight:600;color:#cfd6ee">A fatura foi enviada há uma semana.</div>
 <h1 style="font-size:92px;text-transform:none;letter-spacing:-3.5px;line-height:1;margin-top:22px">Como sabes se o cliente <span style="color:{SKY}">já pagou?</span></h1>
</div>
<div style="position:absolute;z-index:3;left:72px;right:72px;bottom:150px;display:flex;gap:22px">
 <div class="opt"><div class="k" style="background:#0a0a0a">A</div><p>Vou ver ao homebanking, linha a linha</p></div>
 <div class="opt"><div class="k" style="background:#0a0a0a">B</div><p>Peço o comprovativo por e-mail</p></div>
 <div class="opt"><div class="k" style="background:{BLUE}">C</div><p>O sistema mostra-me logo</p></div>
</div>
<div style="position:absolute;z-index:3;left:0;right:0;bottom:70px;text-align:center" class="mono"><span style="font-size:24px;color:#fff">Responde com A, B ou C nos comentários ↓</span></div>
</div>"""

if __name__ == "__main__":
    allp = dict(p19)
    allp["post-20-medida-vs-pronto-comparacao"] = p20
    allp["post-21-pagamentos-sondagem"] = p21
    render(allp, OUT)
