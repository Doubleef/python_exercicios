#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
aluno1 = str(input("Digite o nome do primeiro Aluno: "))
aluno2 = str(input("Digite o nome do segundo Aluno: "))
aluno3 = str(input("Digite o nome do terceiro Aluno: "))
aluno4 = str(input("Digite o nome do Quarto Aluno: "))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print("O Aluno escolhido foi {}".format(escolhido))



