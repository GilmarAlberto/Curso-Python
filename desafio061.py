'''
Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de
uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

termo = int(input('Digite o Primeiro Termo: '))
razão = int(input('Digite a razão: '))

i=1

while i<=10:
    print(termo, end=' → ')
    termo+=razão
    i+=1

print('ACABOU!')
