a = input("Digite algo: ")
print("O tipo primitivo deste valor é, {}".format(type(a)))
print("Só tem espaços? ", a.isspace())
print("É um número? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("É alfanumérico? ", a.isalnum())
print("Está em maiúsculas? ", a.isupper())
print("Está em minúsculas? ", a.islower())

#Nem somente em maiúsculas, e nem somente em minúsculas
print("Está capitalizada? {}".format(a.istitle()))
