# 3. Dado o vetor de preços de um catálogo: precos = [19.90, 45.00, 8.50, 120.00, 3.99, 67.30, 15.75, 220.00, 5.49, 32.00] exiba cada preço, um por linha.

precos: list[float] = [19.90, 45.00, 8.50, 120.00, 3.99, 67.30, 15.75, 220.00, 5.49, 32.00]
i:int = 0

# preco representa o valor de cada posição da lista precos
# Mostra cada preco dentro da lista precos
# i mostra o índice da lista
for preco in precos:
    print(i, preco)  
    i+=1  

for i in range(len(precos)):
    print(i, precos[i])

for i in range(len(precos)):
    print(precos[i])
    