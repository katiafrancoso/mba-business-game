# Estrutura da base de conhecimento

> O conteúdo está em [`../base-conhecimento/`](../base-conhecimento/). Aqui estão **a estrutura e o método**, reutilizáveis em qualquer business game.

## Documentos
| # | Documento | Conteúdo | Usado por |
|---|---|---|---|
| 00 | Índice | Mapa da base, fontes e convenções | Todos |
| 01 | Contexto: empresa e mercado | História, produto, investidores, regiões, segmentos, demanda potencial | Todos |
| 02 | Marketing, vendas e demanda | Atributos de compra por segmento, preço, versão, propaganda, vendedores, prazo, pesquisas | Mercado |
| 03 | Operações e logística | Fábricas, capacidade, custos fixos e diretos, matriz de transferência, fornecedor terceirizado | Operações |
| 04 | Tecnologia e qualidade | P&D, versões, pipeline de qualidade, melhoria de processo | Tecnologia |
| 05 | Finanças | Linhas de crédito, prêmio de risco, aplicações, recebíveis, dividendos, impostos | Finanças |
| 06 | Simulador: telas e relatórios | Cada tela, cada campo de decisão, cada relatório, fluxo para salvar e enviar | Todos (operacional) |
| 07 | Parâmetros e fórmulas | Referência rápida de todos os números e fórmulas | Todos (cálculo) |
| 08 | Estado atual da equipe | Resultados, estoque, caixa, projeções e histórico (reescrito a cada rodada) | Todos |
| 09 | Arquitetura dos agentes | Ver [`arquitetura-agentes.md`](arquitetura-agentes.md) | Orquestração |
| 10 | Checklist e armadilhas | Roteiro antes de salvar e erros comuns | CEO |

## Método de construção
1. **Extração do manual:** texto via `pdftotext`; páginas com tabelas em imagem renderizadas (`pdftoppm`) e lidas visualmente.
2. **Exploração do simulador (somente leitura):** mapeamento de todas as telas, campos de decisão, avisos automáticos e dos relatórios PDF de cada rodada.
3. **Engenharia reversa de parâmetros:** cruzar DRE, balanço, fluxo de caixa e projeções para descobrir valores não publicados (por exemplo, custo de estocagem = despesa ÷ valor do estoque).
4. **Marcação de origem** em cada número: `[manual]`, `[observado]`, `[análise]`, `[premissa]`.
5. **Registro de contradições** do material oficial como perguntas ao professor, em vez de escolher uma versão em silêncio.
6. **Separação entre regra e estado:** os docs 01–07 mudam raramente; o doc 08 é reescrito a cada rodada.
