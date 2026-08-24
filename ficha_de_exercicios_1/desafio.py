print("Olá usuário, vou te explicar umas informações:\n\n" 
      
"1 - Segunda-Feira\n"
"2 - Terça-Feira\n"
"3 - Quarta-Feira\n" 
"4 - Quinta-Feira\n" 
"5 - Sexta-Feira\n" 
"6 - Sábado\n"
"7 - Domingo\n\n"

"A partir disso, você deve digitar um número, por exemplo 200 e eu tenho que descobrir que dia da semana é\n")

num:int = int(input("Digite um número natural maior que zero: "))

if num % 1 == 0:
    print("Seu dia da semana é Segunda-Feira")

#if num <= 0 :
#    print("Seu número não é natural e maior que zero")
#    num:int = int(input("Digite um número natural maior que zero: "))
