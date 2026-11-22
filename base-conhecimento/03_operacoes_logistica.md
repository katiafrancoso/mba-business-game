# 03 — Operações, produção e logística

## 1. Linha do tempo da produção (crítico)
- A construção ou expansão de fábrica vale **no mesmo trimestre** da decisão: a capacidade já está disponível para produzir.
- **O que é produzido em T só fica disponível para venda em T+1.**
- T1 (pré-operacional): escolher local, capacidade e volume. Não há vendas.
- **Kits da RoxConn chegam no mesmo trimestre do pedido**, a R$ 30 cada. É a única forma de "produzir para hoje".

## 2. Fábricas
- De 1 a 4 fábricas, no máximo uma por cidade. O limite é financeiro.
- Uma fábrica atende todas as praças, pagando transporte.
- Não é obrigatório produzir a 100%; o volume é decidido a cada trimestre.
- Na tela de Produção, o aumento de capacidade é escolhido num dropdown em **passos de 500 unidades, até +10.000 por decisão** [observado].

### Investimento para construir ou expandir (Tabela 4), por capacidade total da fábrica
| Capacidade (un./trimestre) | Investimento acumulado (R$) |
|---|---|
| até 2.000 | 75.000 |
| 2.001–4.000 | 135.000 |
| 4.001–6.000 | 186.000 |
| 6.001–8.000 | 232.000 |
| 8.001–10.000 | 277.500 |
| 10.001–12.000 | 324.000 |
| 12.001–14.000 | 371.000 |
| 14.001–16.000 | 420.000 |
| 16.001–18.000 | 472.500 |
| mais de 18.000 | 525.000 |
**Como calcular uma expansão: atenção, há ambiguidade.**
- **Leitura do manual (texto):** "construir ou expandir exigem os mesmos investimentos". No exemplo, expandir de 6.000 para 8.000 (+2.000) custa **R$ 75.000**, o mesmo valor da linha "até 2.000". Ou seja, **a expansão é cobrada pelo tamanho do acréscimo**, consultado na tabela.
- **Leitura alternativa:** diferença entre faixas (232.000 − 186.000 = R$ 46.000).
- [observado] A fábrica de BH com 10.000 custou R$ 277.500, que é exatamente a linha "8.001–10.000".
- [análise] Pela leitura do manual, expansões pequenas e fracionadas saem **mais caras por unidade** do que construir já com a capacidade certa (+2.000 por 75 mil = R$ 37,5/un.; +10.000 por 277,5 mil = R$ 27,75/un.). Antes de salvar, **confirme o valor na tela Projeções (Fluxo de caixa, linha "Aumento de capacidade instalada")**.

### Custo indireto (fixo) trimestral por fábrica (Tabela 5)
| Capacidade instalada | Custo fixo/trimestre (R$) |
|---|---|
| até 2.000 | 15.000 |
| 2.001–4.000 | 25.000 |
| 4.001–6.000 | 32.000 |
| 6.001–8.000 | 37.500 |
| 8.001–10.000 | 45.000 |
| 10.001–12.000 | 52.500 |
| 12.001–14.000 | 60.000 |
| 14.001–16.000 | 67.500 |
| 16.001–18.000 | 75.000 |
| mais de 18.000 | 82.500 |
- Depende da **capacidade instalada**, não do volume produzido.
- **Rateio:** a parcela usada vai para o custo do produto (CMV). A parcela ociosa vira **Despesa com Excesso de Capacidade** na DRE.
  - Exemplo: com utilização de 70%, 70% do custo fixo vai para os kits e 30% vira despesa.
  - **Se a fábrica não produzir nada no trimestre, 100% do custo fixo vira despesa** [observado: projeção do T2 com produção 0 = −R$ 45.000].

### Custo direto — CUF (Custo Unitário de Fabricação)
É afetado por 3 fatores:
1. **Localização:** com tudo o mais igual, **SP é a cidade mais barata e BS a mais cara** [manual].
2. **Tamanho da fábrica:** quanto maior a capacidade, menor o CUF, qualquer que seja o nível de atividade.
3. **Investimentos em melhoria de processo:** reduções cumulativas (ver `04_tecnologia_qualidade.md`).

**[observado]** Tela Tecnologia > Melhoria de Processo no T2: "CUF no trimestre" = SP 25,00 | BS 24,00 | CR 23,00 | **BH 15,00** (BH tem fábrica de 10.000; as demais cidades não têm fábrica).
- No relatório de Operações do T1, BH: **custo direto unitário R$ 15,00**, custo indireto alocado R$ 4,50/un. (36.000 / 8.000), **custo total unitário R$ 19,50**.
- Na imagem de exemplo do manual (outra simulação): SP 19,93 (já com R$ 5.000 de melhoria) | BS 24,00 | CR 23,00 | BH 22,00.
- [análise] Os valores das cidades sem fábrica parecem ser referências de uma fábrica pequena. O valor de 15,00 em BH reflete a escala de 10.000. O valor de SP = 25 contradiz o manual; confirme antes de decidir sobre uma nova fábrica.

### Depreciação [observado]
- Fábrica de R$ 277.500 → depreciação de **R$ 4.625/trimestre**, ou seja, 1,667% por trimestre (≈ 60 trimestres, 15 anos, linear).

### Desativação de fábrica
- Custa **R$ 25.000** no trimestre da desativação.
- Enquanto estiver parada: **50% do custo fixo por trimestre**, e a depreciação continua.
- A reativação não tem custo.

## 3. Estoques
- **Custo de manutenção de estoque [observado]: R$ 7.800 sobre um estoque de R$ 156.000 = 5% do valor do estoque por trimestre.** Não está no manual. O valor foi deduzido da projeção do T2 e deve ser verificado nos próximos trimestres.
- Os clientes funcionam quase em just-in-time. **Faltar produto** gera cancelamento, punição em redes sociais e **queda de demanda no trimestre seguinte**.

## 4. Logística (Manual §5)
- Transportadora **BPLT**: **R$ 3,00 por unidade transferida entre praças**, qualquer que seja a origem ou o destino. O preço pode subir no futuro.
- Entrega na própria praça onde há estoque: sem custo de transferência.
- As entregas ocorrem no mesmo trimestre da venda, se houver estoque.
- **Regra da matriz:**
  1. Cada praça atende primeiro com seu próprio estoque.
  2. Se faltar, a cidade com **maior estoque excedente** (depois de atender a própria demanda) envia para as cidades carentes, seguindo a **prioridade de destino** definida pela empresa.
  3. O processo se repete até atender tudo ou acabar o estoque.
- **Decisão:** a prioridade de destino de cada origem (tela Logística), para proteger as praças estratégicas.
- [observado] Prioridade padrão no T2: SP → (BS, CR, BH); BS → (SP, CR, BH); CR → (SP, BS, BH); BH → (SP, BS, CR). O aviso da tela Conclua diz "Não foram definidas as regras da matriz de logística".

## 5. Fornecedor terceirizado — RoxConn (Manual §5.2)
- **Compra antecipada:** qualquer quantidade, **entregue no mesmo trimestre** na cidade indicada, a **R$ 30,00 por unidade** (frete incluído). O preço pode mudar.
- Os kits chegam na versão básica, e as melhorias já desenvolvidas são adicionadas conforme a tela de Vendas.
- O serviço de "suprimento garantido" **ainda não está em operação**.
- No simulador, o campo aparece como "Compras emergenciais (unidades)" na tela Logística.
- [análise] Serve como seguro contra falta de produto. Com preço de R$ 50 no Básico, ainda há margem bruta (~R$ 20 antes de garantia e despesas).

## 6. Trade-offs a avaliar [análise]
- Uma fábrica grande (economia de escala no CUF e no custo fixo por unidade) mais frete de R$ 3/un. × várias fábricas menores perto de cada mercado.
- Capacidade ociosa custa caro: o custo fixo não alocado vira despesa.
- Produzir sem demanda gera custo de estoque (~5% por trimestre). Produzir de menos gera falta de produto e queda de demanda futura.
