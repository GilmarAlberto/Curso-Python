'''
Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a
razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''

termo = int(input('Digite o Primeiro Termo: '))
razão = int(input('Digite a razão: '))

for i in range(0,10):
    print(termo, end=' → ')
    termo+=razão
print('ACABOU!')

