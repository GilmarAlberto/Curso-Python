'''
Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele
é ou não um número primo.
'''

num = int(input('Digite um número: '))
#print('\033[032m 1\033[0m',end=' ')
cont=0
for i in range (1, num+1):
    if num%i==0:
        print(f'\033[032m{i}\033[0m', end=' ')
        cont+=1
    else:
        print(f'\033[031m{i}\033[0m',end=' ')

print(f'\nO numero {num} foi divisível por {cont} vezes')

if cont>2:
    print('E por isso NÃO É PRIMO!')
else:
    print('E por isso É PRIMO!')

