'''
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

num = int(input('Digite um número: '))

total = 1
while num > 1:

    print(f'{num} x ', end='')

    total *= num

    num -= 1
print('1', end = ' ')

print(f' = {total}')





