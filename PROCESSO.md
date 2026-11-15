# Processo semanal automático — publicações MLDEV

Corre todas as segundas-feiras às 07:45 (Lisboa) como tarefa agendada do Claude.
Gera as 3 publicações **dessa semana** (seg, qua e sex às 10:00, hora de Lisboa) e entrega-as ao **ERP da MLDEV** (página Marketing).

Desde 01/11/2026 já não se usa o Buffer. O ERP lê `erp/fila.json` deste repositório de hora a hora, descarrega as imagens e agenda
as publicações no calendário: publica sozinho no Facebook e no Instagram e envia à equipa o texto do LinkedIn à hora marcada.
Cada publicação só é importada uma vez (chave `semana-NN/post-XX-…`), por isso nunca se reescreve uma semana já entregue.

## Passos

1. **Verificações iniciais**
   - Se a data de hoje for anterior a 2026-11-16, termina sem fazer nada (as semanas até 13/11 já estão tratadas).
   - Lê `erp/fila.json`. Se a semana desta segunda já lá estiver (ou já existir `imagens/semana-NN/descricoes.json` com datas desta semana), termina e avisa (não duplicar).
   - Não uses o Buffer (nem para consultar nem para agendar).

2. **Escolher 3 temas e 3 formatos**
   - Lê `marca/base.md` (identidade, factos, regras), `marca/formatos.md` (catálogo e **regras de variedade — obrigatórias**) e `historico.md` (temas e formatos já usados).
   - Escolhe 3 temas que não repitam o histórico, um por serviço diferente sempre que possível.
   - Escolhe 3 formatos **diferentes entre si e diferentes dos da semana anterior**, cumprindo as regras de `marca/formatos.md` (F1 objeto herói no máximo 1 vez a cada 2 semanas, carrossel pelo menos 1 vez a cada 2 semanas, 1 publicação de interação por semana, CTA completo no rodapé em no máximo 1 imagem).
   - Varia também fundo, composição e cor de uma publicação para a outra. O objetivo é que o feed não pareça repetitivo.
   - **Foco no cliente** (obrigatório desde 16/11/2026): cada publicação parte de uma dor/situação real de uma PME e mostra o serviço como solução. Ver `marca/formatos.md` → "Foco no cliente e fotografias".
   - Regras: nunca nomear projetos nem clientes; usar só os factos confirmados em `marca/base.md`; tratar por "tu" (LinkedIn institucional).

3. **Gerar imagens**
   - Cria `scripts/semanaNN.py` (NN = número da semana). Usa `scripts/kit.py` para fontes, logótipo, texturas e `render()`; exemplos técnicos: `scripts/semana06.py` (F9 conversa, F2 carrossel, F6 pergunta) e `scripts/exemplo_f1.py` (F1 objeto herói). **Não copies os layouts** — desenha cada publicação de raiz segundo o formato escolhido.
   - **Fotografias**: pelo menos 2 das 3 publicações com foto de fundo ligada ao tema, via `scripts/fotos.py` (`foto(...)`) e `foto_bg(...)` de `kit.py`; exemplo técnico em `scripts/exemplo_foto.py`. Abre cada foto antes de a usar e confirma que tem a ver com o tema. A chave do Pexels vem da variável `PEXELS_API_KEY` (nunca escrever a chave no repositório). Faz commit de `fotos_usadas.json`.
   - Numeração das publicações continua a partir do histórico. Carrosséis: um PNG por slide (`post-XX-tema-1.png`, `-2.png`, …).
   - `python3 scripts/semanaNN.py` → `imagens/semana-NN/`.
   - **Abre cada PNG e verifica**: sem sobreposições nem quebras estranhas, nada cortado, logótipo visível, legível no telemóvel, **texto claramente mais destacado do que a foto** (nenhuma palavra se perde no fundo). Verifica também que as 3 publicações parecem claramente diferentes entre si e das últimas 6. Corrige e volta a gerar até estar limpo.

4. **Descrições** em `imagens/semana-NN/descricoes.json` (mesma estrutura JSON da semana 6, mas texto variado — ver regra 9 de `marca/formatos.md`).
   O ERP lê este ficheiro tal como está, por isso cada publicação tem de ter: `titulo`, `tema`, `formato`, `date` (ISO com o offset de Lisboa: +00:00 no inverno, +01:00 no verão, sempre às 10:00 de Lisboa), `images` (nomes dos PNG da pasta, pela ordem do carrossel), `alt`/`alts`, `instagram`, `facebook`, `linkedin`.
   - Instagram: CTA com "link na bio" (redação variável) + telefone + ~7 hashtags.
   - Facebook: link direto https://mldev.pt/contactos + telefone + 2 hashtags.
   - LinkedIn: tom institucional, contexto para empresas, link + telefone, exatamente 5 hashtags.
   - Telefone sempre: "+351 231 109 068 (chamada para a rede fixa nacional)".
   - altText descritivo em cada imagem (inclui o que a foto mostra).
   - Abre as descrições pela dor do cliente (pergunta ou situação do dia a dia), depois a solução — sem repetir o título palavra por palavra.

5. **GitHub**: `git add -A && git commit && git push` para `main`. Confirma que
   `https://raw.githubusercontent.com/mauroloureiro/mldev-redes-sociais/main/imagens/semana-NN/<ficheiro>.png` e `…/semana-NN/descricoes.json` devolvem 200.

6. **Entregar ao ERP** (só depois do passo 5 estar confirmado): acrescenta `"semana-NN"` ao fim da lista `semanas` em `erp/fila.json`, faz commit e push.
   Confirma que `https://raw.githubusercontent.com/mauroloureiro/mldev-redes-sociais/main/erp/fila.json` já mostra a semana nova.
   O ERP importa dentro de 1 hora; as publicações aparecem no calendário da página Marketing como "Agendado".

7. **Fecho**: acrescenta a semana a `historico.md` com o tema **e o formato** (código F) de cada publicação, faz commit e push, e envia ao Mauro um resumo curto com os 3 títulos, datas e as imagens, com a nota de que pode alterar ou apagar as publicações no ERP (Marketing) até à hora de saída.

Se algum passo falhar (sem acesso ao GitHub, imagens com erro), não acrescentes a semana a `erp/fila.json`: avisa o Mauro com o motivo.
