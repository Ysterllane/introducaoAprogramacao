nota1:float = float(input("Digite sua primeira nota: "))
nota2:float = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Sua nota é ", media, "e você foi aprovado.")

if media < 5 and media < 7:
    print("Sua nota é ", media, "e você foi reprovado0.")

else:
    print("Sua nota é ", media, "e você foi reprovado.")