# 05 — Finanças

## 1. Princípios
- Garantir caixa para a operação **sem cair no empréstimo de emergência**, que é automático e caro.
- Os bancos observam o **PL** (capital + lucros acumulados) e o **endividamento**. Em casos extremos, assumem a gestão e "os cargos dos diretores correm risco".
- As despesas saem do caixa no trimestre em que ocorrem; as vendas a prazo entram nos trimestres seguintes.

## 2. Taxas de referência [observado no Resumo de Desempenho Financeiro do T1]
| Item | Valor (a.a.) |
|---|---|
| Taxa básica de juros | **8,0%** (pode mudar a cada trimestre) |
| Custo da linha: Conta garantida | 6,0% |
| Custo da linha: Curto prazo | 4,0% |
| Custo da linha: Longo prazo | 5,0% |
| Custo da linha: Emergência | 9,0% (ver nota) |
| Prêmio de risco | conforme o endividamento (tabela abaixo) |
> Nota: a tabela-resumo do manual diz que a emergência custa **150% da taxa da conta garantida**. [análise] Na projeção do T2, juros de R$ 1.096,20 sobre R$ 20.300 dão **≈ 5,4% ao trimestre**, coerente com 1,5 × (8% + 1% + 6%) = 22,5% a.a.

## 3. Prêmio de risco (Manual §7.1.4)
**Endividamento** = (empréstimos de curto prazo + longo prazo + conta garantida + emergência) ÷ (capital social + lucros acumulados), medido no trimestre anterior ao recebimento do empréstimo.
| Endividamento | Rating | Prêmio |
|---|---|---|
| 0% a 24% | Baixo risco | 0% a.a. |
| 25% a 49% | Risco moderado | 1% a.a. |
| 50% a 99% | Alerta | 2,5% a.a. |
| 100% a 119% | Alto risco | 4,5% a.a. |
| acima de 120% | Restrição de crédito | 6,5% a.a. |
> [observado] A projeção do T2 mostra prêmio de 1,0% com endividamento de 5,3%. Isso não bate exatamente com a tabela; vale confirmar como o sistema calcula.

## 4. Linhas de crédito
| Modalidade | Acesso | Tarifas | Juros | Prazo e pagamento |
|---|---|---|---|---|
| **Emergência** | Automático quando o caixa fica negativo; cobre só o déficit e os juros (o caixa termina em zero) | — | 150% da taxa da conta garantida | Pago automaticamente no trimestre seguinte, se houver caixa |
| **Conta garantida** | A partir do **T2**; o limite é **negociado com o banco (instrutor)**; é preciso **sacar** ativamente | **0,5% sobre o valor utilizado** no trimestre | Básica + prêmio + 6% a.a. (variável) | Pode ser quitada a qualquer momento |
| **Curto prazo (1 ano)** | Negociado com o banco caso a caso | — | Básica (fixada no trimestre do recebimento) + prêmio + 4% a.a. | 4 parcelas trimestrais de 25% do principal mais juros sobre o saldo, começando em T+1. **Não pode ser antecipado.** |
| **Longo prazo (5 anos)** | Negociado com o banco | — | Básica + prêmio + 5% a.a., **prefixada** | Principal no vencimento, juros trimestrais; **pode ser antecipado** total ou parcialmente |

## 5. Outros instrumentos
| Instrumento | Regra |
|---|---|
| **Antecipação de recebíveis** | Antecipa contas a receber de T+1 em diante; entra no caixa do trimestre. **Custo:** o texto do manual (§7.2) diz **3% ao trimestre**; a tabela-resumo (§7.6) diz **12% a.a. proporcional ao prazo + tarifa de R$ 500**. Confirme na tela "Antecipação de recebíveis" (campo Taxa trimestral). |
| **CDB** | Rende **1,5% ao trimestre**. **Não tem resgate automático**: se o caixa ficar negativo, entra emergência mesmo com dinheiro aplicado. |
| **Serviço de cobrança** | Reduz a inadimplência das vendas a prazo. O valor é escolhido pela empresa, de **R$ 0 a R$ 2.000 por trimestre** (aparece como "saídas diversas de caixa"). |
| **Inadimplência** | Atinge as vendas a prazo e é maior quanto mais longo o prazo. |
| **Dividendos** | Exigem caixa ou CDB resgatado **e** lucros acumulados positivos; saem do caixa no mesmo trimestre. |

## 6. Tributos [observado]
- **Crédito fiscal** no T1: R$ 13.132,50 = **34%** do prejuízo de R$ 38.625. Na projeção do T2: R$ 33.029,71 ≈ 34% do prejuízo acumulado.
- [análise] Alíquota de IR/CS de 34%. Os prejuízos geram crédito fiscal que compensa impostos sobre lucros futuros.

## 7. Indicadores usados pelo simulador
Margem líquida (RSV), giro do ativo (V/A), alavancagem (Ativo/PL), ROA = RSV × giro, ROE = ROA × alavancagem, EBITDA = LAJIR + depreciação, índice de cobertura de juros, fluxo de caixa livre, geração líquida de caixa, ponto de equilíbrio, preço de equilíbrio e Balanced Scorecard.
> [análise] O ROE e o lucro/reservas acumulados tendem a ser os critérios de avaliação. Confirme com o instrutor qual indicador define o ranking.

## 8. Regras práticas [análise]
1. Projete **caixa inicial + recebimentos à vista + recebíveis que vencem − todas as saídas** antes de salvar. Use a tela **Projeções** e o aviso "Empréstimo de emergência" na tela Conclua.
2. Negocie com o instrutor um limite de conta garantida **antes** de precisar dele.
3. Para cobrir investimento em capacidade, prefira longo prazo (prefixado e antecipável). Para capital de giro, conta garantida ou curto prazo.
4. Mantenha o endividamento **abaixo de 25%** para não pagar prêmio de risco.
