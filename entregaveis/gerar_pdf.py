from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether, NextPageTemplate)
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Polygon
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DVI", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("DV", normal="DV", bold="DVB", italic="DVI", boldItalic="DVB")

NAVY = colors.HexColor("#1F3A5F")
TEAL = colors.HexColor("#2A7F8E")
LIGHT = colors.HexColor("#EEF3F8")
LIGHT2 = colors.HexColor("#F7F9FB")
GREY = colors.HexColor("#5A6672")
AMBER = colors.HexColor("#B7791F")
AMBERBG = colors.HexColor("#FDF6E7")
LINE = colors.HexColor("#C9D3DD")

W, H = A4
M = 2.0 * cm

st = {
    "body": ParagraphStyle("body", fontName="DV", fontSize=10.5, leading=15, textColor=colors.HexColor("#222")),
    "small": ParagraphStyle("small", fontName="DV", fontSize=9, leading=12, textColor=GREY),
    "cell": ParagraphStyle("cell", fontName="DV", fontSize=9, leading=11.5),
    "cellb": ParagraphStyle("cellb", fontName="DVB", fontSize=9, leading=11.5),
    "cellh": ParagraphStyle("cellh", fontName="DVB", fontSize=9, leading=11.5, textColor=colors.white),
    "h1": ParagraphStyle("h1", fontName="DVB", fontSize=17, leading=22, textColor=NAVY, spaceBefore=4, spaceAfter=8),
    "h2": ParagraphStyle("h2", fontName="DVB", fontSize=12.5, leading=17, textColor=TEAL, spaceBefore=10, spaceAfter=5),
    "bullet": ParagraphStyle("bullet", fontName="DV", fontSize=10.5, leading=15, leftIndent=14, bulletIndent=4),
    "callout": ParagraphStyle("callout", fontName="DV", fontSize=10.5, leading=15),
}

def P(t, s="body"): return Paragraph(t, st[s])
def B(items): return [Paragraph(i, st["bullet"], bulletText="•") for i in items]

def table(rows, widths, header=True, zebra=True, bold_first_col=False):
    data = []
    for r_i, r in enumerate(rows):
        row = []
        for c_i, c in enumerate(r):
            if r_i == 0 and header: s = "cellh"
            elif bold_first_col and c_i == 0: s = "cellb"
            else: s = "cell"
            row.append(Paragraph(str(c), st[s]))
        data.append(row)
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0)
    ts = [("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("GRID", (0, 0), (-1, -1), 0.4, LINE),
          ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
          ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]
    if header: ts.append(("BACKGROUND", (0, 0), (-1, 0), NAVY))
    if zebra:
        for i in range(1 if header else 0, len(rows)):
            if i % 2 == 0: ts.append(("BACKGROUND", (0, i), (-1, i), LIGHT2))
    t.setStyle(TableStyle(ts))
    return t

def callout(text, bg=LIGHT, border=TEAL):
    t = Table([[Paragraph(text, st["callout"])]], colWidths=[W - 2 * M])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("LINEBEFORE", (0, 0), (0, -1), 3, border),
                           ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                           ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    return t

# ---------- diagramas ----------
def box(d, x, y, w, h, title, sub="", fill=LIGHT, stroke=NAVY, tcolor=NAVY, fs=8.5, fs2=7):
    d.add(Rect(x, y, w, h, rx=6, ry=6, fillColor=fill, strokeColor=stroke, strokeWidth=1))
    if sub:
        d.add(String(x + w / 2, y + h / 2 + 3, title, fontName="DVB", fontSize=fs, fillColor=tcolor, textAnchor="middle"))
        d.add(String(x + w / 2, y + h / 2 - 9, sub, fontName="DV", fontSize=fs2, fillColor=GREY, textAnchor="middle"))
    else:
        d.add(String(x + w / 2, y + h / 2 - 3, title, fontName="DVB", fontSize=8.5, fillColor=tcolor, textAnchor="middle"))

def arrow(d, x1, y1, x2, y2, c=GREY):
    d.add(Line(x1, y1, x2, y2, strokeColor=c, strokeWidth=1.1))
    import math
    a = math.atan2(y2 - y1, x2 - x1); L = 6
    p1 = (x2 - L * math.cos(a - 0.4), y2 - L * math.sin(a - 0.4))
    p2 = (x2 - L * math.cos(a + 0.4), y2 - L * math.sin(a + 0.4))
    d.add(Polygon([x2, y2, p1[0], p1[1], p2[0], p2[1]], fillColor=c, strokeColor=c))

def diagrama_arquitetura():
    w = W - 2 * M; d = Drawing(w, 300)
    # entradas
    box(d, 0, 250, w * 0.48, 40, "Base de conhecimento", "manual + regras + parâmetros", fill=LIGHT2)
    box(d, w * 0.52, 250, w * 0.48, 40, "Dados do simulador", "relatórios PDF + estado atual", fill=LIGHT2)
    # agentes
    names = [("Inteligência", "Competitiva"), ("Mercado &", "Marketing"), ("Tecnologia &", "Qualidade"),
             ("Operações &", "Logística"), ("Finanças", "(caixa/crédito)")]
    bw = (w - 4 * 8) / 5
    for i, (a, b) in enumerate(names):
        x = i * (bw + 8)
        box(d, x, 160, bw, 46, a, b, fill=colors.HexColor("#E3F1F3"), stroke=TEAL, tcolor=TEAL)
        arrow(d, x + bw / 2, 248, x + bw / 2, 208)
        arrow(d, x + bw / 2, 158, w / 2, 118)
    box(d, w * 0.25, 76, w * 0.5, 40, "Agente Integrador (CEO)", "consolida, resolve conflitos, checklist")
    arrow(d, w / 2, 74, w / 2, 56)
    box(d, w * 0.2, 14, w * 0.6, 40, "Pacote de recomendações (arquivos)", "a equipe humana discute, decide e salva no simulador",
        fill=AMBERBG, stroke=AMBER, tcolor=AMBER)
    return d

def diagrama_ciclo():
    w = W - 2 * M; d = Drawing(w, 120)
    steps = [("1. Pós-rodada", "lê resultados"), ("2. Nova rodada", "IA recomenda"),
             ("3. Reunião", "equipe discute"), ("4. Registrar", "decisão tomada"),
             ("5. Simulador", "equipe salva"), ("6. Professor", "processa")]
    bw = (w - 5 * 10) / 6
    for i, (a, b) in enumerate(steps):
        x = i * (bw + 10)
        human = i in (2, 4, 5)
        box(d, x, 50, bw, 50, a, b, fill=AMBERBG if human else colors.HexColor("#E3F1F3"),
            stroke=AMBER if human else TEAL, tcolor=AMBER if human else TEAL, fs=7.5, fs2=6.3)
        if i < 5: arrow(d, x + bw, 75, x + bw + 9, 75)
    d.add(Line(w - bw / 2, 48, w - bw / 2, 22, strokeColor=GREY))
    d.add(Line(w - bw / 2, 22, bw / 2, 22, strokeColor=GREY))
    arrow(d, bw / 2, 22, bw / 2, 48)
    d.add(String(w / 2, 10, "volta ao passo 1 no trimestre seguinte", fontName="DVI", fontSize=7.5, fillColor=GREY, textAnchor="middle"))
    d.add(Rect(0, 108, 9, 9, fillColor=colors.HexColor("#E3F1F3"), strokeColor=TEAL))
    d.add(String(13, 109, "IA (agentes)", fontName="DV", fontSize=7.5, fillColor=GREY))
    d.add(Rect(80, 108, 9, 9, fillColor=AMBERBG, strokeColor=AMBER))
    d.add(String(93, 109, "Equipe / professor", fontName="DV", fontSize=7.5, fillColor=GREY))
    return d

# ---------- página ----------
def on_page(c, doc):
    c.saveState()
    c.setStrokeColor(LINE); c.line(M, H - 1.3 * cm, W - M, H - 1.3 * cm)
    c.setFont("DV", 8); c.setFillColor(GREY)
    c.drawString(M, H - 1.1 * cm, "Business Game TecTrain · Projeto Agêntico · Equipe 3")
    c.drawRightString(W - M, 1.1 * cm, f"Página {doc.page}")
    c.drawString(M, 1.1 * cm, "IBMEC · Turma IBMEC-OL-Turma2NOV26 · 22/11/2026")
    c.restoreState()

def on_cover(c, doc):
    c.saveState()
    c.setFillColor(NAVY); c.rect(0, H * 0.42, W, H * 0.58, fill=1, stroke=0)
    c.setFillColor(TEAL); c.rect(0, H * 0.42 - 6, W, 6, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("DV", 12); c.drawString(M, H - 4 * cm, "MBA IBMEC · Business Game TecTrain")
    c.setFont("DVB", 30); c.drawString(M, H - 6.2 * cm, "Projeto Agêntico de")
    c.drawString(M, H - 7.6 * cm, "Apoio à Decisão")
    c.setFont("DV", 14)
    c.drawString(M, H - 9.3 * cm, "O que foi feito, os agentes criados, as recomendações")
    c.drawString(M, H - 10.0 * cm, "para o Trimestre 2 e como o projeto vai funcionar")
    c.setFillColor(NAVY); c.setFont("DVB", 12)
    c.drawString(M, H * 0.42 - 2.2 * cm, "Equipe 3 · Turma IBMEC-OL-Turma2NOV26")
    c.setFont("DV", 11); c.setFillColor(GREY)
    c.drawString(M, H * 0.42 - 3.0 * cm, "Empresa simulada: Startup de Tecnologia (produto Wise)")
    c.drawString(M, H * 0.42 - 3.7 * cm, "Versão 1 · 22/11/2026")
    c.setFont("DVI", 9)
    c.drawString(M, 2.2 * cm, "Documento de apoio à discussão da equipe. Os agentes recomendam; a decisão final é sempre do grupo.")
    c.restoreState()

doc = BaseDocTemplate("Projeto_Agentico_Business_Game_Equipe3.pdf", pagesize=A4,
                      leftMargin=M, rightMargin=M, topMargin=1.9 * cm, bottomMargin=1.8 * cm,
                      title="Projeto Agêntico de Apoio à Decisão – Business Game TecTrain – Equipe 3",
                      author="Equipe 3 – IBMEC")
frame = Frame(M, 1.8 * cm, W - 2 * M, H - 3.7 * cm, id="f")
doc.addPageTemplates([PageTemplate(id="cover", frames=[frame], onPage=on_cover),
                      PageTemplate(id="normal", frames=[frame], onPage=on_page)])
CW = W - 2 * M
s = []
s += [NextPageTemplate("normal"), PageBreak()]

# ===== 1. Resumo =====
s += [P("1. Resumo em uma página", "h1")]
s += [P("Montamos um <b>sistema de agentes de IA</b> que lê as regras do business game TecTrain e os relatórios do simulador e "
        "gera, a cada trimestre, um <b>pacote de recomendações</b> para a equipe decidir. A IA nunca registra decisões no "
        "simulador: ela analisa, calcula e recomenda; <b>quem decide e salva somos nós</b>.")]
s += [P("O que já está pronto", "h2")]
s += B(["<b>Base de conhecimento</b> (11 documentos): o manual inteiro, incluindo as tabelas que estão em imagem, mais os dados do simulador e o estado atual da nossa empresa.",
        "<b>6 agentes</b> com papéis definidos: Mercado, Operações, Tecnologia, Finanças, Inteligência Competitiva e o Integrador (CEO).",
        "<b>Recomendação completa para o Trimestre 2</b>, campo a campo, no formato das telas do simulador.",
        "<b>Harness</b>, o “manual de operação” do projeto: comandos, templates, regras de onde salvar cada coisa e um modelo de simulação de caixa.",
        "Tudo salvo no <b>Projeto “Business Game” no Claude</b>, acessível a qualquer membro do grupo."])
s += [P("A principal conclusão para o T2", "h2")]
s += [callout("<b>O problema do T2 é caixa, não lucro.</b> No cenário base vendemos ~7.500 kits, faturamos ~R$ 404 mil e "
              "o resultado operacional fica perto de +R$ 16 mil. Mas começamos com apenas <b>R$ 32,5 mil em caixa</b> e, "
              "sem financiamento, terminaríamos com ~<b>R$ 50 mil negativos</b>, caindo no empréstimo de emergência (o mais caro). "
              "Recomendação: pedir ao professor um <b>empréstimo de longo prazo de R$ 100 mil</b> ou, se não for liberado, vender <b>100% à vista</b>.",
              bg=AMBERBG, border=AMBER)]
s += [P("O que precisamos fazer agora", "h2")]
s += B(["<b>Hoje:</b> enviar ao professor o pedido de limite de crédito e perguntar o critério de avaliação do jogo.",
        "<b>Reunião do grupo:</b> ler a recomendação (seção 5) e decidir os 4 pontos em aberto (seção 6).",
        "<b>Depois:</b> uma única pessoa preenche e salva no simulador, conferindo as telas Projeções e Conclua."])
s += [PageBreak()]

# ===== 2. O jogo =====
s += [P("2. O jogo em uma página", "h1")]
s += [P("Somos a diretoria contratada pela holding <b>I2</b> para lançar no Brasil o <b>Wise</b>, um computador do tamanho de um cartão de crédito "
        "vendido em kits a revendedores. Capital inicial de <b>R$ 500 mil</b>, sem novos aportes. Concorremos com outras <b>7 equipes</b>. Cada rodada é um trimestre.")]
s += [table([
    ["Dimensão", "Como funciona"],
    ["Mercado", "4 praças (São Paulo, Brasília, Curitiba, Belo Horizonte) e 2 segmentos: <b>Básico</b> (sensível a preço, prazo e propaganda) e <b>Premium</b> (valoriza tecnologia, qualidade e força de vendas)."],
    ["Áreas de decisão", "Vendas (vendedores, preço, versão) · Marketing (propaganda, prazo de recebimento, pesquisas) · Logística · Produção · Tecnologia e Processos (P&amp;D, qualidade, redução de custo) · Finanças (empréstimos, CDB, dividendos)."],
    ["Regra que mais pega", "<b>O que se produz em um trimestre só pode ser vendido no seguinte.</b> As pesquisas de mercado também chegam um trimestre depois."],
    ["Sem vendedor, sem venda", "Só vendemos em uma praça se houver escritório e pelo menos 1 vendedor lá."],
    ["Falta de produto", "Penaliza a demanda do trimestre seguinte e a marca."],
    ["Caixa negativo", "Gera automaticamente um empréstimo de emergência a 150% da taxa da conta garantida."],
], [3.6 * cm, CW - 3.6 * cm], bold_first_col=True)]
s += [P("Onde estamos", "h2")]
s += [P("O <b>Trimestre 1</b> (rodada zero) foi decidido pelos professores, igual para todas as equipes: fábrica em Belo Horizonte com capacidade de 10.000 kits, "
        "8.000 kits produzidos, nenhuma venda. Resultado: prejuízo de R$ 38.625 e caixa de R$ 32.500. "
        "<b>O Trimestre 2 é a primeira rodada decidida por nós.</b>")]
s += [table([
    ["Indicador (início do T2)", "Valor"],
    ["Caixa", "R$ 32.500"], ["Estoque para vender", "8.000 kits em BH (custo de R$ 19,50 cada)"],
    ["Dívida", "Nenhuma"], ["Vendedores e escritórios", "Nenhum, ainda não estamos em nenhuma praça"],
    ["Versão do produto", "0 (nenhum P&amp;D ainda)"],
    ["Demanda potencial do T2 (mercado)", "60.018 kits, ou ~7.500 por equipe"],
], [7 * cm, CW - 7 * cm], bold_first_col=True)]
s += [PageBreak()]

# ===== 3. O que foi feito =====
s += [P("3. O que foi feito", "h1")]
s += [table([
    ["Etapa", "O que foi feito", "Resultado"],
    ["1. Leitura das fontes", "Manual do Participante (42 páginas), incluindo as tabelas que estão em imagem. Exploração de todas as telas do simulador (somente leitura) e leitura dos 10 relatórios em PDF do T1. O site não tem vídeos.", "Todas as regras e números do jogo extraídos"],
    ["2. Base de conhecimento", "Organização em 11 documentos temáticos (contexto, marketing, operações, tecnologia, finanças, telas, parâmetros, estado atual, agentes, checklist).", "Fonte única de verdade para os agentes"],
    ["3. Descobertas", "Números que <b>não estão no manual</b>, deduzidos dos relatórios: custo de estoque ~5% por trimestre, imposto de 34%, custo da fábrica de BH de R$ 15/kit, P&amp;D acelerado por R$ 40 mil. Também mapeamos <b>contradições do manual</b>.", "Calibração do modelo e 7 perguntas ao professor"],
    ["4. Agentes", "Definição de 6 agentes com missão, entradas, decisões e prompts.", "Arquitetura do sistema"],
    ["5. Modelo de simulação", "Modelo em Python de caixa e resultado do trimestre, com cenários.", "Números consistentes, sem chute"],
    ["6. Rodada T2", "Execução dos agentes para o T2 e consolidação pelo CEO.", "6 arquivos de recomendação"],
    ["7. Harness", "Comandos, templates, protocolo de salvamento e registros (decisões, perguntas, lições, histórico).", "O projeto funciona igual em qualquer conversa"],
], [3.3 * cm, 9.2 * cm, CW - 12.5 * cm], bold_first_col=True)]
s += [Spacer(1, 8)]
s += [callout("<b>Princípio de rastreabilidade:</b> todo número nos documentos vem marcado com a origem: "
              "<b>[manual]</b> (regra oficial), <b>[observado]</b> (visto no simulador), <b>[análise]</b> (inferência nossa) ou "
              "<b>[premissa]</b> (suposição a validar). Assim o grupo sabe em que confiar.")]
s += [PageBreak()]

# ===== 4. Como funciona =====
s += [P("4. Como o projeto agêntico funciona", "h1")]
s += [P("Cada agente é um “diretor virtual” especialista em uma área. Todos leem a mesma base de conhecimento e os dados do trimestre; "
        "o <b>Integrador (CEO)</b> junta as recomendações, verifica a coerência entre elas (por exemplo, se o estoque cobre a demanda ou se o caixa fica positivo) "
        "e entrega um pacote único para a equipe.")]
s += [Spacer(1, 4), diagrama_arquitetura(), Spacer(1, 6)]
s += [P("O ciclo de cada trimestre", "h2")]
s += [diagrama_ciclo(), Spacer(1, 4)]
s += [P("Ordem de execução dos agentes", "h2")]
s += B(["Inteligência Competitiva e Mercado analisam concorrentes e demanda.",
        "Tecnologia define P&amp;D, qualidade e redução de custos.",
        "Operações usa a demanda estimada para dimensionar produção e logística.",
        "Finanças junta todos os gastos e receitas, projeta o caixa e propõe o financiamento.",
        "O CEO consolida, aplica o checklist e lista os pontos que a equipe precisa decidir."])
s += [PageBreak()]

# ===== 5. Agentes e outputs =====
s += [P("5. Os agentes e o que recomendaram para o T2", "h1")]
s += [table([
    ["Agente", "Missão", "Principal recomendação para o T2"],
    ["Mercado &amp; Marketing", "Maximizar a demanda rentável por praça e segmento", "Entrar nas <b>4 praças</b> (vendedores SP 3, BS 2, CR 2, BH 2); preços <b>R$ 50 / R$ 60</b>; propaganda de <b>R$ 30 mil</b>; Premium como prioridade em Curitiba (60% Premium); recebimento <b>80/20</b>; comprar as 2 pesquisas"],
    ["Operações &amp; Logística", "Disponibilidade com o menor custo total", "Produzir <b>9.000 kits</b> em BH (para o T3); não expandir; prioridade de transferência BH → SP → BS → CR; RoxConn = 0"],
    ["Tecnologia &amp; Qualidade", "Vantagem em versão e qualidade com retorno", "Contratar <b>6 pesquisadores</b> (versão 1 para o T3/T4); ligar a <b>inspeção de qualidade</b>; <b>R$ 10 mil</b> em redução de custo em BH (payback em menos de 2 trimestres)"],
    ["Finanças", "Viabilizar o plano sem empréstimo de emergência", "<b>Empréstimo de longo prazo de R$ 100 mil</b> (13% a.a., quitável antes); plano C: 100% à vista; cobrança de R$ 500"],
    ["Inteligência Competitiva", "Ler e antecipar os 7 concorrentes", "Todos partem iguais; oferta ≈ demanda, então não há guerra de preço; monitorar preço, vendedores e versão no relatório do T2"],
    ["Integrador (CEO)", "Consolidar e garantir a coerência", "Estratégia “<b>presença total com disciplina de caixa</b>”; pacote final por tela; 4 pontos de decisão para o grupo"],
], [3.3 * cm, 4.2 * cm, CW - 7.5 * cm], bold_first_col=True)]
s += [P("Pacote de decisões recomendado (por tela do simulador)", "h2")]
s += [table([
    ["Tela", "Campo", "SP", "BS", "CR", "BH"],
    ["Vendas", "Vendedores", "3", "2", "2", "2"],
    ["Vendas", "Preço Básico / Premium", "50 / 60", "50 / 60", "50 / 60", "50 / 60"],
    ["Vendas", "Versão B / P", "0 / 0", "0 / 0", "0 / 0", "0 / 0"],
    ["Marketing", "Propaganda (R$)", "10.000", "8.000", "6.000", "6.000"],
    ["Marketing", "Prioridade", "Básico", "Básico", "Premium", "Básico"],
    ["Produção", "Produzir no trimestre", "0", "0", "0", "9.000"],
    ["Tecnologia", "Melhoria de processo (R$)", "0", "0", "0", "10.000"],
], [2.4 * cm, 4.6 * cm] + [(CW - 7 * cm) / 4] * 4)]
s += [Spacer(1, 4)]
s += [P("<b>Demais campos:</b> recebimento 80% à vista e 20% em T+1 · pesquisas Indicadores SIM e Demanda SIM · matriz de logística salva (BH → SP, BS, CR) · "
        "RoxConn 0 · P&amp;D +6 pesquisadores, sem acelerar · inspeção de qualidade SIM · empréstimo de longo prazo de R$ 100 mil · cobrança de R$ 500.", "small")]
s += [PageBreak()]

# ===== 6. Financeiro e decisões =====
s += [P("6. Números do T2 e pontos para o grupo decidir", "h1")]
s += [P("Projeção de caixa por cenário", "h2")]
s += [table([
    ["Cenário", "Kits vendidos", "Receita", "Resultado operacional", "Caixa final sem empréstimo", "Caixa final com LP R$ 100 mil"],
    ["Pessimista", "6.000", "R$ 324 mil", "−R$ 29 mil", "−R$ 109 mil", "−R$ 9 mil"],
    ["<b>Base</b>", "<b>7.500</b>", "<b>R$ 404 mil</b>", "<b>+R$ 16 mil</b>", "<b>−R$ 50 mil</b>", "<b>+R$ 50 mil</b>"],
    ["Otimista", "8.000", "R$ 431 mil", "+R$ 31 mil", "−R$ 31 mil", "+R$ 69 mil"],
    ["Plano C (100% à vista, só 1 pesquisa)", "7.500", "R$ 404 mil", "+R$ 31 mil", "+R$ 46 mil", "não precisa"],
], [4.4 * cm, 2.0 * cm, 2.3 * cm, 2.7 * cm, 2.8 * cm, CW - 14.2 * cm])]
s += [Spacer(1, 4)]
s += [P("Por que o resultado do T2 fica perto do zero: há ~R$ 98 mil de gastos que só ocorrem uma vez (abrir 4 escritórios, contratar vendedores, pesquisas). "
        "Do T3 em diante a estrutura fixa fica mais leve.", "small")]
s += [P("Os 4 pontos que o grupo precisa decidir", "h2")]
s += [table([
    ["#", "Decisão", "Opção A (recomendada)", "Opção B"],
    ["1", "Prazo de recebimento", "80% à vista e 20% em T+1, com empréstimo de R$ 100 mil (mais atrativo para o Básico)", "100% à vista, sem dívida (mais seguro, menos atrativo)"],
    ["2", "Preço do Premium com versão 0", "R$ 60 (referência do manual; todos os concorrentes estão na v0)", "R$ 58 até termos a versão 1"],
    ["3", "Velocidade do P&amp;D", "6 pesquisadores: R$ 18 mil, versão 1 no T3/T4", "Acelerar por R$ 40 mil: versão 1 já no T2, Premium a R$ 62–65, exige mais crédito"],
    ["4", "Pesquisa de demanda (R$ 15 mil)", "Comprar (orienta a produção do T3)", "Cortar se o caixa apertar"],
], [0.8 * cm, 3.6 * cm, 6.4 * cm, CW - 10.8 * cm])]
s += [P("Plano de contingência", "h2")]
s += B(["<b>Professor não liberou crédito a tempo:</b> 100% à vista e só a pesquisa de Indicadores.",
        "<b>A tela Projeções mostra empréstimo de emergência:</b> cortar nesta ordem: pesquisa de Demanda → pesquisadores → produção → prazo de recebimento.",
        "<b>Queremos menos risco:</b> 2 vendedores em SP, produzir 8.000 e 4 pesquisadores."])
s += [PageBreak()]

# ===== 7. Harness =====
s += [P("7. O harness: como usar o projeto no dia a dia", "h1")]
s += [P("O <b>harness</b> é o “manual de operação” do projeto. Ele garante que qualquer membro do grupo, em qualquer conversa no Projeto “Business Game” do Claude, "
        "obtenha o mesmo comportamento: a IA lê a base antes de responder, segue os mesmos formatos e <b>salva tudo o que for importante</b> nos documentos do Projeto, sem depender do histórico do chat.")]
s += [P("Estrutura do Projeto", "h2")]
s += [table([
    ["Pasta", "Conteúdo"],
    ["<b>harness/</b>", "Regras de uso, comandos, templates, protocolo de salvamento, modelo de simulação e o texto das instruções do Projeto"],
    ["<b>base-conhecimento/</b>", "Regras do jogo, parâmetros, telas do simulador, estado atual da equipe, arquitetura dos agentes e checklist"],
    ["<b>rodadas/T2, T3…</b>", "Recomendações dos agentes, decisão tomada, ata da reunião e análise pós-rodada de cada trimestre"],
    ["<b>registro/</b>", "Log de decisões, perguntas ao professor, lições aprendidas sobre o simulador e histórico de mudanças"],
], [4 * cm, CW - 4 * cm])]
s += [P("Comandos para digitar no chat do Projeto", "h2")]
s += [table([
    ["Comando", "O que faz"],
    ["/status", "Mostra a situação atual: caixa, estoque, pendências e próximo passo"],
    ["/nova-rodada T3", "Roda todos os agentes e gera as recomendações do trimestre"],
    ["/agente financas T3", "Roda só um agente (mercado, operacoes, tecnologia, financas, competitiva, ceo)"],
    ["/simular T2 100% à vista", "Testa cenários de caixa e resultado com o modelo"],
    ["/registrar-decisao T2", "Registra o que o grupo decidiu de fato e as diferenças em relação à recomendação"],
    ["/pos-rodada T2", "Analisa os relatórios processados, compara previsto × realizado e atualiza o estado"],
    ["/pergunta-instrutor", "Registra uma dúvida para o professor ou a resposta recebida"],
    ["/regra &lt;tema&gt;", "Explica uma regra do jogo citando a fonte"],
    ["/ata", "Registra o resumo de uma reunião do grupo"],
], [4.6 * cm, CW - 4.6 * cm])]
s += [Spacer(1, 6)]
s += [callout("<b>Regras de ouro:</b> (1) os agentes recomendam e o grupo decide; (2) a IA nunca salva nada no simulador; "
              "(3) números vêm de cálculo, não de estimativa; (4) tudo que for durável é salvo no Projeto; "
              "(5) <b>uma única pessoa salva a decisão final no simulador</b>, porque vale a última versão salva por qualquer membro.")]
s += [PageBreak()]

# ===== 8. Pendências =====
s += [P("8. Pendências, limitações e próximos passos", "h1")]
s += [P("Perguntas abertas ao professor", "h2")]
s += [table([
    ["#", "Pergunta", "Por que importa"],
    ["1", "Liberar limite de empréstimo de longo prazo (R$ 100 mil) e de conta garantida (R$ 50 mil)?", "Sem crédito, o T2 fica com caixa negativo se o recebimento for 80/20"],
    ["2", "Qual é o critério de avaliação ou ranking final?", "Define o que os agentes devem otimizar"],
    ["3", "Quantos trimestres terá o jogo?", "Horizonte dos investimentos"],
    ["4", "Custo da antecipação de recebíveis (o manual traz dois valores)", "Contradição no manual"],
    ["5", "Regra de custo para expandir uma fábrica", "Expandir BH × abrir uma 2ª fábrica"],
    ["6", "Custo de produção por cidade (tela × manual)", "Escolha do local de uma nova fábrica"],
    ["7", "Quantos pesquisadores ou trimestres até a versão 1?", "Planejamento do Premium"],
], [0.8 * cm, 8.6 * cm, CW - 9.4 * cm])]
s += [P("Limitações que o grupo deve conhecer", "h2")]
s += B(["O manual <b>não informa as fórmulas de demanda</b> (quanto cada vendedor, real de propaganda ou desconto de preço gera de vendas). "
        "Por isso os cenários fixam a quantidade vendida. Essas relações serão <b>calibradas a partir do resultado do T2</b>.",
        "Os números são projeções. <b>Antes de salvar, sempre confira a tela Projeções do simulador</b>, que usa o cálculo oficial.",
        "Supomos que todos os concorrentes têm os mesmos 8.000 kits (o T1 foi igual para todos)."])
s += [P("Próximos passos", "h2")]
s += [table([
    ["Quando", "O quê", "Quem"],
    ["Hoje", "Enviar as perguntas 1 e 2 ao professor (menu Suporte do simulador)", "Equipe"],
    ["Hoje (5 min)", "Colar o texto de <i>harness/INSTRUCOES_DO_PROJETO.md</i> nas instruções do Projeto no Claude", "Dona do Projeto"],
    ["Reunião", "Decidir os 4 pontos da seção 6 e rodar <i>/registrar-decisao T2</i>", "Grupo"],
    ["Antes do prazo", "Preencher o simulador, conferir Projeções e Conclua, e salvar (uma pessoa só)", "Responsável designado"],
    ["Após o processamento", "Rodar <i>/pos-rodada T2</i> e depois <i>/nova-rodada T3</i>", "Qualquer membro"],
], [3.2 * cm, CW - 7.6 * cm, 4.4 * cm])]

doc.build(s)
print("ok")
