# Log de acesso ao simulador (via navegador)

> Registro do que a IA fez no simulador TecTrain (`bm.tectrain.com.br`) e do procedimento para repetir a leitura nas próximas rodadas. **Todo acesso é somente leitura.**

## Sessão 1 — 22/11/2026 (T2 aberto, relatórios do T1 disponíveis)
**Ferramenta:** extensão **Claude in Chrome**, pelo painel lateral do Chrome da Kátia, já logado no simulador (turma IBMEC-OL-Turma2NOV26, Equipe 3). Nenhum login nem senha foi digitado pela IA.

### Páginas visitadas
| Página | URL | O que foi lido |
|---|---|---|
| Prepare-se | `/Preparese` | Demanda potencial do T2 por praça e segmento (60.018 kits no mercado) |
| Análise | `/Analise` | Lista dos 10 relatórios do T1 e os links dos PDFs |
| Decisões › Vendas | `/Planeje/Vendas` | Campos de vendedores, preço, versão, demanda; indicadores (lucro projetado de −R$ 58,5 mil se nada for decidido) |
| Decisões › Marketing | `/Planeje/Marketing` | Propaganda, política de recebimento, prioridade por praça, compra de pesquisas |
| Decisões › Logística | `/Planeje/Logistica` | Prioridade de transferência padrão, compras emergenciais |
| Decisões › Produção | `/Planeje/Producao` | Capacidade atual (BH 10.000), opções de aumento (passos de 500 até +10.000), indicadores |
| Decisões › Tecnologia e Processos | `/Planeje/TecnologiaProcessos` | Versão 0, custo para acelerar o P&D (R$ 40 mil), CUF por cidade (SP 25, BS 24, CR 23, BH 15) |
| Decisões › Finanças | `/Planeje/Financas` | Estrutura das 7 sub-abas; nenhum limite de crédito aprovado |
| Projeções | `/Projecoes`, `/Projecoes/Demonstracao`, `/Projecoes/Indicadores` | DRE e indicadores do T2 com as decisões atuais (vazias): empréstimo de emergência de R$ 20,3 mil |
| Conclua | `/Conclua` | Avisos automáticos e revisão das decisões |
| Mensagens | `/Mensagem` | Nenhuma mensagem do instrutor |
| Suporte | `/Home/SuporteTecnico` | Formulário de contato com a professora |
| Ajuda | `/Content/manual_part_bm.pdf` | Mesmo manual anexado pela equipe |

### Relatórios do T1 lidos (10 PDFs)
Indicadores de Mercado (8 equipes) · Operações · Logística · Demonstração de Resultado · Balanço · Fluxo de Caixa · Fontes e Usos · Resumo de Desempenho Financeiro · Demanda Projetada Potencial · Decisões Operacionais da Empresa.

### Como foi feita a leitura
- **Telas:** leitura do texto da página e das tabelas por script de leitura (sem alterar nada).
- **PDFs:** o texto não pôde ser extraído direto, e a tentativa de carregar um leitor de PDF externo dentro da página foi **bloqueada pelas permissões** (corretamente). Por isso cada PDF foi aberto no visualizador do Chrome e lido por **capturas ampliadas da tela**.
- **Dicas de ajuda ("?")** na tela de Tecnologia: lidas passando o mouse.
- **Não há vídeos** no site.

### O que NÃO foi feito
- Nenhum clique em **Modificar**, **Salvar** ou **enviar**. Nenhuma decisão foi alterada.
- Nenhum formulário preenchido (nem o de Suporte).
- Nenhum download de arquivo para o computador.
- Ao terminar, a aba voltou para a página Prepare-se.

### Principais descobertas da sessão
Parâmetros que o manual não traz (detalhes em `registro/licoes_aprendidas.md`): custo de estoque de ~5% por trimestre, imposto de 34%, CUF da fábrica de BH de R$ 15,00, depreciação de 1,667% por trimestre, ociosidade de 100% do custo fixo com produção zero, emergência a ~5,4% por trimestre. Também: as 8 equipes estavam idênticas após o T1.

---

## Procedimento para as próximas rodadas (`/pos-rodada Tn`)
1. A equipe abre o simulador no Chrome, já logada, e chama o Claude no painel da extensão (ou anexa os PDFs no chat, se não houver navegador).
2. **Análise:** selecionar o trimestre processado e ler os 10 relatórios, nesta ordem de prioridade: Indicadores de Mercado → Resumo Financeiro → DRE → Fluxo de Caixa → Logística → Operações → Demanda Projetada → Balanço → Fontes e Usos → Decisões Operacionais.
3. **Prepare-se:** copiar a demanda potencial do novo trimestre.
4. **Decisões › Tecnologia** e **Finanças:** conferir versão e % do P&D, CUF por cidade, limites de crédito aprovados e taxas do trimestre.
5. **Mensagens:** verificar se o instrutor escreveu algo (por exemplo, resposta ao pedido de crédito).
6. Registrar aqui uma nova sessão (data, páginas, descobertas) e seguir o `/pos-rodada`.
7. **Nunca** clicar em Modificar, Salvar ou enviar. Quem registra decisões é a equipe.
