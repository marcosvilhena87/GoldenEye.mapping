# Contrato para consumidores

`GoldenEye.mapping` é a única fonte canônica de símbolos e hipóteses de memória.
Consumidores devem:
1. Identificar a ROM por hash antes de acessar um símbolo.
2. Aceitar somente entradas `validated` da mesma `rom_id` (ou modo exploratório explicitamente habilitado).
3. Verificar domínio de memória, largura, endianidade, resolução e condições do símbolo.
4. Falhar em modo seguro diante de símbolo ausente, ambíguo ou incompatível.
5. Não inferir certeza de endereços provisórios nem incluir offsets copiados e divergentes.
6. Guardar a revisão/commit do catálogo consultado para reproduzir resultados.

Uma API automática de disparo deve tratar auto-aim, elegibilidade de alvo, estado da arma e cadência como **hipóteses separadas**, até que cada mecanismo seja medido.
