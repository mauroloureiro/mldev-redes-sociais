# Catálogo de formatos — variar sempre

O Mauro não quer publicações monótonas. O modelo "título grande + objeto herói + rodapé" (usado nas semanas 1 a 6) é **só um** dos formatos, não o padrão.

## Regras de variedade (obrigatórias)
1. **3 formatos diferentes por semana.** Nunca dois iguais na mesma semana.
2. **Não repetir** nenhum formato usado na semana anterior (ver coluna "formato" em `historico.md`).
3. **"Objeto herói" (F1) no máximo 1 vez a cada 2 semanas.** Já foi usado em excesso.
4. **Pelo menos 1 carrossel (F2) a cada 2 semanas.**
5. **Pelo menos 1 publicação de interação por semana** (pergunta, sondagem, "comenta", "guarda para depois").
6. **Variar a composição**: posição do título (topo, centro, fundo, vertical), tamanho, alinhamento, uso de cor. Não usar a mesma grelha duas vezes seguidas.
7. **Cores**: além do preto, papel claro e azul #103CE7, usar também navy #172041 e azul-claro #4EC2F9 como fundo de vez em quando. Nunca o mesmo fundo em duas publicações seguidas.
8. **Rodapé com CTA completo** (botão + mldev.pt/contactos + telefone) em **no máximo 1 publicação por semana**. Nas outras: só o logótipo e, quando muito, "mldev.pt" discreto. O CTA vai na descrição.
9. **Descrições também variam**: abrir de formas diferentes (pergunta, número, frase curta, história de um dia de trabalho, afirmação polémica); não começar sempre por repetir o título; variar o CTA final ("Fala connosco", "Pede proposta", "Envia-nos mensagem", "Comenta X") e a quantidade de emojis.
10. Antes de gerar, compara os 3 rascunhos com as últimas 6 publicações do histórico. Se parecerem da mesma família, muda.

## Formatos
| Código | Formato | Ideia |
|---|---|---|
| F1 | Objeto herói | Título grande + elemento de interface desenhado (telemóvel, browser, terminal…). |
| F2 | Carrossel educativo (4–6 slides) | Capa com gancho → 1 ideia por slide → último slide com CTA. Ex.: "5 sinais de que já precisas de um ERP". |
| F3 | Tipografia pura | Só uma frase ou número gigante, sem objeto. Ex.: "98%" com "dos clientes satisfeitos" pequeno. |
| F4 | Mito vs Realidade | Ecrã dividido ou riscado: "Mito: um site é para sempre." / "Realidade: …". |
| F5 | Antes / Depois | Duas metades: o caos (Excel, papéis, e-mails) vs a solução organizada. |
| F6 | Pergunta / sondagem | Pergunta grande com opções A/B/C para responderem nos comentários. |
| F7 | Checklist / dicas rápidas | Lista com visto: "Antes de lançares o teu site, confirma:". Bom para guardar. |
| F8 | Glossário | Estilo dicionário: "ERP (n.)", pronúncia/definição simples, exemplo. |
| F9 | Conversa | Bolhas de chat ou e-mail entre "cliente" e "MLDEV" (fictício, sem nomes reais). |
| F10 | Bastidores / processo | Uma fase do processo em detalhe (ex.: "o que acontece na Descoberta"), timeline, post-its. |
| F11 | Dados / gráfico | Gráfico simples ou barra de progresso com factos confirmados (prazos, números da empresa). |
| F12 | Frase da marca | Manifesto curto ou slogan "Além do código. Construído com propósito.", tipografia editorial. |
| F13 | Comparação / tabela | "À medida vs pronto-a-usar", "App nativa vs Flutter" — tabela de 2 colunas. |
| F14 | Notificação / meme de escritório | Situação reconhecível do dia a dia de uma PME, com humor leve (sem imagens de terceiros). |

## Carrosséis no Buffer (testado a 15/10/2026, funciona)
- Gerar cada slide como PNG 1080×1080 (`post-XX-tema-1.png`, `-2.png`, …) e passar todos em `assets` pela ordem.
- Instagram: `metadata.instagram.type = "post"` (não existe "carousel") com várias imagens em `assets` → o Buffer publica como carrossel.
- Facebook (`type: "post"`) e LinkedIn: a mesma lista de imagens, pela mesma ordem.
