'''
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
import random

tupla = (random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9))

print(tupla)
print(f'O menor valor sorteado foi {min(tupla)}')
print(f'O maior valor sorteado foi {max(tupla)}')