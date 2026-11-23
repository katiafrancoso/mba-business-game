const pptxgen = require("pptxgenjs");
const { applyTheme } = require("./apply_theme.js") /* script do skill pptx */;

const THEME = {
  name: "Business Game Agentes",
  headFontFace: "Cambria",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "1B2430", lt1: "FFFFFF", dk2: "1F3A5F", lt2: "EEF3F8",
    accent1: "1F3A5F", accent2: "2A7F8E", accent3: "D08C1F", accent4: "E3F1F3",
    accent5: "FDF3E1", accent6: "5A6672", hlink: "2A7F8E", folHlink: "5A6672",
  },
};

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "Projeto Agêntico – Business Game TecTrain – Equipe 3";
pres.author = "Equipe 3 – IBMEC";
const C = pres.SchemeColor;
const NAVY = C.accent1, TEAL = C.accent2, AMBER = C.accent3, TEAL_BG = C.accent4, AMBER_BG = C.accent5, GREY = C.accent6;

// ---------- layouts ----------
pres.defineSlideMaster({
  title: "CAPA", background: { color: C.text2 },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.8, y: 2.0, w: 11.7, h: 1.9, fontFace: THEME.headFontFace, fontSize: 44, bold: true, color: C.background1, valign: "bottom", align: "left", margin: 0 }, text: "" } },
    { placeholder: { options: { name: "body", type: "body", x: 0.8, y: 4.1, w: 11.7, h: 1.6, fontSize: 20, color: C.background2, valign: "top", margin: 0 }, text: "" } },
  ],
});
pres.defineSlideMaster({
  title: "CONTEUDO", background: { color: C.background1 },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.35, w: 12.1, h: 0.9, fontFace: THEME.headFontFace, fontSize: 32, bold: true, color: C.text2, valign: "middle", align: "left", margin: 0 }, text: "" } },
    { text: { text: "Business Game TecTrain · Projeto Agêntico · Equipe 3", options: { x: 0.6, y: 7.0, w: 8, h: 0.3, fontSize: 10, color: GREY, margin: 0 } } },
  ],
  slideNumber: { x: 12.2, y: 7.0, w: 0.5, h: 0.3, fontSize: 10, color: GREY, align: "right" },
});

// ---------- helpers ----------
const tb = (s, text, o) => s.addText(text, Object.assign({ isTextBox: true, fontSize: 15, color: C.text1, margin: 0, valign: "top" }, o));
function card(s, x, y, w, h, fill, name) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.12, fill: { color: fill }, line: { color: fill }, objectName: name });
}
function circleNum(s, x, y, d, n, fill, size) {
  s.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: fill }, line: { color: fill } });
  tb(s, String(n), { x, y, w: d, h: d, fontSize: size || 18, bold: true, color: C.background1, align: "center", valign: "middle" });
}
function arrowR(s, x, y, w) {
  s.addShape(pres.shapes.RIGHT_ARROW, { x, y, w, h: 0.32, fill: { color: GREY }, line: { color: GREY } });
}
function arrowD(s, x, y, h) {
  s.addShape(pres.shapes.DOWN_ARROW, { x, y, w: 0.32, h, fill: { color: GREY }, line: { color: GREY } });
}
function slide(section, title) {
  const s = pres.addSlide({ masterName: "CONTEUDO", sectionTitle: section });
  s.addText(title, { placeholder: "title" });
  return s;
}

// ================= 1. CAPA =================
pres.addSection({ title: "Abertura" });
let s = pres.addSlide({ masterName: "CAPA", sectionTitle: "Abertura" });
s.addText("Um time de diretores virtuais para o Business Game", { placeholder: "title" });
s.addText("Modelo multiagente, acesso ao simulador pelo Chrome, harness e GitHub\nEquipe 3 · MBA IBMEC · Turma IBMEC-OL-Turma2NOV26", { placeholder: "body" });
s.addNotes("Abertura: em um dia montamos um sistema de agentes de IA que lê as regras do jogo e os relatórios do simulador e recomenda as decisões de cada trimestre. Vou mostrar o que fizemos, como funciona e como cada um de vocês pode usar.");

// ================= 2. DESAFIO =================
pres.addSection({ title: "Contexto" });
s = slide("Contexto", "O jogo tem decisões demais para cabeça e planilha");
const desafios = [
  ["Dezenas de variáveis", "Preço, vendedores, propaganda, produção, logística, P&D, qualidade e crédito, em 4 praças e 2 segmentos, todas interligadas."],
  ["Regras espalhadas", "Manual de 42 páginas com tabelas em imagem e 10 relatórios PDF por rodada no simulador."],
  ["Defasagens", "O que se produz hoje só vende no próximo trimestre; pesquisas chegam com atraso; caixa negativo vira empréstimo caro."],
];
desafios.forEach(([t, d], i) => {
  const x = 0.6 + i * 4.1;
  card(s, x, 1.7, 3.8, 3.9, C.background2, "desafio" + i);
  circleNum(s, x + 0.35, 2.05, 0.7, i + 1, i === 2 ? AMBER : TEAL, 20);
  tb(s, t, { x: x + 0.35, y: 3.0, w: 3.1, h: 0.6, fontSize: 20, bold: true, color: NAVY, fontFace: THEME.headFontFace });
  tb(s, d, { x: x + 0.35, y: 3.65, w: 3.1, h: 1.8, fontSize: 15 });
});
tb(s, "Objetivo: dar ao grupo uma visão integrada e números calculados, sem tirar de nós a decisão.", { x: 0.6, y: 6.0, w: 12.1, h: 0.5, fontSize: 17, italic: true, color: TEAL });
s.addNotes("Por que fizemos isso: o simulador tem muitas variáveis interligadas, as regras estão espalhadas e as defasagens (produção, pesquisa, caixa) são fáceis de errar.");

// ================= 3. JORNADA =================
s = slide("Contexto", "O que fizemos, em 6 passos");
const passos = [
  ["Ler as fontes", "Manual + simulador via Chrome"],
  ["Base de conhecimento", "11 documentos temáticos"],
  ["Agentes", "6 diretores virtuais"],
  ["Rodada T2", "Pacote de decisões"],
  ["Harness", "Regras de operação"],
  ["GitHub", "Versão e portfólio"],
];
passos.forEach(([t, d], i) => {
  const x = 0.6 + i * 2.05;
  circleNum(s, x + 0.6, 2.0, 0.85, i + 1, i < 4 ? TEAL : NAVY, 22);
  tb(s, t, { x, y: 3.1, w: 1.95, h: 0.8, fontSize: 17, bold: true, color: NAVY, align: "center", valign: "top" });
  tb(s, d, { x, y: 3.9, w: 1.95, h: 0.9, fontSize: 14, color: GREY, align: "center" });
  if (i < 5) s.addShape(pres.shapes.LINE, { x: x + 1.5, y: 2.42, w: 1.1, h: 0, line: { color: GREY, width: 1.5, endArrowType: "triangle" } });
});
card(s, 0.6, 5.2, 12.1, 1.3, AMBER_BG, "regra");
tb(s, [{ text: "Princípio que guia tudo: ", options: { bold: true, color: AMBER } }, { text: "os agentes recomendam, o grupo decide. A IA nunca clica em Salvar no simulador." }],
  { x: 0.9, y: 5.45, w: 11.5, h: 0.8, fontSize: 18, valign: "middle" });
s.addNotes("Linha do tempo do trabalho. Destaque para o princípio: a IA só lê o simulador e recomenda; quem decide e salva somos nós.");

// ================= 4. CHROME =================
pres.addSection({ title: "Como construímos" });
s = slide("Como construímos", "A IA leu o simulador direto no nosso Chrome");
const fluxoChrome = [
  ["Painel do Claude no Chrome", "A extensão Claude in Chrome usa a sessão já logada no simulador"],
  ["Navegação pelas telas", "Prepare-se, Análise, as 6 abas de Decisões, Projeções e Conclua"],
  ["Leitura dos relatórios", "Abriu os 10 PDFs do T1 e leu cada um no visualizador do Chrome"],
  ["Engenharia reversa", "Cruzou DRE, balanço e projeções para achar números que o manual não traz"],
];
fluxoChrome.forEach(([t, d], i) => {
  const y = 1.55 + i * 1.3;
  circleNum(s, 0.6, y + 0.1, 0.7, i + 1, TEAL, 18);
  tb(s, t, { x: 1.55, y, w: 5.6, h: 0.45, fontSize: 18, bold: true, color: NAVY });
  tb(s, d, { x: 1.55, y: y + 0.45, w: 5.6, h: 0.7, fontSize: 15, color: C.text1 });
});
card(s, 7.7, 1.55, 5.0, 5.0, C.background2, "stats");
const stats = [["42", "páginas do manual lidas, inclusive tabelas em imagem"], ["10", "relatórios PDF do T1 analisados"], ["6", "parâmetros ocultos descobertos (ex.: estoque custa ~5%/trimestre)"], ["0", "cliques em Salvar: acesso somente leitura"]];
stats.forEach(([n, l], i) => {
  const y = 1.8 + i * 1.18;
  tb(s, n, { x: 8.0, y, w: 1.3, h: 0.9, fontSize: 40, bold: true, color: i === 3 ? AMBER : TEAL, fontFace: THEME.headFontFace, valign: "middle" });
  tb(s, l, { x: 9.35, y, w: 3.1, h: 0.9, fontSize: 14, valign: "middle" });
});
s.addNotes("Como os dados foram coletados: a extensão Claude in Chrome trabalha dentro do navegador já logado no simulador. Ela navegou pelas telas e leu os relatórios, sem alterar nada. O site não tem vídeos. Exemplos de números que não estão no manual: custo de estoque de cerca de 5% por trimestre e imposto de 34%.");

// ================= 5. BASE =================
s = slide("Como construímos", "Uma base de conhecimento única para todos os agentes");
const docs = ["Contexto da empresa e do mercado", "Marketing, vendas e demanda", "Operações e logística", "Tecnologia e qualidade", "Finanças", "Telas e relatórios do simulador", "Parâmetros e fórmulas", "Estado atual da Equipe 3", "Arquitetura dos agentes", "Checklist e armadilhas"];
docs.forEach((d, i) => {
  const col = i % 2, row = Math.floor(i / 2);
  const x = 0.6 + col * 3.55, y = 1.55 + row * 0.98;
  card(s, x, y, 3.4, 0.8, i === 7 ? AMBER_BG : TEAL_BG, "doc" + i);
  tb(s, String(i + 1).padStart(2, "0"), { x: x + 0.15, y, w: 0.55, h: 0.8, fontSize: 16, bold: true, color: i === 7 ? AMBER : TEAL, valign: "middle" });
  tb(s, d, { x: x + 0.7, y, w: 2.6, h: 0.8, fontSize: 14, valign: "middle" });
});
tb(s, "Todo número tem origem marcada", { x: 8.2, y: 1.55, w: 4.5, h: 0.5, fontSize: 20, bold: true, color: NAVY, fontFace: THEME.headFontFace });
const tags = [["[manual]", "regra oficial do jogo", NAVY], ["[observado]", "visto no simulador", TEAL], ["[análise]", "inferência nossa", GREY], ["[premissa]", "suposição a validar", AMBER]];
tags.forEach(([t, d, c], i) => {
  const y = 2.3 + i * 0.95;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 8.2, y, w: 1.7, h: 0.6, rectRadius: 0.1, fill: { color: c }, line: { color: c } });
  tb(s, t, { x: 8.2, y, w: 1.7, h: 0.6, fontSize: 14, bold: true, color: C.background1, align: "center", valign: "middle" });
  tb(s, d, { x: 10.1, y, w: 2.6, h: 0.6, fontSize: 15, valign: "middle" });
});
tb(s, "Regras mudam pouco (docs 1–7); o estado da empresa é reescrito a cada rodada (doc 8).", { x: 8.2, y: 6.1, w: 4.5, h: 0.6, fontSize: 13, italic: true, color: GREY });
s.addNotes("A base de conhecimento tem 11 documentos (índice + 10 temáticos). Cada número traz a origem marcada, para sabermos em que confiar. O doc 8 (estado atual) é reescrito a cada rodada.");

// ================= 6. MODELO MULTIAGENTE =================
pres.addSection({ title: "Modelo multiagente" });
s = slide("Modelo multiagente", "Cinco especialistas, um integrador e o grupo decide");
// inputs
card(s, 0.9, 1.45, 5.5, 0.75, C.background2, "in1"); tb(s, "Base de conhecimento", { x: 0.9, y: 1.45, w: 5.5, h: 0.75, fontSize: 16, bold: true, color: NAVY, align: "center", valign: "middle" });
card(s, 6.9, 1.45, 5.5, 0.75, C.background2, "in2"); tb(s, "Dados do simulador (relatórios + estado)", { x: 6.9, y: 1.45, w: 5.5, h: 0.75, fontSize: 16, bold: true, color: NAVY, align: "center", valign: "middle" });
const ags = ["Inteligência Competitiva", "Mercado & Marketing", "Tecnologia & Qualidade", "Operações & Logística", "Finanças"];
ags.forEach((a, i) => {
  const x = 0.6 + i * 2.46;
  arrowD(s, x + 1.03, 2.3, 0.4);
  card(s, x, 2.8, 2.3, 1.0, TEAL, "ag" + i);
  tb(s, a, { x: x + 0.1, y: 2.8, w: 2.1, h: 1.0, fontSize: 15, bold: true, color: C.background1, align: "center", valign: "middle" });
});
arrowD(s, 6.5, 3.9, 0.45);
card(s, 3.9, 4.45, 5.5, 0.9, NAVY, "ceo");
tb(s, "Agente Integrador (CEO): consolida, checa coerência, resolve conflitos", { x: 4.0, y: 4.45, w: 5.3, h: 0.9, fontSize: 15, bold: true, color: C.background1, align: "center", valign: "middle" });
arrowD(s, 6.5, 5.45, 0.4);
card(s, 3.9, 5.95, 5.5, 0.8, AMBER_BG, "equipe");
tb(s, "Equipe discute, decide e salva no simulador", { x: 3.9, y: 5.95, w: 5.5, h: 0.8, fontSize: 16, bold: true, color: AMBER, align: "center", valign: "middle" });
s.addNotes("Arquitetura: cada agente é um diretor virtual especialista que lê a mesma base. Ordem: Competitiva e Mercado primeiro; Tecnologia; Operações usa a demanda do Mercado; Finanças junta tudo e projeta o caixa; o CEO consolida e verifica a coerência. No fim, quem decide é o grupo.");

// ================= 7. OS AGENTES =================
s = slide("Modelo multiagente", "O que cada agente faz");
const rows = [
  ["Agente", "Pergunta que responde", "O que entrega"],
  ["Mercado & Marketing", "Onde vender, a que preço e com quanto esforço?", "Vendedores, preço, propaganda, prazo e demanda estimada em 3 cenários"],
  ["Operações & Logística", "Quanto produzir e como abastecer cada praça?", "Produção para o próximo trimestre, matriz de transferência, compras de terceiros"],
  ["Tecnologia & Qualidade", "Quando ter produto melhor e com menos defeito?", "Plano de P&D, pipeline de qualidade e redução de custo com payback"],
  ["Finanças", "O plano cabe no caixa? Como financiar?", "Fluxo de caixa e DRE projetados, crédito recomendado, alertas"],
  ["Inteligência Competitiva", "O que os 7 concorrentes devem fazer?", "Perfis prováveis e o que monitorar no relatório da rodada"],
  ["Integrador (CEO)", "Tudo isso fecha junto?", "Pacote final por tela, contingência e pontos para o grupo decidir"],
];
s.addTable(rows.map((r, ri) => r.map((c, ci) => ({
  text: c, options: {
    bold: ri === 0 || ci === 0, color: ri === 0 ? C.background1 : (ci === 0 ? NAVY : C.text1),
    fill: { color: ri === 0 ? NAVY : (ri % 2 === 0 ? C.background2 : C.background1) }, fontSize: 14, valign: "middle",
  },
}))), { x: 0.6, y: 1.5, w: 12.1, colW: [2.9, 4.2, 5.0], rowH: 0.68, border: { type: "solid", pt: 0.5, color: "C9D3DD" }, margin: 0.08 });
s.addNotes("Cada agente responde a uma pergunta de negócio e entrega números exatos para os campos do simulador, com justificativa, impacto no caixa e risco.");

// ================= 8. RESULTADO T2 =================
s = slide("Modelo multiagente", "Primeira rodada: o gargalo do T2 é caixa, não lucro");
card(s, 0.6, 1.55, 3.8, 2.4, TEAL_BG, "kpi1");
tb(s, "+R$ 16 mil", { x: 0.8, y: 1.75, w: 3.4, h: 1.0, fontSize: 40, bold: true, color: TEAL, fontFace: THEME.headFontFace });
tb(s, "resultado operacional estimado (cenário base, ~7.500 kits)", { x: 0.8, y: 2.8, w: 3.4, h: 1.0, fontSize: 14 });
card(s, 0.6, 4.2, 3.8, 2.4, AMBER_BG, "kpi2");
tb(s, "−R$ 50 mil", { x: 0.8, y: 4.4, w: 3.4, h: 1.0, fontSize: 40, bold: true, color: AMBER, fontFace: THEME.headFontFace });
tb(s, "caixa final sem financiamento: o simulador cairia no empréstimo de emergência", { x: 0.8, y: 5.45, w: 3.4, h: 1.0, fontSize: 14 });
tb(s, "Recomendação consolidada pelo CEO", { x: 4.9, y: 1.55, w: 7.8, h: 0.5, fontSize: 20, bold: true, color: NAVY, fontFace: THEME.headFontFace });
const recs = [
  "Entrar nas 4 praças: vendedores SP 3, BS 2, CR 2, BH 2",
  "Preços de referência: Básico R$ 50, Premium R$ 60",
  "Propaganda de R$ 30 mil; Premium priorizado em Curitiba",
  "Produzir 9.000 kits em BH para vender no T3",
  "6 pesquisadores, inspeção de qualidade e R$ 10 mil em redução de custo",
  "Empréstimo de longo prazo de R$ 100 mil, ou 100% à vista se o professor não liberar",
];
tb(s, recs.map((r, i) => ({ text: r, options: { bullet: true, breakLine: i < recs.length - 1 } })), { x: 4.9, y: 2.2, w: 7.8, h: 3.4, fontSize: 16, paraSpaceAfter: 8 });
tb(s, "4 pontos ficaram para o grupo decidir: prazo de recebimento, preço do Premium, velocidade do P&D e pesquisa de demanda.", { x: 4.9, y: 5.85, w: 7.8, h: 0.75, fontSize: 14, italic: true, color: GREY });
s.addNotes("O principal insight da primeira rodada: o trimestre fecha perto do zero a zero em resultado, mas o caixa ficaria negativo. Isso mudou a pauta de 'qual preço' para 'como financiar a entrada no mercado'. Limitação: o modelo não calcula quanto a demanda responde a preço ou vendedores; isso será calibrado com o resultado do T2.");

// ================= 9. HARNESS =================
pres.addSection({ title: "Harness e GitHub" });
s = slide("Harness e GitHub", "O harness transforma conversas soltas em um sistema");
tb(s, "Sem harness, cada conversa com a IA começa do zero e o que foi decidido se perde no histórico do chat. O harness é o manual de operação do projeto.", { x: 0.6, y: 1.45, w: 12.1, h: 0.8, fontSize: 16, color: C.text1 });
const hz = [
  ["Comandos", "/status, /nova-rodada, /simular, /registrar-decisao, /pos-rodada, /publicar"],
  ["Templates", "Mesmo formato em todas as rodadas, para comparar previsto × realizado"],
  ["Persistência", "Tudo que importa vira documento no Projeto, com changelog"],
  ["Modelo de simulação", "Python que projeta caixa e DRE: número calculado, não chutado"],
  ["Registros", "Log de decisões, perguntas ao professor, lições aprendidas"],
  ["Instruções do Projeto", "Toda conversa nova já nasce seguindo essas regras"],
];
hz.forEach(([t, d], i) => {
  const col = i % 3, row = Math.floor(i / 3);
  const x = 0.6 + col * 4.1, y = 2.45 + row * 2.1;
  card(s, x, y, 3.85, 1.9, C.background2, "hz" + i);
  circleNum(s, x + 0.25, y + 0.25, 0.55, i + 1, TEAL, 16);
  tb(s, t, { x: x + 0.95, y: y + 0.25, w: 2.75, h: 0.55, fontSize: 17, bold: true, color: NAVY, valign: "middle" });
  tb(s, d, { x: x + 0.25, y: y + 0.95, w: 3.4, h: 0.85, fontSize: 14 });
});
s.addNotes("Harness: o conjunto de regras que faz qualquer conversa no Projeto se comportar igual. Comandos padronizados, templates, protocolo de salvamento, modelo de simulação e registros. Com as instruções do Projeto, toda conversa nova já segue isso.");

// ================= 10. CICLO =================
s = slide("Harness e GitHub", "O ciclo de cada trimestre");
const ciclo = [["Pós-rodada", "/pos-rodada", "IA"], ["Nova rodada", "/nova-rodada", "IA"], ["Reunião", "grupo discute", "Grupo"], ["Registrar", "/registrar-decisao", "IA"], ["Simulador", "uma pessoa salva", "Grupo"], ["Processamento", "professor", "Grupo"]];
ciclo.forEach(([t, d, who], i) => {
  const x = 0.6 + i * 2.1;
  const ia = who === "IA";
  card(s, x, 2.2, 1.8, 2.0, ia ? TEAL_BG : AMBER_BG, "ciclo" + i);
  tb(s, String(i + 1), { x, y: 2.3, w: 1.8, h: 0.6, fontSize: 26, bold: true, color: ia ? TEAL : AMBER, align: "center", fontFace: THEME.headFontFace });
  tb(s, t, { x: x + 0.05, y: 2.95, w: 1.7, h: 0.5, fontSize: 16, bold: true, color: NAVY, align: "center" });
  tb(s, d, { x: x + 0.05, y: 3.5, w: 1.7, h: 0.6, fontSize: 13, color: GREY, align: "center" });
  if (i < 5) arrowR(s, x + 1.82, 3.05, 0.26);
});
s.addShape(pres.shapes.LINE, { x: 11.7, y: 4.35, w: 0, h: 0.6, line: { color: GREY, width: 1.5 } });
s.addShape(pres.shapes.LINE, { x: 1.5, y: 4.95, w: 10.2, h: 0, line: { color: GREY, width: 1.5 } });
s.addShape(pres.shapes.LINE, { x: 1.5, y: 4.35, w: 0, h: 0.6, line: { color: GREY, width: 1.5, beginArrowType: "triangle" } });
tb(s, "volta ao passo 1 no trimestre seguinte", { x: 4.2, y: 5.05, w: 5, h: 0.4, fontSize: 13, italic: true, color: GREY, align: "center" });
card(s, 0.6, 5.75, 0.4, 0.4, TEAL_BG, "leg1"); tb(s, "IA executa", { x: 1.1, y: 5.75, w: 2, h: 0.4, fontSize: 14, valign: "middle" });
card(s, 3.1, 5.75, 0.4, 0.4, AMBER_BG, "leg2"); tb(s, "Grupo / professor", { x: 3.6, y: 5.75, w: 3, h: 0.4, fontSize: 14, valign: "middle" });
tb(s, "Ao fim de cada passo que salva algo, uma nova versão vai para o GitHub.", { x: 6.6, y: 5.75, w: 6.1, h: 0.4, fontSize: 14, italic: true, color: TEAL, valign: "middle" });
s.addNotes("Ciclo trimestral: a IA lê os resultados e gera as recomendações; o grupo discute; a IA registra a decisão; uma pessoa salva no simulador; o professor processa. E recomeça.");

// ================= 11. GITHUB =================
s = slide("Harness e GitHub", "Tudo versionado no GitHub: memória do grupo e portfólio");
tb(s, "github.com/katiafrancoso/mba-business-game", { x: 0.6, y: 1.45, w: 12.1, h: 0.6, fontSize: 22, bold: true, color: TEAL, hyperlink: { url: "https://github.com/katiafrancoso/mba-business-game" } });
const pastas = [["base-conhecimento/", "regras e estado da empresa"], ["harness/", "operação, comandos, modelo"], ["rodadas/T2, T3…", "saída dos agentes por trimestre"], ["registro/", "decisões, perguntas, lições"], ["docs/", "arquitetura e método"], ["entregaveis/", "PDF e materiais do grupo"]];
pastas.forEach(([p, d], i) => {
  const y = 2.35 + i * 0.68;
  card(s, 0.6, y, 2.9, 0.55, NAVY, "pasta" + i);
  tb(s, p, { x: 0.75, y, w: 2.7, h: 0.55, fontSize: 14, bold: true, color: C.background1, valign: "middle", fontFace: "Courier New" });
  tb(s, d, { x: 3.7, y, w: 3.2, h: 0.55, fontSize: 14, valign: "middle" });
});
card(s, 7.4, 2.35, 5.3, 3.95, C.background2, "regrasgit");
tb(s, "Regras de versionamento", { x: 7.7, y: 2.55, w: 4.8, h: 0.5, fontSize: 18, bold: true, color: NAVY, fontFace: THEME.headFontFace });
const gitr = ["Toda evolução do projeto vira um commit", "Mensagens padronizadas: tipo(escopo): descrição", "Tag ao fechar cada trimestre (ex.: T2-fechado)", "Espelho exato das pastas do Projeto no Claude", "README de portfólio, pronto para o LinkedIn"];
tb(s, gitr.map((r, i) => ({ text: r, options: { bullet: true, breakLine: i < gitr.length - 1 } })), { x: 7.7, y: 3.15, w: 4.8, h: 3.0, fontSize: 15, paraSpaceAfter: 8 });
s.addNotes("O GitHub guarda o histórico completo e serve de portfólio. A cada evolução do projeto, a IA publica uma nova versão automaticamente, com mensagens padronizadas e uma tag no fim de cada trimestre.");

// ================= 12. PRÓXIMOS PASSOS =================
pres.addSection({ title: "Próximos passos" });
s = pres.addSlide({ masterName: "CAPA", sectionTitle: "Próximos passos" });
s.addText("Próximos passos do grupo", { placeholder: "title" });
const prox = [
  "Hoje: pedir ao professor o limite de crédito e o critério de avaliação",
  "Reunião: decidir os 4 pontos em aberto do T2 e registrar com /registrar-decisao T2",
  "Uma pessoa salva no simulador, conferindo Projeções e Conclua",
  "Depois do processamento: /pos-rodada T2 e /nova-rodada T3",
];
s.addText(prox.map((r, i) => ({ text: r, options: { bullet: true, breakLine: i < prox.length - 1 } })), { placeholder: "body", fontSize: 18, paraSpaceAfter: 6 });
s.addNotes("Fechamento: o que precisamos de cada um. Os documentos estão no Projeto Business Game do Claude e no GitHub.");

(async () => {
  await pres.writeFile({ fileName: "Projeto_Agentico_Business_Game_Equipe3.pptx" });
  await applyTheme("Projeto_Agentico_Business_Game_Equipe3.pptx", THEME);
  console.log("ok");
})();
