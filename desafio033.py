"""
Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo  número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 < n2 and n1 < n3:
    print(f'{n1} é o menor número!')
elif n2<n3:
    print(f'{n2} é o menor número!')
else:
    print(f'{n3} é o menor número!')

if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior número!')
elif n2>n3:
    print(f'{n2} é o maior número!')
else:
    print(f'{n3} é o maior número!')
