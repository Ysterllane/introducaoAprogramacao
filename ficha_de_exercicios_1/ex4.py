# 4. Escreva um programa que leia um número inteiro
#  e informe se ele é par ou ímpar, usando o operador % .

num:int = int(input("Digite um número inteiro: "))

if num % 2 == 0:
    print("Par")
else:
    print("Impar")