# Metodologia de mapeamento

## Níveis de evidência
- `candidate`: endereço/hipótese ainda não isolado de alternativas.
- `observed`: correlação detectada numa sessão documentada.
- `reproduced`: mesmo resultado repetido em sessões distintas, com controles.
- `validated`: reproduzido na variante declarada com positivos e negativos, tipo/escala e limites documentados.
- `rejected`: hipótese refutada, preservada para evitar redescoberta.

Estados são **por registro e por variante**, não globalmente transferíveis. `validated` não implica layout invariável noutras regiões/revisões ou emuladores.

## Registro mínimo
Toda evidência deve incluir `id`, `rom_id`, `environment`, `procedure`, `observations` e `artifacts` (pode ser array vazio quando ainda não há arquivo).
Endereços também exigem domínio (RDRAM/ROM/outro), largura, endianidade, método de resolução, condição de validade e ids das evidências.
Endereços dinâmicos exigem cadeia de ponteiros, base e política de invalidação.
Valores sensíveis a cena, tela ou arma devem documentar o escopo.

## Processo
1. Isolar uma única variável de entrada por contraste.
2. Guardar frame, fase de jogo, controles acionados e dados de origem.
3. Testar contra hipóteses alternativas; evitar concluir causalidade de mera correlação.
4. Repetir após reset/reload e com um controle negativo.
5. Vincular evidências e promover confiança após revisão.
6. Preservar entradas rejeitadas, acrescentando substituição quando necessário.

## Compatibilidade
Não assumir equivalência entre ROM USA/PAL/JPN, revisões, hacks, versões de BizHawk ou núcleos N64. Unidades de endereço devem ser explícitas; separar endereço físico de deslocamento no domínio de leitura da API.
