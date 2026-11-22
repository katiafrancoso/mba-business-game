# 07 — Referência rápida: parâmetros e fórmulas

## Parâmetros fixos (manual)
| Área | Parâmetro | Valor |
|---|---|---|
| Empresa | Capital inicial | R$ 500.000 (5.000 ações), sem novos aportes |
| Mercado | Demanda potencial de uma empresa média (ano 1) | 25–35 mil un./ano (Básico 15–20 mil; Premium 10–15 mil) |
| Mercado | Distribuição inicial | SP 35%, BS 25%, CR 20%, BH 20% |
| Preço | Referência inicial | Básico ≈ R$ 50; Premium ≈ R$ 60 |
| Propaganda | Faixa eficiente inicial | R$ 5–10 mil por cidade e trimestre |
| Pesquisa | Indicadores / Demanda | R$ 10.000 / R$ 15.000 (chegam em T+1) |
| Vendas | Contratar ou demitir vendedor | R$ 4.000 |
| Vendas | Salário por vendedor | R$ 3.000/trimestre |
| Vendas | Abrir ou fechar escritório | R$ 10.000 |
| Vendas | Aluguel do escritório | R$ 2.000/trimestre |
| Produção | Investimento em capacidade | Tabela 4 (`03_operacoes_logistica.md`) |
| Produção | Custo fixo por fábrica | Tabela 5 (R$ 15 mil a 82,5 mil/trimestre) |
| Produção | Desativar fábrica | R$ 25.000 + 50% do custo fixo por trimestre parado |
| Logística | Transferência entre praças | R$ 3,00/un. |
| RoxConn | Compra antecipada | R$ 30,00/un., entregue no mesmo trimestre, versão básica |
| P&D | Contratar ou demitir pesquisador | R$ 1.000 |
| P&D | Remuneração do pesquisador | R$ 2.000/trimestre |
| Qualidade | Defeitos iniciais | 10% |
| Qualidade | Inspeção | −40% de defeitos ao cliente; custa 40% da garantia resultante |
| Qualidade | Estudo | R$ 5.000/trimestre |
| Qualidade | Ações de melhoria | R$ 5.000 a 100.000 |
| Processo | Melhoria de processo | R$ 10–15 mil → −5% a 7% no CUF (cumulativo) |
| Finanças | Linhas (custo específico) | Conta garantida 6% a.a. (+0,5% de tarifa sobre o utilizado); Curto prazo 4% a.a.; Longo prazo 5% a.a.; Emergência 150% da conta garantida |
| Finanças | Prêmio de risco | 0 / 1 / 2,5 / 4,5 / 6,5% a.a. por faixa de endividamento (25 / 50 / 100 / 120%) |
| Finanças | CDB | 1,5% ao trimestre |
| Finanças | Antecipação de recebíveis | 3% ao trimestre (texto) ou 12% a.a. + R$ 500 (tabela): confirmar |
| Finanças | Cobrança | R$ 0 a 2.000/trimestre |

## Parâmetros observados no simulador (equipe 3)
| Parâmetro | Valor | Fonte |
|---|---|---|
| Taxa básica de juros | 8% a.a. (T1 e T2) | Resumo financeiro do T1, Projeções do T2 |
| CUF da fábrica de BH (10.000 un.) | R$ 15,00 | Relatório de Operações do T1 |
| CUF de referência nas cidades sem fábrica | SP 25,00, BS 24,00, CR 23,00 | Tela Melhoria de Processo do T2 |
| Depreciação da fábrica | 1,667% do investimento por trimestre (R$ 4.625 sobre 277.500) | DRE do T1 |
| Manutenção de estoque | ≈ 5% do valor do estoque por trimestre | Projeção do T2 (7.800 sobre 156.000) |
| Alíquota de IR/CS (crédito fiscal) | 34% | Resumo do T1 |
| Custo para acelerar P&D até a versão 1 | R$ 40.000 | Tela de P&D do T2 |
| Concorrentes | 8 equipes, todas com 10.000 de capacidade no T1 | Indicadores do T1 |

## Fórmulas
- **Custo fixo alocado ao produto** = Custo fixo × (Produção ÷ Capacidade).
- **Despesa com excesso de capacidade** = Custo fixo × (1 − Produção ÷ Capacidade).
- **Custo unitário do produto** = CUF + Custo fixo alocado ÷ Produção (+ custo de versão).
  - Exemplo do T1 em BH: 15,00 + 36.000/8.000 = **R$ 19,50**.
- **Despesa com garantia** = CMV × taxa de defeitos.
- **Despesa com inspeção** = 40% × despesa com garantia (já reduzida).
- **Endividamento** = Dívidas (curto + longo + conta garantida + emergência) ÷ (Capital + Lucros acumulados).
- **Taxa de um empréstimo** = Taxa básica + Prêmio de risco + Custo da linha (a.a.); taxa trimestral ≈ anual ÷ 4.
- **Receita** = min(Demanda real, Estoque disponível) × Preço.
- **Caixa do trimestre** = Caixa inicial + recebimentos (à vista do trimestre + parcelas de trimestres anteriores − inadimplência) − pagamentos (produção, custo fixo, vendedores, escritórios, propaganda, pesquisas, P&D, qualidade, frete, RoxConn, juros e amortizações, investimentos).
- **Margem de contribuição unitária [análise]** = Preço − Custo unitário − Frete (R$ 3, se transferido) − Garantia (≈ taxa de defeitos × custo unitário).
  - Exemplo: Básico a R$ 50 com custo de R$ 19,50, frete de R$ 3 e garantia de 10% (R$ 1,95) dá ≈ **R$ 25,55/un.**
- **Ponto de equilíbrio (un.)** = Custos e despesas fixos do trimestre ÷ Margem de contribuição unitária.
