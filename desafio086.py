"""
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
"""

matriz = [[],[],[]]
num = 0

for i in range(0,3):
    for j in range(0,3):
        num = int(input(f'Digite um valor para [{i}][{j}]: '))
        matriz[i].append(num)
print("=-"*30)

for i in matriz:
    for j in i:
        print(f'[ {j:^5} ]', end="")
    print('')


        




