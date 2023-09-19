'''
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

import random
import time

print('-'*30)
print(f'{"JOGO NA MEGA SENA":^30}')
print('-'*30)

qtd = int(input('Quantos jogos você quer sortear? '))

print('=-'*3, f'SORTEANDO {qtd} JOGOS','=-'*3)

lista = []

for i in range(qtd):

    mega = []
    cont = 1
    

    while cont <= 6:
        num=random.randint(1,60)
        
        if num not in mega:
            mega.append(num)
            cont+=1

    mega.sort()

    lista.append(mega)

for i,l in enumerate(lista):
    print(f'Jogo {i+1}: {l}')
    time.sleep(1)

print('=-'*5, '< BOA SORTE! >', '=-'*5)