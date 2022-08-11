nome = input("Informe o seu nome: ")

print("Você informou {}.".format(nome))
print("Primeiro nome: {}".format(nome.split()[0]))
print("Último nome: {}".format(nome.split().pop()))
