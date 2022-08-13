f = input("Digite uma frase qualquer: ").strip()

print("Sua frase possui {} letras <A>.".format(f.upper().count('A')))
print("A primeira posição em que aparece a letra <A> é na {}.".format(f.upper().find('A') + 1))
print("A última posição em que aparece a letra <A> é na {}.".format(f.upper().rfind('A') + 1))
