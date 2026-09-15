# 11. Faça um programa em Python que verifique se um determinado ano é bissexto.

# O programa deve:

# Solicitar ao usuário que digite um ano;
# Verificar se o ano é bissexto de acordo com as seguintes regras:
# É divisível por 4 e não é divisível por 100; ou
# É divisível por 400;
# Exibir "Seu ano é bissexto" caso seja bissexto;
# Caso contrário, exibir "Seu ano não é bissexto".

ano: int = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("Seu ano é bissexto.")
else:
    print("Seu ano não é bissexto.")


