# Recebimento de enderecos: candidatos e validados

## Politica permanente
O repositório **recebe e preserva os dois tipos de informação**, sem equiparar a confiabilidade:

- `catalog/candidates.json`: janelas/offsets investigativos, mesmo quando a identidade de ROM ou núcleo N64 da sessão não esteja verificada. Exigem domínio, largura observada, hipótese, experimento de origem e permissão `read_only`. Um offset de janela RAW não comprova o tipo numérico.
- `catalog/symbols.json`: símbolos canônicos estruturados vinculados a ROM cadastrada e `catalog/evidence.json`, regidos por `scripts/validate_catalog.py`. O estado `validated` exige identificação de variante, positivos/negativos, significado, representação, limites e reprodução independente.

`reproduced` no catálogo de candidatos quer dizer apenas *reprodução do padrão observado*, nunca função de memória validada.

## Fluxo de promoção
1. Capturar offsets em `GoldenEye.assistant`, sem escrita, com identificador da sessão, memória/domínio, marcadores, controles e arquivos locais.
2. Incluir/atualizar entrada em `catalog/candidates.json`, referenciando documento em `experiments/` e ressalvas. Não eliminar candidatos refutados; mudar para `rejected`.
3. Confirmar SHA-256 da ROM usada na sessão e núcleo N64. Não associar arbitrariamente evidência antiga a `catalog/roms.json` apenas por a ROM estar listada no repositório.
4. Isolar função semântica, formato, escala, cadeia de resolução e condições de validade com experimentos independentes.
5. Criar evidência formal em `catalog/evidence.json`, então registrar/promover o símbolo em `catalog/symbols.json` quando os critérios forem satisfeitos. Manter rastreabilidade do candidato original.
6. Rodar ambos validadores e testes. Consumidores e bots só podem usar símbolos explicitamente validados e compatíveis com a sessão; candidatos são exclusivamente para diagnóstico.

## Experimento horizontal v1.5.1
`experiments/horizontal_correction_v1_5_1_20261024.json` conserva duas sessões encerradas, 833 pares simultâneos, relação `B-A ~ -2` sob interpretação `float32 big-endian` hipotética e resposta também à rotação manual de Bond sem alvo. Não confundir com orientação da arma, correção automática ou heading de câmera validados.

## Validação
```powershell
python scripts/validate_catalog.py
python scripts/validate_candidates.py
python -m unittest discover -s tests -v
```
