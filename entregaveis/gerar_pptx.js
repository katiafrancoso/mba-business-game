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


// 1. CAPA
pres.addSection({ title: "Resumo" });
let s = pres.addSlide({ masterName: "CAPA", sectionTitle: "Resumo" });
s.addText("Um time de diretores virtuais para o Business Game", { placeholder: "title" });
s.addText("Multiagentes · Chrome · Harness · GitHub\nEquipe 3 · MBA IBMEC", { placeholder: "body" });
s.addNotes("Em um dia montamos agentes de IA que leem o jogo e recomendam as decisões de cada trimestre. A IA recomenda; o grupo decide.");

// 2. O QUE FIZEMOS
s = slide("Resumo", "O que fizemos");
const passos = [["Lemos tudo", "Manual + simulador via Chrome"], ["Base", "11 documentos"], ["Agentes", "6 diretores virtuais"], ["T2", "Decisões recomendadas"], ["Harness", "Regras de operação"], ["GitHub", "Versões e portfólio"]];
passos.forEach(([t, d], i) => {
  const x = 0.6 + i * 2.05;
  circleNum(s, x + 0.6, 2.1, 0.85, i + 1, i < 4 ? TEAL : NAVY, 22);
  tb(s, t, { x, y: 3.2, w: 1.95, h: 0.5, fontSize: 18, bold: true, color: NAVY, align: "center" });
  tb(s, d, { x, y: 3.75, w: 1.95, h: 0.8, fontSize: 14, color: GREY, align: "center" });
  if (i < 5) s.addShape(pres.shapes.LINE, { x: x + 1.5, y: 2.52, w: 1.1, h: 0, line: { color: GREY, width: 1.5, endArrowType: "triangle" } });
});
card(s, 0.6, 5.2, 12.1, 1.1, AMBER_BG, "regra");
tb(s, [{ text: "Regra de ouro: ", options: { bold: true, color: AMBER } }, { text: "a IA recomenda, o grupo decide. A IA nunca salva nada no simulador." }], { x: 0.9, y: 5.2, w: 11.5, h: 1.1, fontSize: 18, valign: "middle" });
s.addNotes("Seis passos, de ler as fontes até publicar no GitHub.");

// 3. CHROME
s = slide("Resumo", "A IA leu o simulador pelo nosso Chrome");
tb(s, "A extensão Claude in Chrome usou a sessão já logada, percorreu todas as telas e leu os relatórios em PDF, somente leitura.", { x: 0.6, y: 1.5, w: 12.1, h: 0.9, fontSize: 18 });
const stats = [["42", "páginas do manual"], ["10", "relatórios lidos"], ["6", "números ocultos descobertos"], ["0", "cliques em Salvar"]];
stats.forEach(([n, l], i) => {
  const x = 0.6 + i * 3.08;
  card(s, x, 2.8, 2.85, 2.6, i === 3 ? AMBER_BG : TEAL_BG, "stat" + i);
  tb(s, n, { x, y: 3.0, w: 2.85, h: 1.3, fontSize: 60, bold: true, color: i === 3 ? AMBER : TEAL, align: "center", valign: "middle", fontFace: THEME.headFontFace });
  tb(s, l, { x: x + 0.2, y: 4.35, w: 2.45, h: 0.8, fontSize: 16, align: "center" });
});
s.addNotes("Exemplos de números que o manual não traz: estoque custa ~5% por trimestre; imposto de 34%.");

// 4. MULTIAGENTE
s = slide("Resumo", "Cinco especialistas, um integrador e o grupo decide");
const ags = ["Concorrência", "Mercado", "Tecnologia", "Operações", "Finanças"];
ags.forEach((a, i) => {
  const x = 0.6 + i * 2.46;
  card(s, x, 1.7, 2.3, 1.0, TEAL, "ag" + i);
  tb(s, a, { x, y: 1.7, w: 2.3, h: 1.0, fontSize: 18, bold: true, color: C.background1, align: "center", valign: "middle" });
  arrowD(s, x + 1.0, 2.8, 0.45);
});
card(s, 0.6, 3.4, 12.1, 1.0, NAVY, "ceo");
tb(s, "CEO integrador: junta tudo, checa se fecha (estoque, caixa, preço) e monta o pacote", { x: 0.8, y: 3.4, w: 11.7, h: 1.0, fontSize: 18, bold: true, color: C.background1, align: "center", valign: "middle" });
arrowD(s, 6.5, 4.5, 0.45);
card(s, 3.9, 5.1, 5.5, 1.0, AMBER_BG, "equipe");
tb(s, "O grupo decide e salva", { x: 3.9, y: 5.1, w: 5.5, h: 1.0, fontSize: 18, bold: true, color: AMBER, align: "center", valign: "middle" });
s.addNotes("Todos leem a mesma base de conhecimento. Finanças roda depois dos outros porque precisa de todos os custos.");

// 5. HARNESS + GITHUB
s = slide("Resumo", "Harness e GitHub: nada se perde");
card(s, 0.6, 1.5, 5.9, 3.9, C.background2, "harness");
tb(s, "Harness", { x: 0.9, y: 1.7, w: 5.3, h: 0.6, fontSize: 22, bold: true, color: NAVY, fontFace: THEME.headFontFace });
const h = ["Comandos: /nova-rodada, /simular, /registrar-decisao", "Mesmo formato em todas as rodadas", "Tudo importante vira documento", "Toda conversa nova segue as regras"];
tb(s, h.map((r, i) => ({ text: r, options: { bullet: true, breakLine: i < h.length - 1 } })), { x: 0.9, y: 2.45, w: 5.3, h: 2.8, fontSize: 17, paraSpaceAfter: 10 });
card(s, 6.8, 1.5, 5.9, 3.9, C.background2, "github");
tb(s, "GitHub", { x: 7.1, y: 1.7, w: 5.3, h: 0.6, fontSize: 22, bold: true, color: NAVY, fontFace: THEME.headFontFace });
const g = ["Cada evolução vira uma versão", "Uma tag por trimestre fechado", "Histórico para o grupo", "Portfólio para o LinkedIn"];
tb(s, g.map((r, i) => ({ text: r, options: { bullet: true, breakLine: i < g.length - 1 } })), { x: 7.1, y: 2.45, w: 5.3, h: 2.1, fontSize: 17, paraSpaceAfter: 10 });
tb(s, "github.com/katiafrancoso/mba-business-game", { x: 7.1, y: 4.6, w: 5.4, h: 0.6, fontSize: 15, bold: true, color: TEAL, hyperlink: { url: "https://github.com/katiafrancoso/mba-business-game" } });
s.addNotes("O harness é o manual de operação: garante que qualquer conversa se comporte igual e salve tudo. O GitHub guarda as versões e serve de portfólio.");

// 6. T2 + PRÓXIMOS PASSOS
s = pres.addSlide({ masterName: "CAPA", sectionTitle: "Resumo" });
s.addText("T2: o desafio é caixa, não lucro", { placeholder: "title" });
const prox = ["Resultado estimado de +R$ 16 mil, mas o caixa fica em −R$ 50 mil sem crédito", "Hoje: pedir ao professor o empréstimo e o critério de avaliação", "Reunião: decidir os 4 pontos em aberto e registrar", "Uma pessoa salva no simulador"];
s.addText(prox.map((r, i) => ({ text: r, options: { bullet: true, breakLine: i < prox.length - 1 } })), { placeholder: "body", fontSize: 18, paraSpaceAfter: 6 });
s.addNotes("Recomendação: entrar nas 4 praças, preços 50/60, produzir 9.000 kits e financiar com longo prazo de R$ 100 mil (ou vender 100% à vista).");

(async () => {
  await pres.writeFile({ fileName: "Projeto_Agentico_Business_Game_Equipe3.pptx" });
  await applyTheme("Projeto_Agentico_Business_Game_Equipe3.pptx", THEME);
  console.log("ok");
})();
