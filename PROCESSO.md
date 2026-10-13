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

2. **Escolher 3 temas**
   - Lê `marca/base.md` (identidade, factos, regras) e `historico.md` (o que já saiu).
   - Escolhe 3 temas que não repitam o histórico, um por serviço diferente sempre que possível.
   - Regras: nunca nomear projetos nem clientes; usar só os factos confirmados em `marca/base.md`; tratar por "tu" (LinkedIn institucional).
   - Fundos: seg escuro (#0a0a0a com grão), qua claro (#ECECE8 amarrotado), sex azul (#103CE7, acento preto).

3. **Gerar imagens**
   - Copia `scripts/semana06.py` para `scripts/semanaNN.py` (NN = número da semana, continua a numeração do histórico) e reescreve títulos, subtítulos e o objeto herói de cada publicação.
   - Numeração das publicações continua a partir do histórico (a semana 6 terminou na 15).
   - `python3 scripts/semanaNN.py` → `imagens/semana-NN/post-XX-tema.png`.
   - **Abre cada PNG e verifica**: título sem sobreposições nem quebras estranhas, nada cortado, logótipo visível, rodapé intacto. Corrige e volta a gerar até estar limpo.

4. **Descrições** em `imagens/semana-NN/descricoes.json` (mesmo formato da semana 6):
   - Instagram: "👉 Pede a tua proposta gratuita: link na bio" + telefone + ~7 hashtags.
   - Facebook: link direto https://mldev.pt/contactos + telefone + 2 hashtags.
   - LinkedIn: tom institucional, contexto para empresas, link + telefone, exatamente 5 hashtags.
   - Telefone sempre: "+351 231 109 068 (chamada para a rede fixa nacional)".
   - altText descritivo em cada imagem.

5. **GitHub**: `git add -A && git commit && git push` para `main`. Confirma que
   `https://raw.githubusercontent.com/mauroloureiro/mldev-redes-sociais/main/imagens/semana-NN/<ficheiro>.png` devolve 200.

6. **Buffer** (`create_post`, `mode: customScheduled`, `schedulingType: automatic`, `dueAt` com o offset de Lisboa na data: +00:00 no inverno, +01:00 no verão):
   - Instagram `6ace4da0778b240e2ff8b77a` — metadata `{"instagram": {"type": "post", "shouldShareToFeed": true}}`
   - Facebook `6ace4dca778b240e2ff8b943` — metadata `{"facebook": {"type": "post"}}`
   - LinkedIn `6ace4def778b240e2ff8ba85` — sem metadata
   - Confirma com `list_posts` que ficaram 9 agendadas.

7. **Fecho**: acrescenta a semana a `historico.md`, faz commit e push, e envia ao Mauro um resumo curto com os 3 títulos, datas e as imagens.

Se algum passo falhar (sem acesso ao GitHub ou ao Buffer, limite atingido), não publiques nada a meio: avisa o Mauro com o motivo.
