"""Semana 07 (16 a 20/11/2026): F5 Antes/Depois (stocks) · F7 Checklist + interação (RH) · F14 Notificação (web e mobile).
Uso: python3 scripts/semana07.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from kit import *

REPO = pathlib.Path(__file__).resolve().parent.parent
OUT = REPO / "imagens" / "semana-07"
import os
F = pathlib.Path(os.environ.get("MLDEV_FOTOS", REPO / "fotos" / "candidatas"))  # fotos apagadas do repo: ver commit 7164767
SKY, BLUE, NAVY, PAPER = "#4EC2F9", "#103CE7", "#172041", "#ECECE8"

CSS = """
<style>
.lbl{font-family:'JB';font-weight:700;font-size:20px;letter-spacing:3px;text-transform:uppercase;padding:8px 14px;display:inline-block}
.row{display:flex;align-items:center;gap:22px;padding:18px 0;border-bottom:2px solid rgba(255,255,255,.14)}
.box{flex:0 0 46px;height:46px;border:4px solid #4EC2F9;border-radius:8px}
.row p{font-size:31px;font-weight:700;line-height:1.18}
.ntf{background:rgba(255,255,255,.96);color:#111;border-radius:30px;padding:24px 28px;box-shadow:0 20px 50px rgba(0,0,20,.35)}
.ntf .h{display:flex;justify-content:space-between;font-family:'JB';font-weight:500;font-size:19px;color:#555;margin-bottom:8px}
.ntf .h b{font-family:'Montserrat';font-weight:800;color:#111;font-size:21px}
.ntf p{font-size:30px;font-weight:600;line-height:1.25}
.ic{width:34px;height:34px;border-radius:9px;display:inline-flex;align-items:center;justify-content:center;margin-right:12px;vertical-align:middle}
</style>
"""

# ---------- 16 · F5 Antes / Depois · stocks ----------
p16 = f"""{CSS}<div class="post" style="padding:0;color:#fff">
<div style="position:absolute;left:0;top:0;width:1080px;height:560px;overflow:hidden">
 {foto_bg(F/'post-16'/'05.jpg', 'escuro', pos='center 40%')}
 <div style="position:absolute;z-index:3;left:72px;top:64px"><span class="lbl" style="background:#fff;color:#0a0a0a">Antes</span></div>
 <div style="position:absolute;z-index:3;left:72px;right:72px;bottom:56px">
  <div style="font-size:34px;font-weight:600;color:#d9deea;margin-bottom:14px">“Ainda temos daquela referência?”</div>
  <h1 style="font-size:86px;text-transform:none;letter-spacing:-3px;line-height:.98">“Tenho de ir<br>ao armazém ver.”</h1>
 </div>
</div>
<div style="position:absolute;left:0;top:560px;width:1080px;height:520px;background:{PAPER};color:#0a0a0a">
 <div class="grain" style="background-image:url(&quot;{CRUMPLE}&quot;);opacity:.55"></div>
 <div style="position:absolute;z-index:3;left:72px;top:50px"><span class="lbl" style="background:{BLUE};color:#fff">Depois</span></div>
 <div style="position:absolute;z-index:3;left:72px;top:130px;width:500px">
  <div style="font-weight:900;font-size:54px;line-height:1.02;letter-spacing:-2px">Abres o sistema. <span style="color:{BLUE}">Já sabes.</span></div>
  <div style="font-size:26px;font-weight:600;line-height:1.38;margin-top:22px;color:#333">Um módulo de stocks mostra o que tens, onde está e o que falta. Sem sair da secretária.</div>
 </div>
 <div style="position:absolute;z-index:3;right:72px;top:118px;width:380px;background:#fff;border-radius:22px;padding:26px 28px;box-shadow:0 14px 40px rgba(0,0,0,.12);font-family:'JB'">
  <div style="font-size:16px;letter-spacing:2px;color:#777;text-transform:uppercase">Stock · armazém</div>
  <div style="font-family:'Montserrat';font-weight:800;font-size:25px;margin:10px 0 18px">Ref. 2041 · caixa M</div>
  <div style="display:flex;justify-content:space-between;font-size:21px;padding:9px 0;border-top:1px solid #e3e3e3"><span>Disponível</span><b style="color:{BLUE}">38 un.</b></div>
  <div style="display:flex;justify-content:space-between;font-size:21px;padding:9px 0;border-top:1px solid #e3e3e3"><span>Localização</span><b>Corredor B</b></div>
  <div style="display:flex;justify-content:space-between;font-size:21px;padding:9px 0;border-top:1px solid #e3e3e3"><span>Reservado</span><b>12 un.</b></div>
 </div>
 <div style="position:absolute;z-index:3;right:72px;bottom:52px">{logo_html('#0a0a0a')}</div>
</div>
</div>"""

# ---------- 17 · F7 Checklist + interação · RH ----------
items = [
    "Pedidos de férias perdidos no meio dos e-mails",
    "Faltas apontadas num caderno",
    "Horários num Excel que só uma pessoa percebe",
    "“Quantos dias de férias me faltam?” E ninguém sabe ao certo",
]
rows = "".join(f'<div class="row"><div class="box"></div><p>{t}</p></div>' for t in items)
p17 = f"""{CSS}<div class="post" style="color:#fff">
{foto_bg(F/'post-17'/'01.jpg', 'lateral', pos='70% center', blur=2)}
<div style="position:absolute;inset:0;z-index:2;background:linear-gradient(90deg,rgba(10,10,10,.55) 0%,rgba(10,10,10,.35) 60%,rgba(10,10,10,0) 100%)"></div>
<div style="position:relative;z-index:3;display:flex;justify-content:space-between;align-items:center">
 <span class="tag" style="color:{SKY}">Equipa & RH</span>{logo_html('#fff')}</div>
<div style="position:absolute;z-index:3;left:72px;top:150px;width:660px">
 <h1 style="font-size:74px;text-transform:none;letter-spacing:-2.5px;line-height:1">Quantos destes<br>acontecem<br>na <span style="color:{SKY}">tua empresa?</span></h1>
 <div style="margin-top:30px">{rows}</div>
 <div style="margin-top:34px;display:inline-block;background:{SKY};color:#0a0a0a;font-weight:900;font-size:34px;padding:14px 24px;border-radius:14px">Comenta com o número ↓</div>
</div>
</div>"""

# ---------- 18 · F14 Notificação · web e mobile sem instalações (CTA completo) ----------
p18 = f"""{CSS}<div class="post" style="color:#fff">
{foto_bg(F/'post-18'/'04.jpg', 'azul', blur=3)}
<div style="position:relative;z-index:3;display:flex;justify-content:space-between;align-items:center">
 {logo_html('#fff')}<span class="tag" style="color:#dfe6ff">sexta · 10:02</span></div>
<div style="position:absolute;z-index:3;left:150px;right:150px;top:140px">
 <div class="ntf"><div class="h"><span><span class="ic" style="background:{BLUE}"></span><b>Equipa · Obra</b></span><span>agora</span></div>
  <p>O cliente quer saber o preço. O programa abre aqui no telemóvel?</p></div>
 <div class="ntf" style="margin-top:18px;margin-left:60px;margin-right:-40px"><div class="h"><span><span class="ic" style="background:#0a0a0a"></span><b>Escritório</b></span><span>agora</span></div>
  <p>Só no PC do escritório 😬 Liga-lhe quando voltares.</p></div>
</div>
<div style="position:absolute;z-index:3;left:72px;right:72px;bottom:180px">
 <h1 style="font-size:70px;text-transform:none;letter-spacing:-2.5px;line-height:1.16">O trabalho sai<br>do escritório.<br><span style="color:#0a0a0a;background:#fff;padding:0 12px;-webkit-box-decoration-break:clone;box-decoration-break:clone">O programa também devia.</span></h1>
</div>
{footer('#fff', '#fff', BLUE)}
</div>"""

render({
    "post-16-stocks-antes-depois": p16,
    "post-17-rh-checklist": p17,
    "post-18-sem-instalacoes-notificacao": p18,
}, OUT)
