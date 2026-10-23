# Auto-Aim Discovery v0.1

Objetivo: distinguir entrada manual, assistência de mira, aquisição de alvo e condição de disparo.

## Contrastes
1. Cena sem inimigos, mira ligada/desligada.
2. Inimigo visível estacionário, mira ligada/desligada.
3. Inimigo atravessa lateralmente o campo de visão.
4. Alvo atrás de obstáculo e fora do alcance aparente.
5. Troca de armas e munição zero.
6. Disparo manual / ausência de disparo.

Anotar ROM/hash, emulador/core, frames, inputs e dumps com timestamps/frame IDs. Propor candidatos somente após verificar controles negativos. Não presumir que um campo de RAM represente diretamente o alvo assistido.


## Auto-Aim Mapping v1 — observação CSV (2026-10-22)

Implementação experimental: [GoldenEye.assistant/autoaim_mapping_v1.lua](https://github.com/marcosvilhena87/GoldenEye.assistant/blob/main/autoaim_mapping_v1.lua).

### Descompilação como fonte de hipóteses
- `chrpropUpdateAutoaimTarget` seleciona candidatos em `g_OnScreenPropList`, mantém `best_prop` e atualiza `bondviewUpdateXAutoAimTime`/`bondviewUpdateYAutoAimTime` (`src/game/chrprop.c`).
- `chrGetOnscreenRenderBounds` filtra alvo fora da tela, morto/morrendo ou marcado `CHRFLAG_NO_AUTOAIM` (`src/game/chr.c`).
- `g_CurrentPlayer->autoaim_target_x/y` e `autoaimx/y` são campos do jogador no código, ainda **sem offsets/endereço de RAM confirmados no BizHawk**.
- Referências de função como `0x7F03D78C` são endereços de código US, **não** endereços canônicos de dados.

### Preparação
1. Abrir o checkout do GoldenEye.assistant e definir o diretório de trabalho da Lua Console como raiz do repositório.
2. Abrir `autoaim_mapping_v1.lua` no BizHawk. Não usar `lua` no PowerShell: o script roda dentro do EmuHawk.
3. Os relatórios são criados onde o diretório de trabalho da Lua Console apontar: `autoaim_v1_samples.csv`, `autoaim_v1_events.csv`, `autoaim_v1_diagnostics.csv`.
4. Em PowerShell, com a captura rodando, usar `Add-Content .\\autoaim_v1_commands.txt 'PHASE:no_enemy'`; repetir para `PHASE:one_guard_visible`, `PHASE:two_guards`, `PHASE:guard_behind_wall`, `PHASE:guard_offscreen`, `PHASE:autoaim_off`.
5. Registrar ocorrências com `Add-Content .\\autoaim_v1_commands.txt 'EVENT:guard_entered_view'`; anotações livres usam `NOTE:texto`.
6. Usar savestate e, se ativado, o cheat Bulletproof Bond, anotando a condição do experimento. Não presumir imunidade a explosivos.

### Contrato dos relatórios
- samples: `session,frame,phase,autoaim_enabled,target_x,target_y,aim_x,aim_y,status,reason`.
- events: `session,frame,event,phase,detail`.
- diagnostics: `session,frame,severity,code,detail`.
- Atualmente `unresolved` significa que nenhum leitor com offsets da ROM e domínio do emulador validados foi integrado. Campos vazios **não equivalem a ponteiro zero**.
- Dados de mira só poderão ser preenchidos por leitor que obtenha símbolos validados, ROM/hash e domínio/endianidade compatíveis, e cuja proveniência seja arquivada com a sessão.
- Sem endereços validados: coleta de frames/eventos é operacional, mas aquisição automática do alvo permanece bloqueada.

### Critérios de validação
Comparar controles negativos e positivos; correlacionar mudanças dos ponteiros de alvo com a entrada/saída de inimigos visíveis, obstáculos, ausência de arma equipada, troca de alvo e autoaim desligado. Exigir repetição em diferentes partidas antes de promover um símbolo para `validated`.
