from calendar import isleap
ano = int(input("Em que ano você está? "))
print("É bissexto." if isleap(ano) else "Não é bissexto.")