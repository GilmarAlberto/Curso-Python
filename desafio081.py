'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista. 
'''

lista = []
num = 0
opc = "S"

while opc.upper() == "S":
    num=int(input('Digite um valor: '))

    lista.append(num)
       
    opc = input('Deseja continuar? S/N: ')

lista.sort(reverse=1)
print('=-'*30)
print(f'Você digitou {len(lista)} elementos')
print(f'Você digitou os valores em ordem decrescente {lista}')

if 5 in lista: 
    print('O valor 5 faz parte da lista!')
else: 
    print('O valor 5 não faz parte da lista!')