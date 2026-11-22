# 02 — Templates obrigatórios

Use os templates abaixo para que todas as rodadas fiquem comparáveis. `{...}` indica um campo a preencher.

---
## T1. Relatório de agente — `rodadas/Tn/Tn_0X_agente_{area}.md`
```markdown
# Tn — Agente {Área}: recomendação
> Base: {docs e relatórios usados}. Gerado em {data}. Status: recomendação para discussão.

## 1. Situação
{3–6 bullets com dados [observado]}

## 2. Recomendação (campos da tela {TELA})
| Campo | SP | BS | CR | BH |
|---|---|---|---|---|
| {campo} | {valor} | ... |

**Racional:** {por quê, citando a regra do doc X}
**Impacto:** caixa {R$} | lucro {R$}
**Alternativas:** {opção → efeito}

## 3. Riscos e o que monitorar no próximo trimestre
```

## T2. Recomendação final do CEO — `rodadas/Tn/Tn_00_RECOMENDACAO_FINAL_CEO.md`
```markdown
# Tn — Recomendação final do Agente Integrador (CEO)
## Estratégia do trimestre (1 frase + 3–4 pilares)
## Pacote de decisões por tela (VENDAS, MARKETING, LOGÍSTICA, PRODUÇÃO, TECNOLOGIA, FINANÇAS)
## Orçamento (saídas e entradas) e resultado esperado (base / pessimista / otimista)
## Plano de contingência (se… então…)
## Checklist antes de salvar
## Pontos de decisão da equipe (trade-offs reais)
```

## T3. Decisão tomada — `rodadas/Tn/Tn_90_DECISAO_TOMADA.md`
```markdown
# Tn — Decisão tomada pela equipe
> Registrado em {data} por {nome}. Salvo no simulador em {data/hora} por {nome}.

| Tela | Campo | Recomendado | Decidido | Motivo da divergência |
|---|---|---|---|---|
| VENDAS | Vendedores SP | 3 | {x} | {—} |
...
## Resultado esperado registrado (para comparar no pós-rodada)
Vendas {un.} | Receita {R$} | Lucro {R$} | Caixa final {R$}
```

## T4. Pós-rodada — `rodadas/Tn/Tn_99_POS_RODADA.md`
```markdown
# Tn — Pós-rodada (resultado processado)
## 1. Resultado real
| Indicador | Previsto | Realizado | Desvio | Explicação |
|---|---|---|---|---|
| Kits vendidos | | | | |
| Receita | | | | |
| Lucro líquido | | | | |
| Caixa final | | | | |
| Falta de produto | | | | |
## 2. Concorrência (8 equipes)
| Equipe | Preço B médio | Preço P médio | Vendedores | Versão | Share entregas | ROE | Endividamento |
## 3. Lições sobre o simulador (→ registro/licoes_aprendidas.md)
## 4. Implicações para T(n+1)
```

## T5. Entrada no log de decisões — `registro/decisoes_log.md`
```markdown
## Tn — {data}
- Estratégia: {frase}
- Decisões-chave: {5–8 bullets}
- Divergências em relação à recomendação: {bullets}
- Resultado: {preencher no pós-rodada}
```

## T6. Lição aprendida — `registro/licoes_aprendidas.md`
```markdown
| # | Trimestre | Lição | Evidência (relatório/valor) | Confiança (alta/média/baixa) | Doc da base atualizado |
```

## T7. Pergunta ao instrutor — `registro/perguntas_instrutor.md`
```markdown
| # | Aberta em | Pergunta | Por que importa | Status | Resposta | Data |
```

## T8. Changelog — `registro/changelog_kb.md`
```markdown
| Data | Arquivo | Alteração | Fonte/motivo | Autor (IA/nome) |
```
