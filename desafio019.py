'''
 Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
 Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela
 nome do escolhido.
'''

import random

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

minhalista = [aluno1, aluno2, aluno3, aluno4]

print(f'O nome escolhido foi {random.choice(minhalista)}')

