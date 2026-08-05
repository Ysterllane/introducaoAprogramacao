nome = input("Qual o seu nome? ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite a sua altura: "))
imc:float = peso /(altura * altura)

print ("Olá, ", nome, "Seu peso é: ", peso, "Sua altura é: ", altura, "e seu IMC é: ", imc)

print(f"{nome}, seu peso é {peso}, sua altura é {altura} e seu IMC é {imc}")