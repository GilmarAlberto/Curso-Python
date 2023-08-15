'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
'''

lista = []

for i in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))

print("=-"*30)
    
print(f'Você digitou os valores: {lista}')

maior_valor = max(lista)
menor_valor = min(lista)

print(f'O maior valor digitado foi {maior_valor} nas posições ',end="")
for i in range(len(lista)):
    if lista[i] == maior_valor:
        print(f'{i}...',end="")

print(f'\nO menor valor digitado foi {menor_valor} nas posições ', end="")
for i in range(len(lista)):
    if lista[i] == menor_valor:
        print(f'{i}...',end="")
