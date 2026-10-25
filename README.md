# GoldenEye.mapping

Catálogo canônico, versionado e auditável de endereços, estruturas e comportamentos de memória de **GoldenEye 007 (Nintendo 64)**.

> Estado inicial: nenhuma localização de memória foi validada. Não confunda o modelo de catálogo com descobertas da ROM.

## Princípios
- Endereços sempre vinculados à identidade da ROM e ao contexto do emulador.
- Cada afirmação possui evidência, método, reprodutibilidade e estado de confiança.
- Observações **não** são automaticamente contratos estáveis.
- Bots e ferramentas consumidoras devem ler este catálogo, sem duplicar endereços locais.
- Não publicar ROMs, saves proprietários ou material protegido.

## Organização
- `catalog/roms.json`: variantes identificadas por hashes; inicialmente vazio.
- `catalog/symbols.json`: símbolos canônicos (não confundir com candidatos); permanece vazio até validação.
- `catalog/candidates.json`: candidatos e observações experimentais com proveniência e restrição somente leitura.
- `catalog/behaviors.json`: hipóteses e comportamentos observados; inicialmente vazio.
- `schema/`: contratos JSON Schema.
- `docs/`: metodologia e compatibilidade.
- `experiments/`: protocolo experimental.
- `scripts/validate_catalog.py`: validação estrutural e cruzada sem dependências externas.
- `scripts/validate_candidates.py`: validação independente do catálogo experimental.
- `tests/`: testes automatizados.
  
## Primeiro experimento
1. Identificar a ROM (nome, região, revisão e SHA-256 do arquivo usado).
2. Registrar versão e núcleo N64 do emulador.
3. Capturar estados controle: parado, inimigo fora de visão, inimigo visível, mira assistida ligada/desligada, disparo.
4. Comparar diferenças e repetir com reinicializações e cenários negativos.
5. Registrar candidato, evidência e condições de validade; só promover a `validated` após replicação.

## Validar
```sh
python scripts/validate_catalog.py
python scripts/validate_candidates.py
python -m unittest discover -s tests -v
```

Consulte [docs/methodology.md](docs/methodology.md) antes de adicionar valores.

## Auto-aim: observação da RDRAM (23/10/2026)

O experimento [Auto-Aim Memory Discovery v1](experiments/autoaim_memory_discovery_v1_20261023.json) documenta **323.702** bytes alterados entre A1 (ligado) e B (desligado), dos quais **23.287** retornaram ao valor de A1 em A2 (religado), em uma sessão de 8 MiB de `RDRAM`. Os offsets listados são **candidatos reversíveis, não endereços identificados de auto-aim**. A ROM/núcleo desta sessão ainda não possuem identidade comprovada; por isso o resultado fica em `experiments/` e `catalog/symbols.json` permanece vazio. CSV integral e dumps ficam locais no `GoldenEye.assistant/output/` do operador.

## Auto-Aim horizontal e Auto-Align (planejamento)

O [protocolo Horizontal Correction / Bond Heading v1](docs/AUTOAIM_HORIZONTAL_AUTOALIGN_V1.md) documenta as hipóteses, os controles experimentais e os critérios para validar a correção horizontal da arma e a orientação de Bond. **Nenhum símbolo novo foi validado**, e a aplicação Auto-Align permanece desabilitada.

## Auto-Aim v1.6 — Consolidação semântica (evidências)

[Registro experimental v1.6](experiments/autoaim_semantic_consolidation_v1_6_20261023.json): três offsets reproduziram seis intervenções ON/OFF e permaneceram estáveis em dois controles negativos. Outros dois offsets permanecem inconclusivos. Identidade de ROM/núcleo e função semântica não comprovadas; **não há novos símbolos em `catalog/symbols.json` nem permissão de escrita ou controle**.

## Recebimento permanente: candidatos e endereços validados (24/10/2026)

O repositório recebe **ambos**, separadamente: `catalog/candidates.json` preserva offsets experimentais mesmo quando a identidade de ROM/núcleo da sessão não foi comprovada; `catalog/symbols.json` contém símbolos sujeitos ao contrato canônico, com status e evidência vinculada. O status `reproduced` de um candidato **não** valida sua função. **Nenhum candidato concede escrita ou automação.** Processo e critérios de promoção: [docs/CANDIDATE_INTAKE.md](docs/CANDIDATE_INTAKE.md).

A [auditoria horizontal v1.5.1](experiments/horizontal_correction_v1_5_1_20261024.json) preserva as duas sessões e a correlação observada nos offsets `0x0D3998` e `0x0D3D40` (833 pares sincronizados, interpretação float32 BE hipotética, diferença próxima de -2). Os campos também variam quando Bond gira sem alvo: **não constituem headings validados**.

## Soldier #1 / Freeze — evidência experimental v1.8.4 (25/10/2026)

[Registro auditável](experiments/bond_soldier_freeze_transition_v1_8_4_20261025.json). O byte candidato `0x02C90C` reproduziu transições `00 ↔ FF` temporalmente relacionadas a Freeze ON/OFF; as janelas RAW de 4 bytes `0x20F594` e `0x20F5AC` variaram durante fases de movimento e ficaram estáveis em controles congelados na sessão íntegra `20261025T153459Z_9589` (7.801 frames; 22 episódios heurísticos; transições no frame 11549, 13414 e 16704). Uma sessão anterior terminou por `invalid_marker` e não é evidência de encerramento íntegro. Todos os três endereços ficam em `catalog/candidates.json` com status `reproduced`, **não** em `catalog/symbols.json`. Atribuição espacial X/Z, formato numérico definitivo, identidade ROM/núcleo e natureza primária do indicador Freeze permanecem **não validados**. Somente leitura, sem autorização de escrita ou controle.

## Contexto Mission/Part das capturas Bond–Soldier (25/10/2026)

O operador identificou a tela **Mission 1: Arkangelsk / Part I: Dam**, vinculando esse contexto às capturas experimentais Bond/Soldier v1.8.2–v1.8.4. [Registro estruturado de contexto](experiments/bond_soldier_mission_part_context_20261025.json) e [evidências técnicas vinculadas](experiments/bond_soldier_freeze_transition_v1_8_4_20261025.json). A identificação baseia-se em screenshot e declaração do operador, **não** em leitura independente da flag de missão em cada sessão. Endereços absolutos, coordenadas X/Z e identidade do soldado **não são transferíveis automaticamente** para outras Mission/Part. Comparações futuras deverão registrar missão, parte, SID, ROM/núcleo, identidade do objeto e respostas a controles equivalentes. Não há promoção de símbolos canônicos.
