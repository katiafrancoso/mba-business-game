# T2 — Agente Operações & Logística: recomendação

> Base: docs 03, 07 e 08, o relatório de Operações do T1 e a demanda estimada pelo agente Mercado. Gerado em 22/11/2026.
> **Status: recomendação para discussão.**

## 1. Situação
- **Fábrica:** BH, com 10.000 un. por trimestre de capacidade e custo fixo de R$ 45.000 por trimestre.
- **CUF em BH:** R$ 15,00; custo total de R$ 19,50 por kit com 80% de uso.
- **Estoque disponível no T2:** 8.000 kits, **todos em BH**.
- **Lembrete:** o que for produzido no T2 **só vende no T3**.

## 2. Produção no T2 (para vender no T3) — **produzir 9.000**
| | SP | BS | CR | BH |
|---|---|---|---|---|
| Aumentar capacidade | 0 | 0 | 0 | **0** |
| **Produzir neste trimestre** | 0 | 0 | 0 | **9.000** |

**Racional:**
- Demanda média por equipe no T3 ≈ **8.006** (mercado +6,7%). Somada à sobra esperada do T2 (~500), teremos **~9.500 disponíveis no T3**, uma margem de segurança de ~15% contra falta de produto.
- Com 90% de uso, a ociosidade custa apenas R$ 4.500 (contra R$ 45.000 se não produzirmos nada).
- Desembolso no T2 ≈ **R$ 169 mil** (9.000 × CUF de 14,25 após a melhoria de processo + R$ 40.500 de custo fixo alocado).
- *Alternativas:*

| Produção | Caixa | Comentário |
|---|---|---|
| 8.000 | −R$ 14 mil | Mais apertado no T3 |
| 10.000 | +R$ 14 mil | Zera a ociosidade, mas o caixa do T2 não comporta sem crédito maior |

- **Não expandir** a capacidade no T2: o caixa é escasso e 10.000 por trimestre cobre a demanda prevista até o T4 (média de 8.865).

## 3. Logística — matriz de prioridade
Todo o estoque está em BH, então só a prioridade **com origem em BH** importa no T2:
| Origem | Prioridade de destino |
|---|---|
| **BH** | **1. São Paulo → 2. Brasília → 3. Curitiba** |
| SP / BS / CR | Manter o padrão (não há estoque nessas cidades) |
- SP primeiro por ser o maior mercado e o mais sensível à falta (base Básico).
- ⚠️ O aviso da tela Conclua diz "Não foram definidas as regras da matriz de logística". **É preciso salvar a matriz** mesmo que o padrão já pareça correto.
- Frete esperado: ~5.850 kits transferidos para fora de BH × R$ 3 ≈ **R$ 17,6 mil**.

## 4. Compras emergenciais (RoxConn)
| SP | BS | CR | BH |
|---|---|---|---|
| **0** | **0** | **0** | **0** |
- No cenário base sobram ~500 kits. A RoxConn (R$ 30 por kit) só se justifica se a equipe acreditar no cenário otimista (> 8.000). Nesse caso, cerca de **500 kits em SP** (R$ 15 mil) seriam o seguro.

## 5. Indicadores esperados no fim do T2 (cenário base)
| Indicador | Valor |
|---|---|
| Kits vendidos | ~7.500 |
| Estoque final | ~500 kits em BH |
| Utilização da capacidade | 90% |
| Custo unitário da produção do T2 | ~R$ 18,75 (com melhoria de processo) |
| Despesa com ociosidade | R$ 4.500 |

## 6. Pauta para os próximos trimestres
- **T3:** avaliar uma 2ª fábrica (SP tem o menor CUF segundo o manual) **ou** expandir BH, se o share passar de 12,5% e a demanda do T4/T5 confirmar (+10,7% no T4). Confirmar a regra de custo de expansão (ver doc 03).
- Comparar sempre: custo de transferir (R$ 3 por kit) × economia de escala.
