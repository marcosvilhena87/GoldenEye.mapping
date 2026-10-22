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
- `catalog/symbols.json`: endereços, ponteiros e estruturas; inicialmente vazio.
- `catalog/behaviors.json`: hipóteses e comportamentos observados; inicialmente vazio.
- `schema/`: contratos JSON Schema.
- `docs/`: metodologia e compatibilidade.
- `experiments/`: protocolo experimental.
- `scripts/validate_catalog.py`: validação estrutural e cruzada sem dependências externas.
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
python -m unittest discover -s tests -v
```

Consulte [docs/methodology.md](docs/methodology.md) antes de adicionar valores.
