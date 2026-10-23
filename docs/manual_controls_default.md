# GoldenEye — controles manuais: perfil `default`

Registro de correspondências confirmado pelo operador na sessão do Manual Controls Recognition v2, em BizHawk 2.11.1 / NLua. **`default` é o nome do perfil registrado**, não a identificação verificada do layout configurado no menu do GoldenEye.

| Entrada N64 | Ação identificada pelo operador | Condição |
|---|---|---|
| Z | Atirar (`fire_manual`) | Conforme arma equipada |
| R | Ativar mira visual (`visual_aim`) | Enquanto acionado |
| A | Alternar armas/desarmado (`cycle_weapon`) | Arsenal disponível |
| B | Recarregar (`reload`) | Arma recarregável e munição extra |

Fonte canônica estruturada: [catalog/manual_controls.json](../catalog/manual_controls.json).

## Procedência
- Repositório de captura: [GoldenEye.assistant](https://github.com/marcosvilhena87/GoldenEye.assistant).
- Sessão: `20261023T020648Z`; frames de início 41098 até último evento 47121.
- Arquivos produzidos e apresentados pelo operador: `manual_controls_v2_events.csv`, `manual_controls_v2_annotations.csv`, `manual_controls_v2_diagnostics.csv`, `manual_controls_v2_commands.txt`.
- A sessão registrou pressões: Z (2), R (1), A (2), B (1), com solturas correspondentes.
- Declaração posterior do operador: Z atira; R ativa mira visual; A alterna armas/desarmado; B recarrega se houver munição extra.

## Limitações
- Pressão física medida e efeito visual confirmado por pessoa são evidências diferentes: nenhuma validação automatizada de animação, munição ou modo de mira foi realizada.
- Os rótulos `ACTION:aim_manual` aplicados aos experimentos de R, A e B no CSV são hipóteses da fase de captura. **Não** concluir que A ou B acionam a mira.
- ROM não identificada por SHA-256; a configuração exata de layout de controles no menu do jogo não foi fotografada ou exportada.
- Portanto, status `operator_confirmed`, não `validated`; não inscrever estes mapeamentos como endereços/offsets na RAM.

## Regras de consumo
O `GoldenEye.assistant` pode apresentar este perfil como referência de comandos, mas não deve inferir validação de memória, comportamento universal ou habilitar disparo automático a partir dele. Mudança de esquema de controle requer novo perfil e validação.
