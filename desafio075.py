'''
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

tupla = (int(input('Digite um número: ')), int(input('Digite um segundo número: ')), int(input('Digite um terceiro número: ')), int(input('Digite um último número: ')))

qtd9 = tupla.count(9)

if (3 in tupla):
    pos3 = tupla.index(3)+1
else:
    pos3 = 0

pares = [numero for numero in tupla if numero % 2 == 0]

print(f'Você digitou os valores {tupla}')
print(f'O nove apareceu {qtd9} vezes')

if pos3 > 0:
    print(f'O três foi digitado na posição {pos3}')
else:
    print('O número três não foi digitado')

print(f'Os pares são {pares}')