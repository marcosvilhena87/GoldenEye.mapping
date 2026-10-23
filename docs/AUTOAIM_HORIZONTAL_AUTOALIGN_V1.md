# Auto-Aim horizontal e Auto-Align — hipóteses e protocolo v1

Data: 2026-10-23. Estado: **proposto / não validado**.

## Objetivo
Investigar a correção horizontal realizada pelo auto-aim nativo de GoldenEye 007 para, no futuro, alimentar um controlador que gire a direção (heading) de Bond até o alvo. Este documento **não** identifica endereços RDRAM, não certifica layout de estruturas e não autoriza automação.

## Conceitos separados
- **Heading de Bond**: orientação horizontal do personagem/câmera, a ser identificada experimentalmente.
- **Correção horizontal da arma**: desvio do disparo/mira em relação à direção de referência. Não assumir que equivale diretamente ao ângulo do alvo.
- **Alvo elegível/selecionado**: estados diferentes; ambos exigem evidência.
- **Entrada de giro**: ação produzida pelo controle virtual do emulador, independente da leitura de memória.

Nomes candidatos identificados em estudos de engenharia reversa (ex.: `weapon_theta_displacement`, `vv_theta`) são **pistas de pesquisa**, jamais endereços, provas de semântica ou símbolos validados deste projeto.

## Experimento: Horizontal Correction v1
1. Registrar hash da ROM, revisão, emulador/núcleo, arma, dificuldade e opção Auto-Aim.
2. Capturar Bond imóvel, sem inimigo visível (controle basal).
3. Com a mesma arma, apresentar alvo estático em posições esquerda, centro e direita, mantendo distância e demais variáveis.
4. Repetir com Auto-Aim OFF e ON, e controles sem alvo/fora de alcance.
5. Repetir após reinício; obter série temporal de frames, não somente instantâneos isolados.
6. Examinar candidatos da `Auto-Aim Memory Discovery v1.2` e comparar assinaturas dos cenários, sem interpretar mera correlação como causalidade.
7. Comparar movimentos normais/animação da arma para excluir falsos positivos; testar dois inimigos e oclusão.
8. Documentar direção do sinal, unidade, escala, atraso, estabilidade, critérios de invalidação e evidência reproduzível.

## Experimento: Bond Heading Discovery v1
Capturar rotação manual para esquerda/direita com cenários sem alvo e Auto-Aim OFF. Identificar candidato de orientação, verificar wrap-around de ângulo, diferenciação da oscilação da arma, repetibilidade e identidade ROM/núcleo. Não inferir heading a partir de posição X/Y.

## Gates de promoção
Manter em `experiments/` até que identidades ROM/núcleo e domínios/endianidade/larguras estejam confirmados, testes negativos e reinicializações reproduzidos, e evidências auditáveis documentadas. Só então propor símbolos ou comportamentos `validated` seguindo schema e metodologia do catálogo.

## Contrato esperado para consumidores
O `GoldenEye.assistant` só poderá consumir medições com validade explícita, identificação do alvo quando disponível, sinais e unidades calibrados e condições de aplicabilidade verificadas. Dado ausente, inválido ou ambíguo implica **nenhuma rotação automática**. Auto-Align e Auto-Shot devem ser ativados independentemente, com Auto-Shot desligado por padrão.

Referências internas: `experiments/autoaim_memory_discovery_v1_20261023.json`; protocolo v1.2 no `GoldenEye.assistant/docs/AUTOAIM_MEMORY_DISCOVERY_V1_2.md`.
