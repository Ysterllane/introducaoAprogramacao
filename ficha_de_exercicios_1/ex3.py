# 3. Escreva um programa que leia dois números em variáveis a e b e,
#  usando uma variável auxiliar, 
# troque os valores entre elas,
#  imprimindo o resultado antes 
# e depois da troca.

a: float = float(input("Digite o 1° número: "))
b: float = float(input("Digite o 2° número: "))

print(a, b)

auxiliar: float = a+b
a = auxiliar - a
b = auxiliar - b 

print(a, b)
