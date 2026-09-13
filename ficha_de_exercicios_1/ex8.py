# 8. Escreva um programa que leia um número e informe se ele é positivo, negativo ou zero.

num:float = float(input("Digite um número: "))

if num == 0:
    print("Zero")
elif num > 0:
    print("Positivo")
else:
    print("Negativo")