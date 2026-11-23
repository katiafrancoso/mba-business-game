# 01 — Comandos do harness

Basta digitar o comando (ou algo equivalente em linguagem natural) em qualquer conversa do Projeto. Cada comando define **o que ler**, **o que fazer** e **o que salvar**.

| Comando | Para quê |
|---|---|
| `/status` | Fotografia rápida: trimestre, caixa, estoque, pendências e próximo passo |
| `/nova-rodada Tn` | Gera as recomendações completas dos agentes para o trimestre n |
| `/agente <nome> Tn` | Roda só um agente (mercado, operacoes, tecnologia, financas, competitiva, ceo) |
| `/simular Tn <variações>` | Roda cenários de caixa e DRE com o modelo |
| `/registrar-decisao Tn` | Grava o que a equipe decidiu de fato |
| `/pos-rodada Tn` | Analisa os relatórios do trimestre processado e atualiza o estado |
| `/pergunta-instrutor` | Adiciona ou atualiza dúvidas para o professor |
| `/regra <tema>` | Responde dúvidas sobre as regras do jogo citando a base |
| `/atualizar-kb` | Corrige ou acrescenta informação na base de conhecimento |
| `/ata` | Registra o resumo de uma reunião da equipe |
| `/entregavel <formato>` | Gera um material para o grupo (PDF ou PowerPoint) a partir do estado atual |
| `/publicar` | Publica uma nova versão no GitHub (também roda automaticamente ao final dos demais comandos que salvam algo) |

---

## `/status`
- **Ler:** `harness/00` (seção Status), `08_estado_atual_equipe3.md`, `registro/decisoes_log.md`, `registro/perguntas_instrutor.md`.
- **Fazer:** responder em até 10 linhas: trimestre, caixa, estoque, dívida, versão, última decisão, pendências e próximo comando.
- **Salvar:** nada.

## `/nova-rodada Tn`
- **Ler:** toda a `base-conhecimento/`, `registro/licoes_aprendidas.md`, `rodadas/T(n-1)/` (incluindo o `_99_POS_RODADA`).
- **Fazer:** executar, nesta ordem:
  1. Inteligência Competitiva (05) e Mercado (01).
  2. Tecnologia (03).
  3. Operações (02), que usa a demanda do 01.
  4. Finanças (04), que usa todos e roda o modelo `04_modelo_simulacao.py`.
  5. CEO (00), que consolida e aplica o checklist do doc 10.
- **Salvar:** `rodadas/Tn/Tn_00..05_*.md` (templates no `02_TEMPLATES.md`); atualizar o Status no `harness/00`; linha no `changelog_kb.md`.

## `/agente <nome> Tn`
- **Ler:** os docs da área (ver `base-conhecimento/09_arquitetura_agentes.md`) e o `08_estado`.
- **Salvar:** sobrescrever **apenas** o arquivo do agente em `rodadas/Tn/`. Se o resultado mudar a recomendação final, avisar que o CEO (00) precisa ser rodado de novo.

## `/simular Tn <variações>`
- **Fazer:** ajustar os parâmetros em `04_modelo_simulacao.py` (preço, vendedores, produção, % à vista, empréstimo etc.) e mostrar uma tabela comparativa de cenários.
- **Salvar:** só se a equipe pedir. Nesse caso, acrescentar a seção "Simulações adicionais" no `rodadas/Tn/Tn_04_agente_financas.md`.

## `/registrar-decisao Tn`
- **Entrada:** as decisões finais da equipe. O usuário cola os valores ou diz "igual à recomendação, exceto X".
- **Fazer:** montar a tabela por tela do simulador e listar as **divergências em relação à recomendação**, com o motivo.
- **Salvar:** `rodadas/Tn/Tn_90_DECISAO_TOMADA.md` e uma nova entrada em `registro/decisoes_log.md`; atualizar o Status no `harness/00`.

## `/pos-rodada Tn`
- **Entrada:** os relatórios do trimestre processado. A IA pode lê-los no simulador (aba ANÁLISE, só leitura) se o navegador estiver disponível; senão, o usuário anexa os PDFs.
- **Fazer:**
  1. Extrair DRE, Balanço, Caixa, Operações, Logística e Resumo financeiro.
  2. Indicadores de Mercado: tabela das 8 equipes (preço, vendedores, versão, share, ROE, endividamento).
  3. Comparar **previsto × realizado** (vendas, receita, caixa, custos) e explicar os desvios.
  4. Extrair **lições** sobre como o simulador reage (elasticidades, efeito dos vendedores e da propaganda, falta de produto etc.).
- **Salvar:** nova sessão em `registro/log_acesso_simulador.md` (se o navegador foi usado); `rodadas/Tn/Tn_99_POS_RODADA.md`; **reescrever** o `base-conhecimento/08_estado_atual_equipe3.md` (situação nova, histórico acrescido); novas lições em `registro/licoes_aprendidas.md`; correções de parâmetros nos docs 03, 05 e 07 se algum [observado] mudar; linha no `changelog_kb.md`.

## `/pergunta-instrutor`
- **Salvar:** `registro/perguntas_instrutor.md`. Abrir uma pergunta nova ou registrar a resposta recebida; se a resposta mudar uma regra, propagar para a base e anotar no changelog.

## `/regra <tema>`
- **Fazer:** responder citando o documento e a seção (por exemplo, "doc 05 §4"). Se a base não tiver a resposta, dizer isso e sugerir `/pergunta-instrutor`.
- **Salvar:** nada, a não ser que se descubra uma lacuna na base (nesse caso, `/atualizar-kb`).

## `/atualizar-kb`
- **Fazer:** ler o doc inteiro, aplicar a mudança e salvar o doc completo no mesmo caminho.
- **Salvar:** o doc alterado e uma linha no `changelog_kb.md` (o quê, por quê, fonte).

## `/ata`
- **Salvar:** `rodadas/Tn/Tn_80_ATA_REUNIAO.md` (participantes, decisões, divergências, responsáveis, prazos).

## `/entregavel <formato>`
- **Formato:** `pdf` (documento explicativo) ou `pptx` (apresentação). Se não for informado, perguntar.
- **Ler:** `harness/00` (status), o `rodadas/Tn/Tn_00` mais recente, `registro/decisoes_log.md`.
- **Fazer:** atualizar o material existente em vez de criar outro do zero. Linguagem para quem não acompanhou o chat: o que foi feito, os agentes, as recomendações e os próximos passos. Conferir visualmente cada página ou slide antes de entregar.
- **Salvar:** o arquivo e o script gerador em `entregaveis/` no GitHub (binários não cabem no Projeto); linha no `changelog_kb.md`; atualizar "Entregáveis prontos" no `harness/00`.

## `/publicar`
- **Quando:** ao final de **todo** comando que salvou algo no Projeto, ou quando o usuário pedir.
- **Fazer:**
  1. Conectar o repositório `katiafrancoso/mba-business-game` com acesso de escrita.
  2. Clonar e espelhar os documentos alterados do Projeto nas mesmas pastas (`claude/README.md` do Projeto vai para `README.md` na raiz).
  3. Atualizar o `README.md` se necessário.
  4. Commit no formato `tipo(escopo): descrição` e push na `main`.
  5. Ao fechar um trimestre, criar a tag `T{n}-fechado`.
- **Salvar:** linha no `registro/changelog_kb.md` citando o commit; atualizar a linha "GitHub" do Status no `harness/00`.
