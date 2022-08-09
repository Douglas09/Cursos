from math import hypot
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = hypot(co, ca)
print("A hipotenusa vai medir {:.2f}".format(hi))

'''
[Forma matemática sem importação de classe externa]

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print("A hipotenusa vai medir {:.2f}".format(hi))
'''