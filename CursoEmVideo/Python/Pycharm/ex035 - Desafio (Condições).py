from random import randint
from time import sleep
n = randint(0, 5)
sorte = int(input("Qual foi o número entre 0 e 5 que o computador escolheu desta vez? "))

print("PROCESSANDO...")
sleep(2)

print("O número gerado foi {}.".format(n))
if sorte == n:
    print("Parabéns, vocÊ acertou!")
else:
    print("Ops, não foi desta vez!")