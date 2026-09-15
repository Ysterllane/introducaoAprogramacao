# A distância da Terra à Lua é de aproximadamente 380.000km. Em 1 abril de 2026, às 00:00, horário do Brasil, a missão da Nasa Artemis II fez seu primeiro voo tripulado em direção à Lua. O módulo Artemis II retornou à Terra após 231 horas de missão. A missão tinha o objetivo de realizar um sobrevoo ao redor da Lua sem pousar, testando os sistemas de suporte à vida da espaçonave Orion e o foguete SLS com humanos a bordo.

# (Questão 1) Desconsiderando a distância percorrida pela Artemis II no sobrevoo ao redor da lua, implemente um algoritmo que calcula a velocidade média do módulo Artemis II para ir e voltar da lua. Considere: Vm = S_total / T_total

# (Questão 2) Elabora um algoritmo que identifique o dia em que o módulo pousou de volta a terra.

# (Questão 3) Elabore um algoritmo que identifique o horário do dia em que o módulo pousou de volta na Terra, sendo manha (das 6h as 12h), tarde (das 13h as 18h) ou noite.

distacia:int = 380000 * 2
tempo:int = 231
velocidadeMedia:float = distancia / tempo
print(velocidadeMedia)

diaDePartida:int = 1
horasParaDias:int = 231 // 24
print(f"Ele voltou no dia {diaDePartida + horasParaDias} de abril.")

horasRestantes:int = 231 % 24
if horasRestantes >= 6 and horasRestantes < 12:
    print("Voltou de manhã.")
elif horasRestantes >= 12 and horasRestantes <= 18:
    print("Voltou de tarde.")
else:
    print("Voltou de noite.")

