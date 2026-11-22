# Base de Conhecimento — Business Game "Startup de Tecnologia" (TecTrain Business Management)

> **Como operar este Projeto:** leia primeiro `harness/00_HARNESS_LEIA_PRIMEIRO.md` (regras, comandos, templates e onde salvar). Os registros vivos estão em `registro/`.

> Projeto agêntico de MBA (IBMEC – Turma IBMEC-OL-Turma2NOV26 – **Equipe 3**).
> Objetivo: dar aos agentes o contexto necessário para apoiar as decisões trimestrais no simulador.

## Fontes usadas
1. **Manual do Participante v.2** (TecTrain, 42 p.): texto e tabelas, incluindo as que estão como imagem.
2. **Simulador** `bm.tectrain.com.br`: telas Prepare-se, Análise (10 relatórios do T1), Decisões (6 abas), Projeções, Conclua, Mensagens e Suporte. O site **não tem vídeos**.
3. **Dados observados no simulador** que não constam do manual. Eles estão marcados como **[observado]** e foram deduzidos dos relatórios.

## Mapa dos documentos
| Arquivo | Conteúdo | Usado principalmente por |
|---|---|---|
| `01_contexto_empresa_mercado.md` | História, produto Wise, investidores, segmentos e regiões | Todos |
| `02_marketing_vendas_demanda.md` | Atributos de demanda, preço, versão, propaganda, vendedores, prazo, pesquisas | Agente Mercado/Marketing |
| `03_operacoes_logistica.md` | Fábricas, capacidade, custos fixos e diretos, matriz de logística, RoxConn | Agente Operações |
| `04_tecnologia_qualidade.md` | P&D, versões, qualidade, melhoria de processo | Agente Tecnologia |
| `05_financas.md` | Linhas de crédito, prêmio de risco, CDB, antecipação, dividendos, impostos | Agente Financeiro |
| `06_simulador_telas_relatorios.md` | Telas, campos de decisão, relatórios, fluxo para salvar e enviar | Todos (operacional) |
| `07_parametros_e_formulas.md` | Referência rápida com todos os números e fórmulas | Todos (cálculo) |
| `08_estado_atual_equipe3.md` | Resultado do T1, estoque, caixa, projeção do T2 e demanda potencial | Todos (situação) |
| `09_arquitetura_agentes.md` | Papéis, entradas, saídas e prompts dos agentes | Orquestração |
| `10_checklist_rodada_e_armadilhas.md` | Roteiro de decisão por trimestre e erros comuns | Agente Integrador (CEO) |

## Recomendações por rodada (`rodadas/`)
Cada trimestre tem uma pasta com a saída dos agentes. **Comece pelo `T{n}_00_RECOMENDACAO_FINAL_CEO.md`.**
- `rodadas/T2/`: 00 CEO (pacote final por tela) | 01 Mercado & Marketing | 02 Operações & Logística | 03 Tecnologia & Qualidade | 04 Finanças | 05 Inteligência Competitiva.

> O jogo é o **TecTrain Business Management**, contratado pela escola. A rodada zero (T1) foi decidida pelos professores, igual para todas as equipes. Os agentes **apenas geram recomendações**; quem decide e registra no simulador é a equipe.

## Convenções
- **T** = trimestre corrente; T1 = fase pré-operacional.
- Cidades: **SP** São Paulo, **BS** Brasília, **CR** Curitiba, **BH** Belo Horizonte.
- Segmentos: **Básico** e **Premium**.
- **[manual]** = regra do manual; **[observado]** = valor visto nas telas ou relatórios; **[análise]** = inferência nossa, que precisa ser validada.
- Atualize o `08_estado_atual_equipe3.md` a cada trimestre, depois do processamento.
