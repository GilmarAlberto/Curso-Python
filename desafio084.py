'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

listao = []
lista = []
maiorpeso = []
menorpeso = []
opc = "S"

while opc.upper() == "S":
    lista.append(input('Nome: '))
    lista.append(float(input('Peso: ')))
    listao.append(lista[:])
    lista.clear()

    opc = input('Deseja continuar? S/N: ')

print('=-'*40)

print(f'Foram cadastradas {len(listao)} pessoas.')

for pessoa in (listao):

    if len(maiorpeso)==0:
        maiorpeso.append(pessoa[:])
    elif pessoa[1] > maiorpeso[0][1]:
        maiorpeso.clear()
        maiorpeso.append(pessoa[:])
    elif pessoa[1] == maiorpeso[0][1]:
        maiorpeso.append(pessoa[:])

for pessoa in (listao):

    if len(menorpeso)==0:
        menorpeso.append(pessoa[:])
    elif pessoa[1] < menorpeso[0][1]:
        menorpeso.clear()
        menorpeso.append(pessoa[:])
    elif pessoa[1] == menorpeso[0][1]:
        menorpeso.append(pessoa[:])

print(f'O maior peso foi {maiorpeso[0][1]}. Peso de: ',end=" ")
for pessoa in (maiorpeso):
    print(f'[{pessoa[0]}]',end=" ")

print(f'\nO menor peso foi {menorpeso[0][1]}. Peso de: ',end=" ")
for pessoa in (menorpeso):
    print(f'[{pessoa[0]}]',end=" ")