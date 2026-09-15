# 16. Um sistema de login permite no máximo 3 tentativas de senha. Caso o usuário erre todas, o acesso deve ser bloqueado — o programa precisa interromper as tentativas assim que esse limite for atingido.

senha = "abacate"

for i in range(3):
    tentativa = input("Digite sua senha: ")
    if senha == tentativa:
        print("Você acessou o sistema.")
        break
    elif i == 2:
        print("Acesso bloqueado.")







