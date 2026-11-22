"""
Modelo de caixa e DRE de um trimestre - Equipe 3 (TecTrain Business Management)
=============================================================================
Uso (Python 3, sem dependencias):
    python3 04_modelo_simulacao.py               -> roda os cenarios padrao
    from 04_modelo_simulacao import trimestre     -> (renomeie para modelo.py para importar)

ATUALIZE o bloco PARAMETROS_ATUAIS a cada trimestre (fonte: 08_estado_atual_equipe3.md).
Limitacao: as vendas NAO reagem a preco/vendedores/propaganda; o cenario fixa a demanda.
Calibre com as licoes em registro/licoes_aprendidas.md. Confira SEMPRE na tela PROJECOES.
"""

# ---------------- PARAMETROS ATUAIS (T2) ----------------
PARAMETROS_ATUAIS = dict(
    caixa0=32500,            # caixa inicial do trimestre
    estoque={"BH": 8000},    # kits disponiveis por praca
    custo_est=19.5,          # custo unitario do estoque
    receber_entrando=0,      # recebiveis de trimestres anteriores que vencem agora
    escritorios_abertos=[],  # pracas que ja tem escritorio
    vendedores_atuais={"SP": 0, "BS": 0, "CR": 0, "BH": 0},
    pesquisadores_atuais=0,
    fabricas={"BH": dict(cap=10000, fixo=45000, cuf=15.0)},
)
# demanda potencial MEDIA por equipe (mercado / 8) -> (basico, premium)
DEMANDA_MEDIA = {"SP": (1791, 768), "BS": (1241, 668), "CR": (555, 832), "BH": (989, 659)}

# ---------------- CONSTANTES DO MANUAL ----------------
C = dict(abrir_escr=10000, aluguel_escr=2000, contratar_vend=4000, salario_vend=3000,
         contratar_pesq=1000, salario_pesq=2000, frete=3.0, roxconn=30.0,
         manut_estoque=0.05,  # [observado]
         defeito_base=0.10, reducao_inspecao=0.40, custo_inspecao=0.40, retrabalho=0.01,
         melhoria_reducao=0.05, depreciacao_trim=4625, acelerar_pd=40000, ir=0.34)


def trimestre(fator_demanda=1.0, preco_b=50, preco_p=60,
              vendedores={"SP": 3, "BS": 2, "CR": 2, "BH": 2},
              propaganda={"SP": 10000, "BS": 8000, "CR": 6000, "BH": 6000},
              pct_vista=0.8, pesquisas=25000, contratar_pesq=6, acelerar=False,
              inspecao=True, estudo=False, acoes_melhoria=0, melhoria_processo={"BH": 10000},
              producao={"BH": 9000}, roxconn=0, emprestimo=0, cobranca=0, p=PARAMETROS_ATUAIS):
    estoque_tot = sum(p["estoque"].values()) + roxconn
    dem = {c: (b * fator_demanda, pp * fator_demanda) for c, (b, pp) in DEMANDA_MEDIA.items()
           if vendedores.get(c, 0) > 0}
    dem_tot = sum(b + pp for b, pp in dem.values())
    esc = min(1, estoque_tot / dem_tot) if dem_tot else 0
    vend = {c: (b * esc, pp * esc) for c, (b, pp) in dem.items()}
    un = sum(b + pp for b, pp in vend.values())
    receita = sum(b * preco_b + pp * preco_p for b, pp in vend.values())
    est_proprio = sum(p["estoque"].values())
    cmv = min(un, est_proprio) * p["custo_est"] + max(0, un - est_proprio) * C["roxconn"]
    # frete: vendas em pracas sem estoque proprio (aproximacao)
    frete = C["frete"] * sum(b + pp for c, (b, pp) in vend.items() if c not in p["estoque"])
    taxa_def = C["defeito_base"] * (1 - C["reducao_inspecao"]) if inspecao else C["defeito_base"]
    garantia = cmv * taxa_def
    insp = C["custo_inspecao"] * garantia if inspecao else 0
    retrab = C["retrabalho"] * cmv if inspecao else 0
    qualidade = garantia + insp + retrab + (5000 if estudo else 0) + acoes_melhoria
    # comercial
    novas_pracas = [c for c, n in vendedores.items() if n > 0 and c not in p["escritorios_abertos"]]
    escr = len(novas_pracas) * C["abrir_escr"] + sum(1 for n in vendedores.values() if n > 0) * C["aluguel_escr"]
    delta_v = sum(abs(vendedores.get(c, 0) - p["vendedores_atuais"].get(c, 0)) for c in vendedores)
    vendas_pessoal = delta_v * C["contratar_vend"] + sum(vendedores.values()) * C["salario_vend"]
    prop = sum(propaganda.values())
    pd = abs(contratar_pesq) * C["contratar_pesq"] + (p["pesquisadores_atuais"] + contratar_pesq) * C["salario_pesq"] \
        + (C["acelerar_pd"] if acelerar else 0)
    melhoria = sum(melhoria_processo.values())
    manut = C["manut_estoque"] * est_proprio * p["custo_est"]
    # producao (para o proximo trimestre)
    prod_caixa, ocios, unit_prox = 0, 0, {}
    for c, f in p["fabricas"].items():
        q = producao.get(c, 0)
        cuf = f["cuf"] * (1 - C["melhoria_reducao"]) if melhoria_processo.get(c, 0) >= 10000 else f["cuf"]
        aloc = f["fixo"] * q / f["cap"]
        ocios += f["fixo"] - aloc
        prod_caixa += q * cuf + aloc
        unit_prox[c] = round((q * cuf + aloc) / q, 2) if q else None
    desp = qualidade + escr + vendas_pessoal + prop + pesquisas + pd + melhoria + frete + manut + ocios \
        + C["depreciacao_trim"] + cobranca
    lajir = receita - cmv - desp
    entradas = receita * pct_vista + p["receber_entrando"] + emprestimo
    saidas = prod_caixa + ocios + qualidade + escr + vendas_pessoal + prop + pesquisas + pd + melhoria \
        + frete + manut + roxconn * C["roxconn"] + cobranca
    caixa = p["caixa0"] + entradas - saidas
    return dict(un_vendidas=round(un), receita=round(receita), cmv=round(cmv), lajir=round(lajir),
                caixa_final=round(caixa), emergencia=round(max(0, -caixa)),
                a_receber=round(receita * (1 - pct_vista)), estoque_final=round(estoque_tot - un),
                custo_unit_prox_trim=unit_prox,
                despesas=dict(qualidade=round(qualidade), escritorios=escr, vendedores=vendas_pessoal,
                              propaganda=prop, pesquisas=pesquisas, p_d=pd, melhoria=melhoria,
                              frete=round(frete), manut_estoque=round(manut), ociosidade=round(ocios),
                              depreciacao=C["depreciacao_trim"]),
                producao_caixa=round(prod_caixa))


if __name__ == "__main__":
    cenarios = {
        "Base (recomendado, sem emprestimo)": {},
        "Base + LP 100k": dict(emprestimo=100000),
        "Pessimista 0.8 + LP 100k": dict(fator_demanda=0.8, emprestimo=100000),
        "Otimista 1.15 + LP 100k": dict(fator_demanda=1.15, emprestimo=100000),
        "Plano C: 100% a vista, so Indicadores": dict(pct_vista=1.0, pesquisas=10000),
        "Agressivo: acelerar P&D, P=62, LP 140k": dict(acelerar=True, contratar_pesq=0, preco_p=62, emprestimo=140000),
    }
    print(f"{'cenario':42s} {'un':>6} {'receita':>9} {'LAJIR':>8} {'caixa':>9} {'estFinal':>8}")
    for n, kw in cenarios.items():
        r = trimestre(**kw)
        print(f"{n:42s} {r['un_vendidas']:6d} {r['receita']:9d} {r['lajir']:8d} {r['caixa_final']:9d} {r['estoque_final']:8d}")
