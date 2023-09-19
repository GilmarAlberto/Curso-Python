"""
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
"""

matriz = [[],[],[]]
num = 0
par = 0
tcol = 0
maior = 0
for i in range(0,3):
    for j in range(0,3):
        num = int(input(f'Digite um valor para [{i}][{j}]: '))
        matriz[i].append(num)
print("=-"*30)

for i in matriz:
    for j in range(len(i)):
        print(f'[ {i[j]:^5} ]', end="")

        if i[j]%2 == 0:
            par += i[j]

        if j == 2:
            tcol += i[j]

        if j == 1 and i[j] > maior:
            maior = i[j]

    print('')

maior = matriz[1][0]

if matriz[1][1]>maior:
    maior = matriz[1][1]
if matriz[1][2]>maior:
    maior = matriz[1][2]

print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {tcol}')
print(f'O maior valor da segunda linha é {maior}')