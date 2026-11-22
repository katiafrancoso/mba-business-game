# 06 — Simulador: telas, campos de decisão e relatórios

URL: `https://bm.tectrain.com.br` (TecTrain Business Management). Cabeçalho: usuário, turma **IBMEC-OL-Turma2NOV26**, **Equipe 3** e trimestre atual.

## Menu principal
| Aba | URL | Conteúdo |
|---|---|---|
| **PREPARE-SE** | `/Preparese` | Gráficos (unidades vendidas, participação de mercado, demanda real consolidada) e a tabela de **demanda potencial do trimestre**, que só aparece se a pesquisa foi comprada no trimestre anterior |
| **ANÁLISE** | `/Analise` | Seletor de trimestre e relatórios em PDF (lista abaixo) |
| **DECISÕES** | `/Planeje/...` | 6 sub-abas de decisão |
| **PROJEÇÕES** | `/Projecoes` | Simulação do trimestre atual com as decisões salvas: Resumo, DRE, Balanço, Fontes e Usos, Fluxo de Caixa, Indicadores |
| **CONCLUA** | `/Conclua` | **Avisos importantes** e revisão consolidada de todas as decisões |
| Mensagens | `/Mensagem` | Mensagens do instrutor (nenhuma até o T2) |
| Suporte | `/Home/SuporteTecnico` | Formulário de contato com a professora |
| Ajuda | `/Content/manual_part_bm.pdf` | Manual do participante |

## Sub-abas de DECISÕES e seus campos
### Vendas (`/Planeje/Vendas`)
- **Vendedores** por cidade (anterior/atual): contratar ou demitir, o que abre ou fecha o escritório.
- Por cidade × segmento: **Demanda estimada (un.)**, Entregas, **Preço (R$)** e **Versão do produto**.
- Indicadores (T atual × T anterior): preço de equilíbrio, ponto de equilíbrio (un.), margem de venda, giro do ativo, lucro líquido, saldo de caixa, preço médio, demanda, entregas e receitas.
- Botões: **Modificar** → editar → **Salvar**.

### Marketing (`/Planeje/Marketing`)
- **Propaganda (R$)** por cidade.
- **Política de recebimento:** % em T, T+1, T+2, T+3.
- **Prioridade (de entrega/atuação) por cidade:** Básico ou Premium (direciona o esforço dos vendedores).
- **Comprar pesquisas de mercado:** Indicadores (R$ 10 mil) e Demanda projetada (R$ 15 mil), SIM/NÃO.

### Logística (`/Planeje/Logistica`)
- **Prioridade para transferência de estoque**, por cidade de origem (ordem dos destinos).
- **Compras emergenciais (unidades)** por cidade, ou seja, a compra antecipada da RoxConn a R$ 30/un., entregue no mesmo trimestre.

### Produção (`/Planeje/Producao`)
- **Aumentar capacidade** por cidade (dropdown de 0 a 10.000, em passos de 500).
- **Produzir neste trimestre** por cidade (fica disponível para venda no **próximo** trimestre).
- Indicadores: utilização da capacidade, estoque disponível para vendas, compra de terceiros e demanda estimada.

### Tecnologia e Processos (`/Planeje/TecnologiaProcessos`)
- **P&D:** Acelerar projeto? (SIM/NÃO); Pesquisadores contratar (+) ou demitir (−). Itens: versão atual, % completado, trimestres para a nova versão, custo para acelerar, nº de pesquisadores e despesa da equipe.
- **Qualidade:** Inspeções (SIM/NÃO), Estudo (SIM/NÃO), Ações de melhoria (R$). Indicadores de defeitos e despesas.
- **Melhoria de processo:** Redução de custos (R$) por cidade. Itens: CUF no trimestre por cidade e gastos acumulados.

### Finanças (`/Planeje/Financas`)
Sub-abas: Conta garantida | Empréstimo de curto prazo | Empréstimo de longo prazo | Antecipação de recebíveis | Investimentos (CDB: investir e resgatar) | Cobrança | Dividendos.
Cada linha de crédito mostra a taxa básica, o prêmio de risco, o custo da linha, a taxa total anual e trimestral, o **limite aprovado** (vem do banco/instrutor), o empréstimo em vigor, o valor sacado, o disponível para saque e o campo para pagar o empréstimo.

## Tela CONCLUA: avisos automáticos (exemplos reais do T2)
- "As decisões podem ser enviadas."
- "Produção no trimestre igual a zero"
- "Investimento em propaganda no trimestre igual a zero"
- "Nenhum representante alocado no trimestre"
- "Não foram definidas as regras da matriz de logística"
- "Ponto de equilíbrio", "Lucro líquido", "Endividamento"
- "**Caixa final < 0 – gerou empréstimo de emergência**"
> Use esta tela como **checklist final** antes de cada envio.

## Relatórios da aba ANÁLISE (PDF, por trimestre)
1. **Indicadores de Mercado, Operacionais e Financeiros** (exige a pesquisa de R$ 10 mil): para as 8 equipes, % de entregas e % de demanda por segmento e cidade, preços, preço médio, representantes por cidade, versão do produto por praça e segmento, capacidade instalada, estoque final, entregas e resumo financeiro (receita, EBITDA, dividendos, índice de endividamento, reservas, margem, giro, alavancagem, ROA, ROE).
2. **Operações:** por fábrica, capacidade, unidades em fabricação, custo direto unitário, custo fixo alocado e não alocado, custo total unitário e unidades disponíveis para o próximo trimestre.
3. **Logística:** entregue e falta por cidade e segmento, transferências entre praças e compras emergenciais.
4. **Demonstração de Resultado.**
5. **Balanço Patrimonial.**
6. **Fluxo de Caixa.**
7. **Fontes e Usos de Caixa.**
8. **Resumo de Desempenho Financeiro:** endividamento, cobertura de juros, crédito fiscal, margens, ROA, ROE, FCL, taxa básica, prêmio de risco, custo de cada linha, taxa de inadimplência e prazo médio de recebimento.
9. **Demanda Projetada Potencial** (exige a pesquisa de R$ 15 mil): demanda por cidade e segmento para o próximo trimestre e crescimento estimado do mercado para os 3 trimestres seguintes.
10. **Decisões Operacionais da Empresa:** registro de todas as decisões tomadas.

O manual ainda cita: Geração de Demanda, Política de Qualidade e P&D, e Balanced Scorecard (devem aparecer a partir dos trimestres operacionais).

## Regras de operação do sistema
- **Vale a última decisão salva por qualquer membro da equipe.** Combinem quem salva o quê e revisem tudo antes do processamento.
- As decisões valem para 1 trimestre. O instrutor processa a rodada.
- **Os agentes não devem clicar em Salvar ou enviar decisões.** Eles produzem recomendações; quem registra é a equipe.
