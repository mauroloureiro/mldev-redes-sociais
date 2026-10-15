"""Exemplo do formato F1 (objeto herói): versão original da semana 6, substituída por formatos variados.
Correr: python3 scripts/exemplo_f1.py  -> imagens/exemplos/f1/
Referência técnica apenas; não copiar o layout.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from kit import *

# ---------- 13 · Modo offline (escuro) ----------
P13 = f"""<div class="post" style="background:#0a0a0a;color:#fff">
<div class="grain" style="background-image:url(&quot;{GRAIN}&quot;)"></div>
<div class="top">{logo_html('#fff')}<div class="tag" style="color:#8a8a8a">Aplicações móveis</div></div>
<h1 style="font-size:90px;margin-top:80px;width:560px">Sem rede?<br>A app<br><span style="color:#2569ED">continua.</span></h1>
<p style="position:relative;z-index:3;margin-top:34px;width:470px;font-size:25px;line-height:1.4;font-weight:500;color:#bdbdbd">No armazém, na estrada ou na cave: a tua equipa continua a trabalhar e tudo sincroniza quando a rede voltar.</p>

<div style="position:absolute;z-index:2;right:70px;top:150px;width:370px;height:740px;border-radius:56px;background:#161616;border:2px solid #2c2c2c;padding:16px;box-shadow:0 40px 80px rgba(0,0,0,.6)">
 <div style="width:100%;height:100%;border-radius:42px;background:#f4f4f2;overflow:hidden;position:relative;color:#111">
  <div style="display:flex;justify-content:space-between;align-items:center;padding:20px 28px 0;font-family:'JB';font-weight:700;font-size:17px">
   <span>10:24</span>
   <span style="display:flex;gap:8px;align-items:center">
    <svg width="26" height="18" viewBox="0 0 26 18"><rect x="1" y="12" width="4" height="5" fill="#bbb"/><rect x="8" y="8" width="4" height="9" fill="#bbb"/><rect x="15" y="4" width="4" height="13" fill="#bbb"/><rect x="22" y="0" width="3" height="17" fill="#bbb"/><path d="M0 18 L26 0" stroke="#e5484d" stroke-width="2.4"/></svg>
    <span style="color:#999">Sem rede</span></span>
  </div>
  <div style="margin:22px 18px 0;background:#111;color:#fff;border-radius:18px;padding:14px 18px;display:flex;gap:12px;align-items:center;font-size:17px;font-weight:700">
   <span style="width:12px;height:12px;border-radius:50%;background:#2569ED;box-shadow:0 0 0 5px rgba(37,105,237,.25)"></span>Modo offline ativo</div>
  <div style="padding:24px 22px 0;font-weight:900;font-size:27px;letter-spacing:-.5px">Encomendas</div>
  {''.join(f'''<div style="margin:12px 18px 0;background:#fff;border-radius:16px;padding:15px 18px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 2px 0 rgba(0,0,0,.05)">
   <div><div style="font-weight:800;font-size:18px">{n}</div><div style="font-size:14px;color:#888;margin-top:3px">{d}</div></div>
   <span style="font-family:'JB';font-weight:700;font-size:13px;padding:6px 10px;border-radius:20px;{s}">{t}</span></div>''' for n,d,t,s in [
     ("Encomenda #2041","12 artigos","GUARDADA","background:#e8eefc;color:#103CE7"),
     ("Encomenda #2042","4 artigos","GUARDADA","background:#e8eefc;color:#103CE7"),
     ("Inventário · A3","38 contagens","GUARDADO","background:#e8eefc;color:#103CE7"),
     ("Encomenda #2040","enviada às 09:58","ENVIADA","background:#eaeaea;color:#555")])}
  <div style="position:absolute;left:18px;right:18px;bottom:22px;border:2px dashed #c9c9c9;border-radius:16px;padding:14px;text-align:center;font-size:15px;font-weight:700;color:#777">
   3 registos à espera de rede · sincroniza sozinho</div>
 </div>
</div>
{footer('#fff', '#2569ED', '#fff')}
</div>"""

# ---------- 14 · CMS (claro) ----------
P14 = f"""<div class="post" style="background:#ECECE8;color:#0a0a0a">
<div class="grain" style="background-image:url(&quot;{CRUMPLE}&quot;)"></div>
<div class="grain" style="background-image:url(&quot;{GRAIN_DARK}&quot;);opacity:.6"></div>
<div class="top">{logo_html('#0a0a0a')}<div class="tag" style="color:#6b6b66">Websites</div></div>
<h1 style="font-size:80px;margin-top:56px">Atualiza<br>o teu site<br><span style="color:#103CE7">sem programador.</span></h1>

<div style="position:absolute;z-index:2;left:72px;right:72px;top:450px;height:400px;background:#fff;border-radius:22px;border:2px solid #0a0a0a;box-shadow:14px 14px 0 #0a0a0a;overflow:hidden">
 <div style="height:58px;border-bottom:2px solid #0a0a0a;display:flex;align-items:center;gap:10px;padding:0 22px">
  <span style="width:14px;height:14px;border-radius:50%;border:2px solid #0a0a0a"></span><span style="width:14px;height:14px;border-radius:50%;border:2px solid #0a0a0a"></span><span style="width:14px;height:14px;border-radius:50%;border:2px solid #0a0a0a"></span>
  <div style="margin-left:18px;flex:1;height:34px;border-radius:17px;background:#f0f0ec;display:flex;align-items:center;padding:0 18px;font-family:'JB';font-size:16px;color:#666">o-teu-site.pt/admin/paginas/inicio</div>
 </div>
 <div style="display:flex;height:340px">
  <div style="width:220px;border-right:2px solid #eee;padding:20px 20px;font-size:18px;font-weight:700;color:#999;line-height:2.1">
   <div>Páginas</div><div style="color:#0a0a0a;background:#f0f0ec;border-radius:10px;padding-left:12px;margin-left:-12px">Início</div><div>Serviços</div><div>Notícias</div><div>Contactos</div></div>
  <div style="flex:1;padding:22px 30px;position:relative">
   <div style="font-family:'JB';font-size:14px;color:#888;letter-spacing:1px">TÍTULO</div>
   <div style="margin-top:8px;border:2px solid #103CE7;border-radius:12px;padding:12px 16px;font-size:24px;font-weight:800">Novo horário a partir de novembro<span style="display:inline-block;width:3px;height:26px;background:#103CE7;vertical-align:middle;margin-left:3px"></span></div>
   <div style="font-family:'JB';font-size:14px;color:#888;letter-spacing:1px;margin-top:20px">TEXTO</div>
   <div style="margin-top:8px;border:2px solid #e3e3df;border-radius:12px;padding:14px 16px;font-size:18px;color:#444;line-height:1.5">Segunda a sexta, das 9h às 18h.<br>Sábados, das 9h às 13h.</div>
   <div style="position:absolute;right:30px;bottom:28px;background:#103CE7;color:#fff;font-weight:800;font-size:21px;padding:16px 30px;border-radius:40px">Publicar</div>
   <svg style="position:absolute;right:42px;bottom:2px" width="38" height="44" viewBox="0 0 24 28"><path d="M2 2 L2 22 L7.5 17 L11 25 L14.5 23.5 L11 15.5 L18 15.5 Z" fill="#0a0a0a" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/></svg>
  </div>
 </div>
</div>
{footer('#0a0a0a', '#0a0a0a', '#fff')}
</div>"""

# ---------- 15 · Backups diários (azul) ----------
rows = [("SÁB","07/11"),("DOM","08/11"),("SEG","09/11"),("TER","10/11"),("QUA","11/11"),("QUI","12/11")]
log = "".join(f'''<div style="display:flex;gap:22px;padding:11px 0;border-bottom:1px dashed rgba(255,255,255,.12)">
 <span style="color:#7f8aa3">{d} {dt}</span><span style="color:#7f8aa3">03:00</span><span style="flex:1;color:#e8ecf5">cópia de segurança</span><span style="color:#4EC2F9;font-weight:700">✓ CONCLUÍDA</span></div>''' for d,dt in rows)
P15 = f"""<div class="post" style="background:#103CE7;color:#fff">
<div class="grain" style="background-image:url(&quot;{GRAIN}&quot;);opacity:.8"></div>
<div class="top">{logo_html('#fff')}<div class="tag" style="color:rgba(255,255,255,.75)">Suporte & manutenção</div></div>
<h1 style="font-size:80px;margin-top:66px">Todos os dias.<br><span style="color:#0a0a0a">Sem te lembrares.</span></h1>

<div style="position:absolute;z-index:2;left:72px;right:72px;top:390px;height:440px;background:#0a0a0a;border-radius:22px;overflow:hidden;box-shadow:0 30px 60px rgba(0,0,0,.35)">
 <div style="height:54px;background:#161616;display:flex;align-items:center;gap:10px;padding:0 22px">
  <span style="width:13px;height:13px;border-radius:50%;background:#3a3a3a"></span><span style="width:13px;height:13px;border-radius:50%;background:#3a3a3a"></span><span style="width:13px;height:13px;border-radius:50%;background:#3a3a3a"></span>
  <span style="margin-left:16px;font-family:'JB';font-size:16px;color:#888">backups.log</span></div>
 <div style="padding:16px 30px;font-family:'JB';font-weight:500;font-size:19px">{log}
  <div style="padding-top:16px;color:#7f8aa3">$ <span style="color:#e8ecf5">próxima cópia: esta noite, 03:00</span><span style="display:inline-block;width:11px;height:20px;background:#4EC2F9;vertical-align:middle;margin-left:6px"></span></div>
 </div>
</div>
{footer('#fff', '#0a0a0a', '#fff')}
</div>"""

POSTS = {"post-13-modo-offline": P13, "post-14-cms": P14, "post-15-backups": P15}


render(POSTS, REPO / "imagens" / "exemplos" / "f1")
