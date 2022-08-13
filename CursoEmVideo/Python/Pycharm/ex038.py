d = float(input("Indique a distância em KM de sua viagem: "))

if d <= 200:
    print("Preço por KM rodado: R$0,50")
    print("Sua viagem custará R${:.2f}.".format(d * 0.5))
else:
    print("Preço por KM rodado: R$0,45")
    print("Sua viagem custará R${:.2f}.".format(d * 0.45))
