# Processo semanal automático — publicações MLDEV

Corre todas as segundas-feiras às 07:45 (Lisboa) como tarefa agendada do Claude.
Gera as 3 publicações **dessa semana** (seg, qua e sex às 10:00, hora de Lisboa) e agenda-as no Buffer.

Porquê na própria semana: o plano gratuito do Buffer só aceita 10 publicações em fila.
Na segunda de manhã a semana anterior já saiu toda, por isso há espaço para as 9 novas.

## Passos

1. **Verificações iniciais**
   - Se a data de hoje for anterior a 2026-11-16, termina sem fazer nada (as semanas até 13/11 já estão tratadas).
   - Buffer `list_posts` (org `6ace4d5f973519dbf3844c5c`, status scheduled, dueAt entre hoje 00:00 e domingo 23:59).
     Se já existirem publicações agendadas para esta semana, termina e avisa (não duplicar).
   - Conta todas as publicações em fila. Se 9 novas ultrapassarem o limite de 10, avisa o Mauro e termina.

2. **Escolher 3 temas e 3 formatos**
   - Lê `marca/base.md` (identidade, factos, regras), `marca/formatos.md` (catálogo e **regras de variedade — obrigatórias**) e `historico.md` (temas e formatos já usados).
   - Escolhe 3 temas que não repitam o histórico, um por serviço diferente sempre que possível.
   - Escolhe 3 formatos **diferentes entre si e diferentes dos da semana anterior**, cumprindo as regras de `marca/formatos.md` (F1 objeto herói no máximo 1 vez a cada 2 semanas, carrossel pelo menos 1 vez a cada 2 semanas, 1 publicação de interação por semana, CTA completo no rodapé em no máximo 1 imagem).
   - Varia também fundo, composição e cor de uma publicação para a outra. O objetivo é que o feed não pareça repetitivo.
   - Regras: nunca nomear projetos nem clientes; usar só os factos confirmados em `marca/base.md`; tratar por "tu" (LinkedIn institucional).

3. **Gerar imagens**
   - Cria `scripts/semanaNN.py` (NN = número da semana). Usa `scripts/kit.py` para fontes, logótipo, texturas e `render()`; exemplos técnicos: `scripts/semana06.py` (F9 conversa, F2 carrossel, F6 pergunta) e `scripts/exemplo_f1.py` (F1 objeto herói). **Não copies os layouts** — desenha cada publicação de raiz segundo o formato escolhido.
   - Numeração das publicações continua a partir do histórico. Carrosséis: um PNG por slide (`post-XX-tema-1.png`, `-2.png`, …).
   - `python3 scripts/semanaNN.py` → `imagens/semana-NN/`.
   - **Abre cada PNG e verifica**: sem sobreposições nem quebras estranhas, nada cortado, logótipo visível, legível no telemóvel. Verifica também que as 3 publicações parecem claramente diferentes entre si e das últimas 6. Corrige e volta a gerar até estar limpo.

4. **Descrições** em `imagens/semana-NN/descricoes.json` (mesma estrutura JSON da semana 6, mas texto variado — ver regra 9 de `marca/formatos.md`):
   - Instagram: CTA com "link na bio" (redação variável) + telefone + ~7 hashtags.
   - Facebook: link direto https://mldev.pt/contactos + telefone + 2 hashtags.
   - LinkedIn: tom institucional, contexto para empresas, link + telefone, exatamente 5 hashtags.
   - Telefone sempre: "+351 231 109 068 (chamada para a rede fixa nacional)".
   - altText descritivo em cada imagem.

5. **GitHub**: `git add -A && git commit && git push` para `main`. Confirma que
   `https://raw.githubusercontent.com/mauroloureiro/mldev-redes-sociais/main/imagens/semana-NN/<ficheiro>.png` devolve 200.

6. **Buffer** (`create_post`, `mode: customScheduled`, `schedulingType: automatic`, `dueAt` com o offset de Lisboa na data: +00:00 no inverno, +01:00 no verão):
   - Instagram `6ace4da0778b240e2ff8b77a` — metadata `{"instagram": {"type": "post", "shouldShareToFeed": true}}` (carrossel: ver `marca/formatos.md`)
   - Facebook `6ace4dca778b240e2ff8b943` — metadata `{"facebook": {"type": "post"}}`
   - LinkedIn `6ace4def778b240e2ff8ba85` — sem metadata
   - Confirma com `list_posts` que ficaram 9 agendadas.

7. **Fecho**: acrescenta a semana a `historico.md` com o tema **e o formato** (código F) de cada publicação, faz commit e push, e envia ao Mauro um resumo curto com os 3 títulos, datas e as imagens.

Se algum passo falhar (sem acesso ao GitHub ou ao Buffer, limite atingido), não publiques nada a meio: avisa o Mauro com o motivo.
