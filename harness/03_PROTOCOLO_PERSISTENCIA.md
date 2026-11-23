# 03 — Protocolo de persistência (o que salvar, onde e quando)

## Princípio
**Se uma informação pode ser útil numa conversa futura, ela precisa estar num documento do Projeto.** O histórico de chat não é base de conhecimento.

## Onde cada coisa vai
| Tipo de informação | Destino | Como |
|---|---|---|
| Regra do jogo (manual) ou correção de regra | `base-conhecimento/01–07` | Editar o doc inteiro e registrar no changelog |
| Parâmetro descoberto no simulador ([observado]) | `base-conhecimento/07_parametros_e_formulas.md` e o doc da área | Editar e registrar no changelog |
| Situação atual da empresa | `base-conhecimento/08_estado_atual_equipe3.md` | **Reescrever** a cada pós-rodada; o histórico só cresce |
| Recomendações dos agentes | `rodadas/Tn/Tn_00–05_*.md` | Um arquivo por agente |
| Decisão efetivamente tomada | `rodadas/Tn/Tn_90_DECISAO_TOMADA.md` e `registro/decisoes_log.md` | Template T3/T5 |
| Ata de reunião | `rodadas/Tn/Tn_80_ATA_REUNIAO.md` | Livre |
| Resultado e análise pós-processamento | `rodadas/Tn/Tn_99_POS_RODADA.md` | Template T4 |
| Como o simulador reage (aprendizado) | `registro/licoes_aprendidas.md` | Template T6 |
| Dúvidas e respostas do professor | `registro/perguntas_instrutor.md` | Template T7 |
| Toda mudança na base | `registro/changelog_kb.md` | Template T8 |
| Material para o grupo (PDF, PPTX) | `entregaveis/` **somente no GitHub** | Arquivo + script gerador; status no `harness/00` |
| Textos de vitrine (arquitetura, método) | `docs/` | Projeto e GitHub |
| README de portfólio | `claude/README.md` no Projeto = `README.md` no GitHub | Manter os dois iguais |

## Convenções de nome
- Rodadas: `rodadas/T{n}/T{n}_{NN}_{descricao}.md`. Faixas de NN: 00 = CEO; 01–05 = agentes; 80 = ata; 90 = decisão tomada; 99 = pós-rodada.
- Sem acentos nem espaços nos nomes de arquivo; o conteúdo pode ter acentos.
- Datas no formato DD/MM/AAAA dentro dos documentos.

## Regras de escrita
1. **Ler o documento atual antes de alterá-lo** e salvar a versão completa (não existe edição parcial).
2. **Não apagar o histórico:** o `decisoes_log`, as `licoes` e o `changelog` só recebem acréscimos. O `08_estado` mantém a tabela de histórico.
3. **Uma alteração de regra se propaga:** se um valor do doc 07 muda, atualizar também o doc da área (03, 04 ou 05) e o `08_estado` se for o caso.
4. **Marcar a origem** de todo número: [manual], [observado], [análise] ou [premissa].
5. **Fechar a conversa salvando:** ao final de qualquer interação que gerou decisão, número novo ou aprendizado, a IA lista o que salvou ("Salvei: …").

## Versionamento no GitHub (obrigatório)
Repositório: **https://github.com/katiafrancoso/mba-business-game** (público; empresa e dados fictícios).
- **Sempre que o projeto evoluir**, publicar uma nova versão no GitHub. Evoluir significa: novos documentos ou documentos alterados no Projeto, uma rodada nova, uma decisão registrada, um pós-rodada, ajustes no harness ou no modelo, ou um novo entregável.
- O GitHub é **espelho do Projeto**, com a mesma estrutura de pastas: `base-conhecimento/`, `harness/`, `rodadas/`, `registro/`, `docs/` e `entregaveis/`.
- **Mensagem de commit** em português, no formato `tipo(escopo): descrição`. Exemplos: `feat(rodadas): recomendações do T3`, `docs(registro): decisão tomada no T2`, `fix(base): corrige custo de expansão`.
- **Marcos com tag:** ao fechar cada trimestre, depois do pós-rodada, criar a tag `T{n}-fechado` (por exemplo, `T2-fechado`).
- Atualizar o `README.md` quando mudar a estrutura, a lista de agentes ou o status do jogo.
- Não versionar o manual original do participante (documento da TecTrain) nem segredos ou credenciais.
- Se não houver acesso ao GitHub na sessão, avisar o usuário e registrar no `changelog_kb.md` que a publicação ficou pendente.

## Checklist de fim de conversa (para a IA)
- [ ] Gerou recomendação? → `rodadas/Tn/`
- [ ] A equipe decidiu algo? → `_90_DECISAO_TOMADA` + `decisoes_log`
- [ ] Apareceu um número ou uma regra nova? → base + changelog
- [ ] Surgiu uma dúvida para o professor? → `perguntas_instrutor`
- [ ] Aprendemos algo sobre o simulador? → `licoes_aprendidas`
- [ ] O Status no `harness/00` está atualizado?
- [ ] **Nova versão publicada no GitHub** (commit + push; tag se o trimestre fechou)?
