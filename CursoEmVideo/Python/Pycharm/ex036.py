vel = float(input("Informe a velocidade atual de seu carro: "))

#Caso o carro ultrapassar os 80 km/h, o usuário será multado em R$7,00 por KM excedido
if vel > 80:
    print("Você foi multado por ultrapassar do limite de velocidade. pague R${:.2f}.".format((vel - 80) * 7))
else:
    print("Você está dentro da velocidade permitida para a via.")