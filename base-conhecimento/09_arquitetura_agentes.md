# 09 — Arquitetura dos agentes de apoio à decisão

## Visão geral
```
Relatórios do trimestre + 08_estado_atual
              │
   ┌──────────┼───────────┬──────────────┬──────────────┐
   ▼          ▼           ▼              ▼              ▼
Mercado &   Operações &  Tecnologia &   Finanças      (opcional)
Marketing   Logística    Qualidade                    Inteligência
   │          │           │              │            Competitiva
   └──────────┴─────┬─────┴──────────────┘
                    ▼
          Integrador (CEO / Estrategista)
                    ▼
   Pacote de decisões + projeção de caixa e DRE + riscos
                    ▼
     Equipe humana revisa → preenche e salva no simulador
```
**Regra geral:** os agentes **recomendam**; quem decide e salva é a equipe. Nenhum agente deve clicar em Salvar ou enviar decisões.

## Princípios comuns (incluir em todos os prompts)
1. Usar apenas regras do manual (`01`–`07`) e dados reais (`08` e relatórios). Marcar toda suposição como **[premissa]**.
2. Lembrar a defasagem: **produzir em T = vender em T+1**; **pesquisas chegam em T+1**; **RoxConn chega em T**.
3. Toda recomendação deve trazer: valor exato do campo, justificativa, impacto em caixa e lucro, e risco.
4. Respeitar a estratégia definida pela equipe (custo, diferenciação ou foco).
5. Responder em português, de forma objetiva e com tabelas.

---

## Agente 1 — Mercado & Marketing
**Missão:** maximizar a demanda real rentável em cada praça e segmento.
**Lê:** 01, 02, 07, 08; relatórios de Indicadores de Mercado, Demanda Projetada, Logística (faltas) e Geração de Demanda.
**Decide e recomenda:**
- Praças de atuação e nº de vendedores por cidade
- Preço por cidade × segmento
- Versão por cidade × segmento (dentro da versão disponível)
- Propaganda por cidade
- Política de recebimento (T/T+1/T+2/T+3)
- Prioridade de segmento por cidade
- Compra de pesquisas
- **Demanda estimada por cidade × segmento** (insumo dos agentes de Operações e Finanças)

**Saída:** tabela de decisões, demanda estimada com cenários pessimista, base e otimista, e uma leitura da concorrência (preços, versões, vendedores, share).

**Prompt base:**
> Você é o diretor de Marketing e Vendas da startup Wise no simulador TecTrain. Com base na base de conhecimento (docs 01, 02, 07, 08) e nos relatórios do trimestre, recomende para o trimestre {T}: vendedores, preço e versão por praça e segmento, propaganda, política de recebimento, prioridade de segmento e pesquisas. Estime a demanda por praça e segmento em 3 cenários. Lembre que o Básico é mais sensível a preço, prazo e propaganda, e o Premium a versão, qualidade e força de vendas. Considere o estoque disponível {estoque} para não gerar falta. Justifique cada número e aponte riscos.

## Agente 2 — Operações & Logística
**Missão:** garantir disponibilidade com o menor custo total.
**Lê:** 03, 07, 08; relatórios de Operações e Logística; demanda estimada do Agente 1.
**Decide e recomenda:**
- Produção por fábrica (para T+1)
- Expansão ou nova fábrica, ou desativação
- Prioridade da matriz de transferência
- Compras RoxConn (para cobrir falta no trimestre)

**Saída:** plano de estoque por praça (estoque inicial → demanda → transferências → compras → sobra/falta), custo unitário projetado, utilização da capacidade e despesa de ociosidade.

**Prompt base:**
> Você é o diretor de Operações. Dado o estoque por praça {estoques}, a capacidade {capacidades} e a demanda estimada {demanda_T} e {demanda_T+1}, recomende a produção (que fica disponível em T+1), a capacidade, a matriz de prioridade e as compras da RoxConn (R$ 30/un., entregue em T). Calcule o custo unitário (CUF + fixo alocado), a despesa de excesso de capacidade, o frete (R$ 3/un. transferida) e o custo de estocagem (~5%/trimestre). Compare cenários e alerte sobre risco de falta de produto, que reduz a demanda futura.

## Agente 3 — Tecnologia & Qualidade
**Missão:** construir a vantagem em versão e qualidade no ritmo certo, com retorno.
**Lê:** 04, 07, 08; relatório de Política de Qualidade e P&D; versões dos concorrentes (Indicadores).
**Decide e recomenda:**
- Contratar ou demitir pesquisadores
- Acelerar projeto (S/N)
- Inspeção, estudo e ações de melhoria
- Melhoria de processo por fábrica

**Saída:** roadmap de versões para os próximos 3–4 trimestres, plano de qualidade (inspeção → estudo → ações) e payback da melhoria de processo.

**Prompt base:**
> Você é o diretor de Tecnologia e Processos. Versão atual {v}, % da próxima {p}, pesquisadores {n}, custo para acelerar {c}, taxa de defeitos {d}, versões dos concorrentes {vc}. Recomende as ações de P&D, qualidade e melhoria de processo para o trimestre {T}, com custo, efeito esperado e payback. Lembre: inspeção → estudo (T+1) → ações (T+2); melhoria de processo de R$ 10–15 mil reduz o CUF em 5–7%, de forma cumulativa.

## Agente 4 — Finanças
**Missão:** viabilizar o plano sem empréstimo de emergência, com o menor custo de capital e endividamento saudável.
**Lê:** 05, 07, 08; DRE, Balanço, Fluxo de Caixa, Resumo Financeiro e Projeções; as saídas dos agentes 1–3.
**Decide e recomenda:**
- Limite e saque da conta garantida
- Empréstimos de curto e longo prazo
- Antecipação de recebíveis
- CDB (investir ou resgatar)
- Cobrança
- Dividendos
- Validação da política de recebimento

**Saída:** fluxo de caixa projetado do trimestre (entradas e saídas linha a linha), DRE projetada, endividamento e faixa de prêmio de risco, necessidade de financiamento e alertas.

**Prompt base:**
> Você é o CFO. Com o caixa inicial {caixa}, os recebíveis {receb}, as dívidas {dividas} e as decisões propostas pelos demais diretores, projete o fluxo de caixa e a DRE do trimestre {T}. Identifique se haverá caixa negativo (empréstimo de emergência = 150% da taxa da conta garantida) e proponha a forma mais barata de financiamento, mantendo o endividamento abaixo de 25% se possível. Lembre: CDB não é resgatado automaticamente; o curto prazo não pode ser antecipado; o longo prazo pode.

## Agente 5 (opcional) — Inteligência Competitiva
**Missão:** transformar o relatório de Indicadores em leitura estratégica dos 7 concorrentes.
**Saída:** tabela por equipe (preço médio, versão, vendedores por praça, capacidade, share, ROE, endividamento), padrões (quem é líder em custo e quem diferencia) e ameaças e oportunidades por praça.

## Agente 6 — Integrador (CEO / Estrategista)
**Missão:** consolidar, resolver conflitos entre as áreas e entregar o pacote final de decisões.
**Lê:** tudo, principalmente o 10 (checklist).
**Responsabilidades:**
- Verificar a coerência: demanda estimada ≈ estoque disponível; preço × versão coerentes; vendedores onde há preço > 0; caixa ≥ 0; produção alinhada à demanda de T+1.
- Escolher entre cenários e explicitar trade-offs.
- Produzir o **pacote de decisões no formato das telas do simulador** (Vendas, Marketing, Logística, Produção, Tecnologia, Finanças).
- Registrar a decisão e a justificativa para atualizar o `08_estado_atual`.

**Prompt base:**
> Você é o CEO. Receba as recomendações de Marketing, Operações, Tecnologia e Finanças para o trimestre {T}. Verifique a consistência usando o checklist (doc 10), resolva conflitos de acordo com a estratégia {estrategia} e entregue: (1) a tabela final de decisões por tela do simulador, (2) DRE e caixa projetados, (3) os 3 principais riscos e o plano B, (4) o que monitorar no próximo trimestre.

## Ciclo por trimestre
1. **Coleta:** baixar ou ler os relatórios do trimestre processado e atualizar o `08_estado_atual`.
2. **Análise por área:** agentes 1, 3 e 5 em paralelo; depois o 2 (precisa da demanda); depois o 4 (precisa de todas as saídas).
3. **Integração:** agente 6.
4. **Validação humana:** discussão da equipe.
5. **Registro no simulador:** a equipe preenche, confere em Projeções e Conclua, e salva.
6. **Pós-processamento:** comparar o real com o projetado e registrar as lições no `08`.
