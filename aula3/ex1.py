# distancia, valor do combustivel por litro, quantos litros gastou
# valor total de viagem é tantos rs e o veículo faz tantos km por L

distancia = float(input('Digite a distância percorrida pelo veículo: '))
preco_combustivel = float(input('Digite o preço do combustível: '))
litros_gastos = float(input('Digite quantos litros foram gastos na viagem: '))

custo_total:float = litros_gastos * preco_combustivel
km_por_litro:float = distancia / litros_gastos #Autonomia do veículo

print("O valor total da viagem é ", custo_total, " reais.")
print("O veículo faz ", km_por_litro, "Km/L")
