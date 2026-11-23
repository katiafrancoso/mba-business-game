# HARNESS do Projeto "Business Game": leia primeiro

> O harness é a **camada de operação** do projeto: define **como** qualquer conversa (de qualquer membro da equipe, em qualquer dispositivo) usa a base de conhecimento, aciona os agentes e **salva tudo de volta**. Assim nada se perde entre conversas.

## 1. Estrutura do Projeto (espelhada no GitHub)
```
harness/                       ← como operar (este conjunto de arquivos)
  00_HARNESS_LEIA_PRIMEIRO.md    regras de ouro, estrutura e fluxo
  01_COMANDOS.md                 comandos padronizados (/status, /nova-rodada, ...)
  02_TEMPLATES.md                formatos obrigatórios das saídas
  03_PROTOCOLO_PERSISTENCIA.md   o que salvar, onde, com que nome e quando
  04_modelo_simulacao.py         modelo de caixa e DRE (reutilizável)
  INSTRUCOES_DO_PROJETO.md       texto para colar nas instruções do Projeto no claude.ai
base-conhecimento/             ← regras do jogo e estado (fonte da verdade)
  00_INDICE.md ... 10_checklist_rodada_e_armadilhas.md
rodadas/                       ← uma pasta por trimestre
  T2/ T2_00_RECOMENDACAO_FINAL_CEO.md, T2_01..05 agentes, (depois) T2_90_DECISAO_TOMADA.md, T2_99_POS_RODADA.md
registro/                      ← memória viva do projeto
  decisoes_log.md                o que foi efetivamente decidido em cada trimestre
  perguntas_instrutor.md         dúvidas abertas e respostas do professor
  licoes_aprendidas.md           o que aprendemos sobre o simulador (calibração)
  changelog_kb.md                histórico de alterações da base
docs/                          ← textos de vitrine (arquitetura dos agentes, método da base)
claude/README.md               ← README de portfólio (no GitHub fica na raiz: README.md)
entregaveis/                   ← SÓ NO GITHUB: PDF, PowerPoint e os scripts que os geram
```
> Arquivos binários (PDF, PPTX) não cabem nos documentos do Projeto: eles vivem apenas em `entregaveis/` no GitHub.

## 2. Regras de ouro (valem para qualquer conversa)
1. **Ler antes de responder.** Comece por `harness/00`, `base-conhecimento/08_estado_atual_equipe3.md` e `registro/decisoes_log.md`. Para perguntas sobre regras, consulte os docs 01–07.
2. **Fonte da verdade:** o manual e os relatórios do simulador. Toda inferência é marcada como **[análise]** ou **[premissa]**; todo valor visto no simulador, como **[observado]**.
3. **Os agentes recomendam, a equipe decide.** Ninguém (humano ou IA) salva decisões no simulador a partir de uma recomendação sem a revisão da equipe. A IA **nunca** clica em Salvar ou enviar no simulador.
4. **Tudo que for durável é salvo no Projeto** seguindo o `03_PROTOCOLO_PERSISTENCIA.md`. Uma conversa sem registro é uma conversa perdida.
5. **Toda alteração na base gera uma linha no `registro/changelog_kb.md`.**
6. **Números vêm de cálculo, não de estimativa de cabeça:** use o `04_modelo_simulacao.py` ou a tela Projeções do simulador.
7. **Português, tabelas e objetividade.** Cada recomendação traz valor exato, justificativa, impacto no caixa e no lucro, e risco.
8. **Toda evolução do projeto vira uma nova versão no GitHub** (https://github.com/katiafrancoso/mba-business-game), espelhando o Projeto. Regras em `03_PROTOCOLO_PERSISTENCIA.md`.

## 3. Ciclo de vida de um trimestre
```
[1] /pos-rodada T(n-1)      → lê os relatórios processados, gera T(n-1)_99_POS_RODADA, atualiza 08_estado e licoes
[2] /nova-rodada Tn         → roda os agentes 01–05 e o CEO 00 em rodadas/Tn/
[3] reunião da equipe       → discute os "pontos de decisão"
[4] /registrar-decisao Tn   → grava Tn_90_DECISAO_TOMADA + decisoes_log
[5] equipe preenche e salva no simulador (confere PROJEÇÕES e CONCLUA)
[6] professor processa      → volta para [1]
```

## 4. Status atual (atualizar a cada etapa)
> Última atualização: **23/11/2026**

| Item | Situação |
|---|---|
| Trimestre atual | **T2**: recomendações geradas em 22/11/2026; decisão da equipe **pendente** |
| Próximo comando esperado | `/registrar-decisao T2` (após a reunião) |
| Pendências críticas | Pedir ao instrutor o limite de empréstimo de longo prazo (R$ 100 mil) e o critério de avaliação (ver `registro/perguntas_instrutor.md`); prazo de entrega do T2 ainda não informado |
| Configuração pendente | Colar `harness/INSTRUCOES_DO_PROJETO.md` nas instruções do Projeto no claude.ai; descrição e tópicos do repositório no GitHub (manual) |
| Entregáveis prontos | `entregaveis/Projeto_Agentico_Business_Game_Equipe3.pdf` (9 págs.) e `.pptx` (6 slides, versão resumida) |
| GitHub | https://github.com/katiafrancoso/mba-business-game · branch `main` · última versão em 23/11/2026 |
| Melhoria oferecida, não feita | Análise competitiva por praça (como as 7 equipes podem se distribuir entre as praças) para refinar a alocação de vendedores e propaganda do T2 |
| Decisões em aberto da equipe | Repositório em dois idiomas (PT/EN): aguardando decisão |

## 5. Limitações conhecidas do sistema
- O modelo não calcula a participação de mercado a partir das decisões (preço, vendedores, propaganda versus os 7 concorrentes). Os cenários fixam 10%, 12,5% ou 14% do mercado. **Calibrar com o resultado do T2** e registrar em `registro/licoes_aprendidas.md`.
- Não se sabe se a demanda não atendida de um concorrente migra para outra equipe (ver `registro/perguntas_instrutor.md`).
- O acesso ao simulador é feito pela extensão Claude in Chrome (ou pelo navegador do app), **somente leitura**. Sem navegador disponível, a equipe anexa os PDFs dos relatórios.
