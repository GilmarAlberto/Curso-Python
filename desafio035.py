'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.
'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo  número: '))
n3 = int(input('Digite o terceiro número: '))


if n1+n2 > n3 and n1+n3 > n2 and n2+n3 > n1:
    print('É um triângulo!')
else:
    print('Não é um triângulo!')