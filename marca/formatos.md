# Catálogo de formatos — variar sempre

## Foco no cliente e fotografias (pedido do Mauro, 15/11/2026 — obrigatório)
**A mensagem.** Cada publicação parte de uma situação/dor que o cliente reconhece no seu dia a dia e mostra que o serviço da MLDEV resolve isso. O objetivo é o leitor pensar "isto acontece-me, preciso disto".
- Começa pelo problema, não pelo serviço: "Ainda a fechar o mês no Excel?", "O cliente ligou e ninguém sabia em que ponto estava a encomenda.", "O site está bonito, mas o telefone não toca."
- Depois a consequência (tempo, dinheiro, clientes perdidos, stress) e por fim a solução MLDEV numa frase. O título fala da dor; a solução vai no subtítulo, no último slide ou na descrição.
- Nada de números inventados: só factos de `base.md`. Para quantificar a dor, usa perguntas ("Quantas horas por semana…?") em vez de estatísticas.
- Público: donos e gestores de PME (comércio, indústria, serviços, armazém, escritório).

**As imagens.** Estilo aprovado pelo Mauro a 15/11/2026 (exemplos: foto escurecida em baixo com título grande; texto à esquerda e foto à direita; foto em tom azul com frase em caixa branca). Pelo menos **2 das 3 publicações por semana** têm fotografia de fundo (num carrossel basta a capa e o último slide; os do meio podem ser lisos).
- A foto tem de ter a ver com o contexto da publicação (ex.: papéis e Excel → secretária cheia de papéis; armazém/stock → prateleiras e caixas; site que não vende → pessoa a ver o telemóvel; suporte → servidor/portátil à noite; consultoria → reunião). Sem fotos genéricas "bonitas" sem relação com o tema.
- **O texto manda, a foto é contexto**: usar sempre `foto_bg()` de `scripts/kit.py` (foto escurecida/dessaturada + camada da marca). Estilos: `escuro`, `navy`, `azul`, `lateral` (texto à esquerda), `base` (texto em baixo). Variar o estilo entre publicações.
- Títulos grandes (≥ 72 px), brancos ou azul-claro #4EC2F9 / caixa branca com texto preto; nunca texto fino sobre zonas claras da foto. Se ao verificar o PNG alguma palavra se confundir com a foto, escurece mais (outro estilo ou blur) ou troca de foto.
- Evitar fotos com texto, logótipos ou marcas visíveis, ecrãs com software de terceiros reconhecível, e caras em grande plano a olhar para a câmara (parece banco de imagens). Mãos, costas, secretárias, ambientes de trabalho funcionam melhor.
- Fonte: pedidos em `fotos/pedidos.json` → GitHub Actions procura no Pixabay e grava candidatas em `fotos/candidatas/` (ver `PROCESSO.md`). Licenças livres para uso comercial. Não repetir fotos (`fotos_usadas.json`).
- Sem fotos aproveitáveis: `marca/fotos/` (se tiver) e, em último caso, fundo da marca sem foto — e avisar o Mauro.
- Os formatos abaixo continuam válidos — a fotografia é o fundo, o formato é a composição (ex.: F6 Pergunta com foto, F4 Mito vs Realidade com foto em metade do ecrã, F2 Carrossel com foto na capa).

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
10. O fundo com fotografia conta como fundo: não usar o mesmo estilo de `foto_bg()` em duas publicações seguidas.
11. Antes de gerar, compara os 3 rascunhos com as últimas 6 publicações do histórico. Se parecerem da mesma família, muda.

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

## Carrosséis (histórico: no Buffer, testado a 15/10/2026; desde 01/11/2026 o ERP publica o carrossel a partir da lista `images`)
- Gerar cada slide como PNG 1080×1080 (`post-XX-tema-1.png`, `-2.png`, …) e passar todos em `assets` pela ordem.
- Instagram: `metadata.instagram.type = "post"` (não existe "carousel") com várias imagens em `assets` → o Buffer publica como carrossel.
- Facebook (`type: "post"`) e LinkedIn: a mesma lista de imagens, pela mesma ordem.
