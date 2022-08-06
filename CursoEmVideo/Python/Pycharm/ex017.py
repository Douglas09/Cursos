dias = int(input("Quantos dias alugados? "))
dist = float(input("Quantos Km rodados? "))

#Carro custa R$60,00 por dia e R$0.15 por Km rodado
pago = (dias * 60) + (dist * 0.15)
print("O total a pagar é R${:.2f}.".format(pago))