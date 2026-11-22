# T2 — Agente Finanças: projeção e recomendação

> Base: docs 05, 07 e 08, as Projeções do T2 e as propostas dos agentes 1–3. Gerado em 22/11/2026.
> Modelo simplificado em Python (premissas no fim). **Valide sempre na tela PROJEÇÕES antes de salvar.**

## 1. Ponto de partida
Caixa de **R$ 32.500** | Dívida 0 | PL R$ 461.375 | Endividamento 0% (sem prêmio de risco) | Taxa básica de 8% a.a. | Crédito fiscal de R$ 13,1 mil.

## 2. Projeção do T2 com o plano recomendado (cenário base: 7.500 kits)
### DRE estimada
| Linha | R$ |
|---|---|
| Receita (4.575 B × 50 + 2.927 P × 60) | **404.400** |
| (−) CMV (7.500 × 19,50) | −146.300 |
| **Lucro bruto** | **258.100** |
| Escritórios (abertura + aluguel) | −48.000 |
| Vendedores (contratação + salário, 9) | −63.000 |
| Propaganda | −30.000 |
| Pesquisas de mercado | −25.000 |
| P&D (6 pesquisadores) | −18.000 |
| Melhoria de processo | −10.000 |
| Frete entre praças | −17.600 |
| Garantia + inspeção + retrabalho | −13.800 |
| Manutenção de estoque | −7.800 |
| Ociosidade (90% de uso) | −4.500 |
| Depreciação | −4.600 |
| **LAJIR estimado** | **≈ +15.900** |
> O T2 fica **perto do ponto de equilíbrio** por causa de ~R$ 98 mil de gastos que só ocorrem uma vez (escritórios, contratações e pesquisas). Do T3 em diante a estrutura fica mais leve.

### Caixa do T2 (base)
| | R$ |
|---|---|
| Caixa inicial | 32.500 |
| (+) Recebimento à vista (80% de 404 mil) | 323.500 |
| (−) Produção do T2 para o T3 (9.000 kits) | −168.750 |
| (−) Demais saídas (despesas acima, exceto CMV e depreciação) | −237.600 |
| **Caixa final sem financiamento** | **≈ −50.300** → geraria empréstimo de emergência |
| (+) Contas a receber em T+1 | 80.900 |

## 3. Sensibilidade do caixa final (sem financiamento)
| Cenário | Kits vendidos | LAJIR | Caixa 80/20 | Caixa 100% à vista |
|---|---|---|---|---|
| Pessimista | 6.000 | −29,5 mil | **−108,8 mil** | −44,1 mil |
| **Base** | **7.500** | **+15,9 mil** | **−50,3 mil** | **+30,6 mil** |
| Otimista | 8.000 | +30,9 mil | −31,0 mil | +55,3 mil |

Outras variações (cenário base, 80/20):
| Variação | Efeito no caixa |
|---|---|
| Só pesquisa de Indicadores (sem Demanda) | +15 mil |
| Produzir 8.000 em vez de 9.000 | +14 mil |
| Acelerar P&D no lugar dos 6 pesquisadores | −22 mil |
| Política 70/30 | −40 mil |

## 4. Recomendação de financiamento
**Opção recomendada: empréstimo de LONGO PRAZO de R$ 100.000**, com o limite **negociado com o instrutor** (banco).
- Custo: 8% + 0% de prêmio + 5% = **13% a.a. prefixado (~3,25% ao trimestre ≈ R$ 3,3 mil por trimestre)**, sem tarifa.
- **Pode ser quitado antecipadamente** a qualquer momento: assim que o caixa sobrar (T3/T4), pagamos.
- Com ele, o caixa final fica em ≈ **+R$ 50 mil (base)** e ≈ **−R$ 9 mil (pessimista)**, quase coberto.
- **Endividamento:** 100 mil ÷ ~R$ 470 mil de PL ≈ **21%**, ainda na faixa sem prêmio de risco (< 25%).

**Plano B:** conta garantida com limite de R$ 100–150 mil. Custa 14% a.a. (~3,5% ao trimestre) **+ 0,5% de tarifa sobre o utilizado**, e é preciso **sacar ativamente**, porque o saque não é automático.

**Plano C (sem crédito aprovado até o prazo):** **política de recebimento 100% à vista** e, se possível, comprar só a pesquisa de Indicadores. O caixa fica em ≈ +R$ 30 mil no base e ≈ −R$ 44 mil no pessimista (nesse caso entraria emergência a 150% da taxa da conta garantida).

> Não aplicar em CDB no T2: não haverá sobra de caixa relevante.

## 5. Campos da tela Finanças (opção recomendada)
| Sub-aba | Campo | Valor |
|---|---|---|
| Empréstimo de longo prazo | Valor sacado | **R$ 100.000** (após o instrutor aprovar o limite) |
| Conta garantida | — | Pedir um limite de reserva (R$ 50 mil) ao instrutor; não sacar |
| Antecipação de recebíveis | — | 0 (não há recebíveis) |
| Investimentos (CDB) | — | 0 |
| Cobrança | Investimento | **R$ 500** (protege os 20% a prazo; o custo vai de 0 a 2.000) |
| Dividendos | — | 0 (há prejuízo acumulado) |

## 6. Ação imediata
📧 **Enviar hoje uma mensagem ao instrutor (pelo menu SUPORTE ou MENSAGENS)** pedindo: (a) limite de empréstimo de longo prazo de R$ 100 mil e (b) limite de conta garantida de R$ 50 mil, e perguntando (c) o critério de avaliação final e (d) o custo da antecipação de recebíveis.

## Premissas do modelo
- As vendas não reagem às decisões no modelo. Os cenários fixam a quantidade vendida, então **o modelo não mostra o efeito de cortar vendedores ou propaganda** sobre a demanda.
- Garantia de 6% do CMV com inspeção; inspeção = 40% da garantia; retrabalho ≈ 1% do CMV.
- Manutenção de estoque de 5% sobre o estoque inicial; frete de R$ 3 por kit vendido fora de BH; melhoria de processo de −5% no CUF já no T2.
- Juros do empréstimo, inadimplência e impostos não modelados (há crédito fiscal).
