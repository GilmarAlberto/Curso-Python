'''
Exercício Python 037: Escreva um programa em Python que leia um número inteiro
qualquer e peça para o usuário escolher qual será a base de conversão: 1 para
binário, 2 para octal e 3 para hexadecimal.
'''

num=int(input('Digite um número: '))

opc=0

while opc < 1 or opc > 3:
    opc = int(input('Qual a base de conversão? [1] - binário; [2] - octal; [3] - hexadecimal: '))

if opc == 1:
    print(f'O número {num} em binário é {bin(num) [2:]}')
elif opc == 2:
    print(f'O número {num} em octal é {oct(num) [2:]}')
else:
    print(f'O número {num} em hexadecimal é {hex(num) [2:]}')



