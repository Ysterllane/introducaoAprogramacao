# 12. Escreva um programa que leia o valor de uma compra 
# e aplique desconto por faixa: até R$100 sem desconto, de R$100 a R$500 com 5%, acima de R$500 com 10%. Imprima o valor final.

valorCompra: float = float(input("Digite o valor da compra: "))

if valorCompra >= 0:
    if valorCompra <= 100:
        print("R$:", valorCompra, " Sem desconto.")
    elif valorCompra <= 500:
        print("R$:", valorCompra * 0.95, "Desconto de 5%.")
    elif valorCompra > 500:
        print("R$:", valorCompra * 0.90, "Desconto de 10%")
else:
    print("Digite um valor de compra válido na próxima tentativa.")
