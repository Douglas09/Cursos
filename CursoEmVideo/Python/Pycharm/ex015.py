alt = float(input("Informe a altura da parede: "))
larg = float(input("Informe a largura da parede: "))
area = alt * larg

print("Sua parede tem a dimensão de {}X{} e sua área é de {}m²".format(larg, alt, area))

tinta = area / 2
print("Para pintar esta parede você precisará de {}l de tinta.".format(tinta))