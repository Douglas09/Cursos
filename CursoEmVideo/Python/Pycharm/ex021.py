#Sortear aluno que apagará o quadro

from random import randint

alunos = ["Douglas", "Daniela", "Zuleide", "Djanho"]
sorteio = randint(0, 3);
print("O aluno {} apagará o quadro agora.".format(alunos[sorteio]))
