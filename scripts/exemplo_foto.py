"""Exemplo técnico: publicação com fotografia de fundo (foco na dor do cliente).
Não copiar o layout — serve só para mostrar foto_bg() e a hierarquia texto > imagem.
Uso: python3 scripts/exemplo_foto.py <foto.jpg> <pasta_saida>
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from kit import *

foto, out = sys.argv[1], sys.argv[2]
SKY = "#4EC2F9"

A = f"""<div class="post" style="color:#fff">
{foto_bg(foto, "base")}
<div class="top"><span class="tag" style="color:#cfd6ff">Software de gestão</span>{logo_html('#fff')}</div>
<div style="position:absolute;z-index:3;left:72px;right:72px;bottom:70px">
 <div class="tag" style="color:{SKY};margin-bottom:22px">sexta-feira, 18:47</div>
 <h1 style="font-size:96px">Ainda a fechar<br>o mês <span style="color:{SKY}">no Excel?</span></h1>
 <p style="font-size:32px;font-weight:600;line-height:1.35;margin-top:28px;max-width:820px;color:#e8ecff">Um sistema à medida faz as contas por ti. Tu vais para casa.</p>
</div></div>"""

B = f"""<div class="post" style="color:#fff">
{foto_bg(foto, "lateral")}
<div style="position:relative;z-index:3;height:100%;display:flex;flex-direction:column;justify-content:center;max-width:640px">
 <div style="font-family:'JB';font-weight:700;font-size:120px;line-height:1;color:{SKY}">?h</div>
 <div style="font-weight:900;font-size:58px;line-height:1.02;letter-spacing:-2px;margin-top:10px">Quantas horas por semana perdes à procura de encomendas no <span style="white-space:nowrap">e-mail</span>?</div>
 <div style="font-size:28px;font-weight:600;margin-top:26px;color:#d7dcf0">Num sistema, estão todas num só sítio.</div>
</div>
<div style="position:absolute;z-index:3;left:72px;bottom:60px">{logo_html('#fff')}</div></div>"""

C = f"""<div class="post" style="color:#fff;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">
{foto_bg(foto, "azul", blur=2)}
<h1 style="font-size:88px;text-transform:none;letter-spacing:-3px;line-height:1.14">O cliente ligou.<br>Ninguém sabia<br><span style="color:#0a0a0a;background:#fff;padding:0 14px;-webkit-box-decoration-break:clone;box-decoration-break:clone">em que ponto estava.</span></h1>
<div style="position:absolute;z-index:3;bottom:60px">{logo_html('#fff')}</div></div>"""

render({"exemplo-foto-base": A, "exemplo-foto-lateral": B, "exemplo-foto-azul": C}, out)
