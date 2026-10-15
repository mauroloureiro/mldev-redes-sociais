"""Semana 6 (09–13/11/2026), versão com formatos variados.
13 · F9 Conversa (navy)      · Apps, modo offline
14 · F2 Carrossel 5 slides (papel) · Websites, CMS
15 · F6 Pergunta (azul, único com CTA completo) · Suporte, backups
Correr: python3 scripts/semana06.py -> imagens/semana-06/
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from kit import *

NAVY, BLUE, BLUE2, SKY, INK, PAPER = "#172041", "#103CE7", "#2569ED", "#4EC2F9", "#0a0a0a", "#ECECE8"

EXTRA_CSS = """
.mono{font-family:'JB'}
.chat-head{display:flex;align-items:center;gap:18px;padding:22px 28px;border-radius:26px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.09)}
.avatar{width:58px;height:58px;border-radius:50%;background:#2a3566;display:flex;align-items:center;justify-content:center}
.bubble{max-width:640px;padding:16px 24px;border-radius:26px;font-size:27px;line-height:1.3;font-weight:600;position:relative}
.in{background:#fff;color:#111;border-bottom-left-radius:8px}
.out{background:#2569ED;color:#fff;border-bottom-right-radius:8px;margin-left:auto}
.who{font-family:'JB';font-size:17px;letter-spacing:1px;margin:0 0 8px 6px;color:#8d97c4}
.meta{font-family:'JB';font-size:15px;margin-top:4px;opacity:.55;text-align:right}
"""

def page(html):
    return f"<style>{EXTRA_CSS}</style>{html}"

def ticks(color):
    return f'<svg width="30" height="18" viewBox="0 0 30 18" fill="none" stroke="{color}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M1 9l5 5L16 3"/><path d="M12 13l1 1L24 3"/></svg>'

# ---------- 13 · F9 Conversa ----------
P13 = page(f"""<div class="post" style="background:{NAVY};color:#fff;padding:60px 72px">
<div class="grain" style="background-image:url(&quot;{GRAIN}&quot;);opacity:.7"></div>
<div style="position:relative;z-index:3">
 <div class="chat-head">
  <div class="avatar"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#c9d1f5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.4"/><path d="M16 14.2c2.8.3 5 2.6 5 5.8"/></svg></div>
  <div><div style="font-weight:800;font-size:27px">Equipa · Encomendas</div><div class="mono" style="font-size:17px;color:#8d97c4;margin-top:4px">armazém, escritório</div></div>
  <div class="mono" style="margin-left:auto;font-size:17px;color:#8d97c4">qua 09:12</div>
 </div>

 <div style="margin-top:30px">
  <div class="who">ARMAZÉM</div>
  <div class="bubble in" style="width:fit-content">Aqui no armazém não há rede nenhuma 😩<div class="meta" style="color:#555">09:12</div></div>
 </div>
 <div style="margin-top:12px">
  <div class="bubble in" style="width:fit-content">Como é que registo as encomendas?<div class="meta" style="color:#555">09:12</div></div>
 </div>
 <div style="margin-top:22px">
  <div class="bubble out" style="width:fit-content">Regista na app na mesma. Quando apanhares rede, sincroniza sozinha 👍<div class="meta" style="display:flex;justify-content:flex-end;gap:8px;align-items:center;opacity:.8">09:13 {ticks('#fff')}</div></div>
 </div>
 <div style="margin-top:22px">
  <div class="who">ARMAZÉM</div>
  <div class="bubble in" style="width:fit-content">Já está ✅<div class="meta" style="color:#555">09:41</div></div>
 </div>
 <div style="margin:20px auto 0;width:fit-content;font-family:'JB';font-size:17px;color:#c9d1f5;background:rgba(78,194,249,.12);border:1px solid rgba(78,194,249,.35);padding:12px 22px;border-radius:40px">
  ⟳ 3 registos guardados sem rede · sincronizados às 09:41</div>
</div>

<div style="position:absolute;z-index:3;left:72px;right:72px;bottom:58px;display:flex;justify-content:space-between;align-items:flex-end">
 <div style="font-weight:900;font-size:54px;line-height:1;letter-spacing:-2px">Sem rede?<br><span style="color:{SKY}">A app continua.</span></div>
 <div style="text-align:right">{logo_html('#fff')}<div class="mono" style="font-size:17px;color:#8d97c4;margin-top:10px">mldev.pt</div></div>
</div>
</div>""")

# ---------- 14 · F2 Carrossel (5 slides) ----------
ICONS = {
 "relogio": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/>',
 "jornal": '<rect x="3" y="4" width="15" height="16" rx="1.5"/><path d="M18 8h3v10a2 2 0 0 1-2 2"/><path d="M7 8h7M7 12h7M7 16h4"/>',
 "foto": '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="10" r="1.8"/><path d="M21 16l-5-5-8 8"/>',
 "lista": '<path d="M9 6h11M9 12h11M9 18h11"/><path d="M4 6l1 1 2-2M4 12l1 1 2-2M4 18l1 1 2-2"/>',
}
def icon(name, size=120, color=BLUE, sw=1.6):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>'

def paper_bg():
    return (f'<div class="grain" style="background-image:url(&quot;{CRUMPLE}&quot;)"></div>'
            f'<div class="grain" style="background-image:url(&quot;{GRAIN_DARK}&quot;);opacity:.6"></div>')

def dots(active, total=5):
    return "".join(f'<span style="width:{30 if i==active else 12}px;height:12px;border-radius:6px;background:{INK if i==active else "#bdbdb6"};display:inline-block;margin-right:8px"></span>' for i in range(1, total+1))

C1 = page(f"""<div class="post" style="background:{PAPER};color:{INK}">
{paper_bg()}
<div class="top">{logo_html(INK)}</div>
<div style="position:absolute;z-index:2;right:30px;top:40px;font-weight:900;font-size:760px;line-height:.8;color:{BLUE};letter-spacing:-30px">5</div>
<div style="position:absolute;z-index:3;left:72px;bottom:190px;width:560px">
 <div style="font-weight:900;font-size:66px;line-height:1.02;letter-spacing:-2px">coisas que podes mudar no teu site</div>
 <div style="margin-top:22px;font-weight:600;font-size:32px;line-height:1.3;color:#3a3a36">sem ligar a um programador.</div>
</div>
<div style="position:absolute;z-index:3;left:72px;right:72px;bottom:70px;display:flex;justify-content:space-between;align-items:center">
 <div>{dots(1)}</div><div class="mono" style="font-size:22px;font-weight:700">desliza →</div>
</div>
</div>""")

def slide(n, idx, icn, title, text, example):
    return page(f"""<div class="post" style="background:{PAPER};color:{INK}">
{paper_bg()}
<div class="top"><div class="mono" style="font-size:24px;font-weight:700;color:{BLUE}">{n:02d} / 05</div><div class="tag" style="color:#6b6b66">Sem programador</div></div>
<div style="position:relative;z-index:3;margin-top:170px">{icon(icn)}</div>
<div style="position:relative;z-index:3;margin-top:40px;font-weight:900;font-size:96px;line-height:.95;letter-spacing:-3px">{title}</div>
<div style="position:relative;z-index:3;margin-top:30px;width:820px;font-weight:500;font-size:34px;line-height:1.4;color:#3a3a36">{text}</div>
<div style="position:relative;z-index:3;margin-top:40px;display:inline-block;font-family:'JB';font-size:22px;background:#fff;border:2px solid {INK};border-radius:14px;padding:14px 22px;box-shadow:6px 6px 0 {INK}">{example}</div>
<div style="position:absolute;z-index:3;left:72px;right:72px;bottom:70px;display:flex;justify-content:space-between;align-items:center">
 <div>{dots(idx)}</div>{logo_html(INK).replace('class="logo-img"','class="logo-img" style="height:38px"')}
</div>
</div>""")

C2 = slide(1, 2, "relogio", "O horário.", "Feriado, horário de inverno, férias de agosto. Mudas num minuto, sem esperar por ninguém.", "Seg–Sex · 9h–18h <span style='color:#103CE7'>→</span> 9h–17h")
C3 = slide(2, 3, "jornal", "As novidades.", "Um produto novo, uma vaga de emprego, um evento. Escreves, carregas em Publicar e já está online.", "+ Nova notícia &nbsp;·&nbsp; <span style='color:#103CE7'>Publicar</span>")
C4 = slide(3, 4, "foto", "As fotografias.", "Trocas imagens de destaque e galerias com arrastar e largar. O site ajusta o tamanho sozinho.", "montra-natal.jpg &nbsp;<span style='color:#103CE7'>✓ carregada</span>")

C5 = page(f"""<div class="post" style="background:{PAPER};color:{INK}">
{paper_bg()}
<div class="top"><div class="mono" style="font-size:24px;font-weight:700;color:{BLUE}">04 + 05 / 05</div><div class="tag" style="color:#6b6b66">Sem programador</div></div>
<div style="position:relative;z-index:3;margin-top:80px;display:flex;gap:28px;align-items:center">{icon('lista', 110)}</div>
<div style="position:relative;z-index:3;margin-top:34px;font-weight:900;font-size:86px;line-height:.95;letter-spacing:-3px">Os serviços<br>e os contactos.</div>
<div style="position:relative;z-index:3;margin-top:26px;width:800px;font-weight:500;font-size:32px;line-height:1.4;color:#3a3a36">Novo serviço, novo telefone, nova morada. Tudo no mesmo painel.</div>
<div style="position:absolute;z-index:3;left:0;right:0;bottom:0;height:300px;background:{INK};color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 72px">
 <div>
  <div style="font-weight:900;font-size:50px;line-height:1.05;letter-spacing:-1px">Guarda para<br>mais tarde.</div>
  <div style="margin-top:20px">{dots(5).replace('#bdbdb6','#4a4a4a').replace(f'background:{INK}','background:#fff')}</div>
 </div>
 <div style="text-align:right">{logo_html('#fff').replace('class="logo-img"','class="logo-img" style="height:64px;margin-left:auto"')}<div class="mono" style="font-size:20px;color:#9a9a9a;margin-top:14px">mldev.pt</div></div>
</div>
</div>""")

# ---------- 15 · F6 Pergunta ----------
def option(letter, text):
    return f"""<div style="display:flex;align-items:center;gap:28px;border:3px solid rgba(255,255,255,.85);border-radius:24px;padding:22px 28px;margin-top:20px">
 <div style="width:64px;height:64px;border-radius:50%;background:{INK};color:#fff;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:32px;flex:none">{letter}</div>
 <div style="font-weight:800;font-size:40px">{text}</div></div>"""

P15 = page(f"""<div class="post" style="background:{BLUE};color:#fff">
<div class="grain" style="background-image:url(&quot;{GRAIN}&quot;);opacity:.8"></div>
<div class="top">{logo_html('#fff')}<div class="tag" style="color:rgba(255,255,255,.75)">Pergunta da semana</div></div>
<div style="position:relative;z-index:3;margin-top:52px;font-weight:900;font-size:60px;line-height:1.04;letter-spacing:-1.5px">Quando foi feita a última cópia de segurança dos dados da <span style="color:{INK}">tua empresa?</span></div>
<div style="position:relative;z-index:3;margin-top:28px">
 {option('A','Ontem à noite')}
 {option('B','Não faço ideia')}
 {option('C','Cópia de quê? 😅')}
</div>
<div class="mono" style="position:relative;z-index:3;margin-top:24px;font-size:22px;color:rgba(255,255,255,.85)">Responde nos comentários ↓</div>
{footer('#fff', INK, '#fff')}
</div>""")

POSTS = {
 "post-13-sem-rede-conversa": P13,
 "post-14-cms-carrossel-1": C1, "post-14-cms-carrossel-2": C2, "post-14-cms-carrossel-3": C3,
 "post-14-cms-carrossel-4": C4, "post-14-cms-carrossel-5": C5,
 "post-15-backups-pergunta": P15,
}
render(POSTS, REPO / "imagens" / "semana-06")
