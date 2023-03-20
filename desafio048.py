'''
Exercício Python 048: Faça um programa que calcule a soma entre todos os
números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''

soma=0
qtdnum=0

for i in range(1,501,2):
    if i%3 == 0:
        print(i,end=' ')
        soma += i
        qtdnum += 1

print(f'\nA soma de todos os {qtdnum} valores é {soma}.')