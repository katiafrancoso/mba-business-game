# T2 — Agente Mercado & Marketing: recomendação

> Base: docs 01, 02, 07 e 08 e o relatório "Demanda Projetada Potencial" do T1. Gerado em 22/11/2026.
> **Status: recomendação para discussão da equipe. Não registrar no simulador sem validação.**

## 1. Leitura do mercado no T2
- Todas as 8 equipes partem **iguais**: o T1 foi rodado pelos professores, com 10.000 de capacidade e 8.000 kits em estoque para cada equipe [premissa: as demais equipes também têm 8.000 kits].
- **Oferta total ≈ 64.000 kits × demanda potencial de 60.018.** O mercado está equilibrado, e **não há motivo para guerra de preço no T2**.
- Ninguém tem versão > 0 nem vendedores ainda. O T2 é a **corrida pela presença nas praças**.
- Mix por praça (demanda potencial total do mercado → média por equipe):

| Praça | Total | Básico | Premium | % Premium | Média por equipe |
|---|---|---|---|---|---|
| SP | 20.471 | 14.329 | 6.142 | 30% | **2.559** |
| BS | 15.272 | 9.927 | 5.345 | 35% | 1.909 |
| CR | 11.091 | 4.437 | 6.654 | **60%** | 1.386 |
| BH | 13.184 | 7.910 | 5.274 | 40% | 1.648 |
| **Total** | 60.018 | 36.603 | 23.415 | 39% | **7.502** |

## 2. Recomendação de decisões (telas Vendas e Marketing)
### Praças e vendedores — **entrar nas 4 praças**
| | SP | BS | CR | BH | Total |
|---|---|---|---|---|---|
| **Vendedores** | **3** | **2** | **2** | **2** | **9** |

**Por quê:**
- Com 8.000 kits e média de demanda de 7.502 por equipe, **precisamos das 4 praças para girar o estoque**. Se ficarmos fora de uma praça, sobram de ~1.400 a 2.500 kits parados, pagando ~5% ao trimestre.
- SP é o maior mercado (34%) e recebe 1 vendedor a mais.
- Força de vendas pesa bastante nos dois segmentos (Premium ≈ 0,85; Básico ≈ 0,65).
- Custo: 4 escritórios (4 × 12 mil = R$ 48 mil) + 9 vendedores (9 × 7 mil = R$ 63 mil) = **R$ 111 mil**. Do T3 em diante cai para R$ 35 mil por trimestre (aluguel + salários).
- *Alternativa enxuta:* 2 vendedores em cada praça (8 no total), economizando R$ 7 mil.

### Preço e versão
| Praça | Básico (R$) | Premium (R$) | Versão B | Versão P |
|---|---|---|---|---|
| SP | **50,00** | **60,00** | 0 | 0 |
| BS | **50,00** | **60,00** | 0 | 0 |
| CR | **50,00** | **60,00** | 0 | 0 |
| BH | **50,00** | **60,00** | 0 | 0 |

- Seguimos a referência da Projecta (B ≈ 50 / P ≈ 60). O manual pede para não se afastar dela "até ter informações sobre os concorrentes", e a primeira leitura dos concorrentes só chega no T3.
- Só existe a versão 0 (P&D zerado). ⚠️ O manual diz que "não é racional vender produtos idênticos por preços diferentes". Como **todos** os concorrentes estão na versão 0, o risco é igual para todos. **A diferenciação do Premium começa no T3**, quando chegar a versão 1 (ver agente Tecnologia).
- *Variante a discutir:* Premium a R$ 58 em SP, BS e BH (mais sensíveis a preço) e R$ 60 em CR.

### Propaganda — R$ 30 mil no total
| SP | BS | CR | BH |
|---|---|---|---|
| **R$ 10.000** | **R$ 8.000** | **R$ 6.000** | **R$ 6.000** |
- Fica dentro da faixa eficiente do manual (R$ 5–10 mil), proporcional ao tamanho da praça e ao peso do Básico, que é o mais sensível à propaganda.

### Prioridade de atuação dos vendedores
| SP | BS | CR | BH |
|---|---|---|---|
| **Básico** | **Básico** | **Premium** | **Básico** |

### Política de recebimento
| T (à vista) | T+1 | T+2 | T+3 |
|---|---|---|---|
| **80%** | **20%** | 0% | 0% |
- O Básico valoriza prazo (≈ 0,6), mas **o caixa é o gargalo do T2** (ver agente Finanças).
- **Com 80/20 é preciso um empréstimo** de ~R$ 100 mil. **Sem empréstimo aprovado, use 100% à vista.**

### Pesquisas de mercado
| Pesquisa | Decisão | Justificativa |
|---|---|---|
| Indicadores (R$ 10 mil) | **SIM** | Indispensável: é a primeira vez que veremos preços, vendedores e share dos concorrentes |
| Demanda projetada (R$ 15 mil) | **SIM** | Abre a demanda por praça e segmento do T3 e orienta a produção do T3 para o T4. Se o caixa apertar, é a primeira a cortar. |

## 3. Demanda estimada (insumo para os agentes Operações e Finanças)
| Cenário | Demanda nossa (un.) | Vendas (limitadas a 8.000) | Receita estimada |
|---|---|---|---|
| Pessimista (80% da média) | 6.000 | 6.000 | R$ 324 mil |
| **Base (média)** | **7.500** | **7.500** | **R$ 404 mil** |
| Otimista (115%) | 8.630 | 8.000 (falta de ~600) | R$ 431 mil |

Quanto preencher no campo "Demanda (unidades)" da tela Vendas (cenário base):
| | SP | BS | CR | BH |
|---|---|---|---|---|
| Básico | 1.790 | 1.240 | 555 | 990 |
| Premium | 770 | 670 | 830 | 660 |

## 4. Riscos e monitoramento
- **Falta de produto** no cenário otimista: aceitável, porque o estoque é o limite para todos. Avaliar a RoxConn se surgirem sinais de demanda forte.
- **Concorrente agressivo em preço:** só veremos no relatório do T3. Manter a margem no T2.
- **No T3, monitorar:** % de demanda e de entregas por praça, preços médios, vendedores por praça e versão de cada concorrente.
