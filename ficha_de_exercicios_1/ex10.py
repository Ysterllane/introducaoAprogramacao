# 10. Escreva um programa que leia peso e altura, calcule o IMC ( peso / altura**2 ) e classifique em Abaixo do peso, Peso normal, Sobrepeso ou Obesidade.

peso: float = float(input("Digite seu peso: "))
altura: float = float(input("Digite sua altura: "))
print(peso/(altura**2))
