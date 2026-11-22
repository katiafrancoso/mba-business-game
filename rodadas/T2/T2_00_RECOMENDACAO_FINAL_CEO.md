# T2 — Recomendação final do Agente Integrador (CEO)

> Consolida os agentes 01 a 05 desta pasta. Gerado em 22/11/2026.
> **A decisão é da equipe.** Este documento é o guia para a reunião e para o preenchimento do simulador.

## Estratégia proposta para o T2: "Presença total com disciplina de caixa"
1. **Entrar nas 4 praças** para girar todo o estoque de 8.000 kits.
2. **Preços de referência (50/60)**: sem guerra de preço num mercado equilibrado.
3. **Plantar o futuro barato:** P&D com equipe própria, pipeline de qualidade e redução de custo.
4. **Financiar com longo prazo** (antecipável) em vez de cair no empréstimo de emergência.

**Resultado esperado (base):** ~7.500 kits vendidos, receita de ~R$ 404 mil, LAJIR de ~+R$ 16 mil e caixa final de ~+R$ 50 mil (com o empréstimo de R$ 100 mil).

---

## Pacote de decisões por tela do simulador
### DECISÕES › VENDAS
| | SP | BS | CR | BH |
|---|---|---|---|---|
| Vendedores (total atual) | **3** | **2** | **2** | **2** |
| Preço Básico (R$) | **50,00** | **50,00** | **50,00** | **50,00** |
| Preço Premium (R$) | **60,00** | **60,00** | **60,00** | **60,00** |
| Versão Básico | 0 | 0 | 0 | 0 |
| Versão Premium | 0 | 0 | 0 | 0 |
| Demanda estimada Básico | 1.790 | 1.240 | 555 | 990 |
| Demanda estimada Premium | 770 | 670 | 830 | 660 |

### DECISÕES › MARKETING
| | SP | BS | CR | BH |
|---|---|---|---|---|
| Propaganda (R$) | **10.000** | **8.000** | **6.000** | **6.000** |
| Prioridade | **Básico** | **Básico** | **Premium** | **Básico** |

- **Política de recebimento:** T **80%** | T+1 **20%** | T+2 0% | T+3 0%. *Se o empréstimo não for aprovado: 100% em T.*
- **Pesquisas:** Indicadores **SIM** | Demanda projetada **SIM** (a primeira a cortar se o caixa apertar).

### DECISÕES › LOGÍSTICA
- **Prioridade de transferência (origem BH):** 1. São Paulo → 2. Brasília → 3. Curitiba. Demais origens: manter o padrão. **Salvar a matriz** (há aviso pendente).
- **Compras emergenciais (RoxConn):** 0 em todas as praças.

### DECISÕES › PRODUÇÃO
- Aumentar capacidade: **0** em todas.
- **Produzir neste trimestre: BH = 9.000** (as demais, 0).

### DECISÕES › TECNOLOGIA E PROCESSOS
- **P&D:** Acelerar = **NÃO**; Pesquisadores = **+6**. Conferir na tela os trimestres até a versão 1; se mostrar mais de 2, usar +8.
- **Qualidade:** Inspeção = **SIM**; Estudo = NÃO (começa no T3); Ações = R$ 0.
- **Melhoria de processo:** BH = **R$ 10.000** (as demais, 0).

### DECISÕES › FINANÇAS
- **Empréstimo de longo prazo: R$ 100.000** (depende de o instrutor liberar o limite).
- Conta garantida: pedir um limite de reserva de R$ 50 mil; **não sacar**.
- Cobrança: **R$ 500**. CDB, antecipação e dividendos: 0.

---

## Orçamento do T2 (cenário base)
| Bloco | R$ |
|---|---|
| Comercial (escritórios + vendedores + propaganda + pesquisas) | 166.000 |
| Produção para o T3 (9.000 kits) | 168.750 |
| Tecnologia (P&D + qualidade + melhoria) | ~33.000 |
| Logística (frete + manutenção de estoque) | ~25.400 |
| **Total de saídas** | **~406.000** |
| Entradas à vista (80%) | ~323.500 |

## Plano de contingência
| Se… | Então… |
|---|---|
| O instrutor **não liberar** o empréstimo a tempo | Recebimento **100% à vista** e comprar só a pesquisa de Indicadores. O caixa base fica em ~+R$ 45 mil. |
| A equipe quiser **reduzir risco de caixa** | 2 vendedores em SP (−R$ 7 mil); produzir 8.000 (−R$ 14 mil); P&D com 4 pesquisadores (−R$ 6 mil) |
| A equipe quiser ser **mais agressiva no Premium** | Acelerar P&D (R$ 40 mil) e vender a versão 1 no Premium a R$ 62–65, financiando com R$ 140 mil de longo prazo (endividamento de ~30%, com prêmio de 1%) |
| A tela Projeções mostrar **empréstimo de emergência** | Rever, nesta ordem: pesquisa de Demanda → nº de pesquisadores → produção → política de recebimento |

## Checklist antes de salvar (resumo do doc 10)
- [ ] Mensagem enviada ao instrutor pedindo os limites de crédito e o critério de avaliação.
- [ ] Preço > 0 somente onde há vendedor (as 4 praças).
- [ ] A matriz de logística foi salva.
- [ ] **PROJEÇÕES:** caixa final ≥ 0, sem empréstimo de emergência.
- [ ] **CONCLUA:** todos os avisos lidos; revisão completa das decisões.
- [ ] **Uma única pessoa salva a versão final**, porque vale a última decisão salva.

## Pontos de decisão da equipe (onde há trade-off real)
1. **Prazo de recebimento:** 80/20 com empréstimo ou 100% à vista sem dívida?
2. **Premium a R$ 60 com versão 0**, ou R$ 58 até ter a versão 1?
3. **P&D:** 6 pesquisadores (barato e mais lento) ou acelerar por R$ 40 mil (rápido e caro)?
4. **Pesquisa de Demanda (R$ 15 mil):** comprar já no T2?

## Depois do processamento do T2
Atualizar o `08_estado_atual_equipe3.md` com o resultado real e pedir aos agentes a análise do relatório de Indicadores do T2 (concorrentes), que será a base das decisões do T3.
