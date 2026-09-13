# 9. Escreva um programa que leia os três lados de um triângulo e classifique-o em equilátero (todos os lados iguais), isósceles (dois lados iguais) ou escaleno (todos diferentes).

lado1Triangulo: float = float(input("Digite o lado 1 do triângulo: "))
lado2Triangulo: float = float(input("Digite o lado 2 do triângulo: "))
lado3Triangulo: float = float(input("Digite o lado 3 do triângulo: "))

if lado1Triangulo == lado2Triangulo and lado1Triangulo == lado3Triangulo:
    print("Equilátero")
elif lado1Triangulo != lado2Triangulo & lado1Triangulo != lado3Triangulo &  lado3Triangulo != lado2Triangulo:
    print("Escaleno")
else:
    print("Isóceles")
