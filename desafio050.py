'''
Exercício Python 050: Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar,
desconsidere-o.
'''

lista = [None]*6
soma = 0
pares = 0

for i in range(0,6):
    lista[i] = int(input(f'Digite o número {i+1}: '))
    if lista[i]%2 == 0:
        soma += lista[i]
        pares +=1
print(f'A soma dos {pares} números pares é: {soma}')

