"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""

num=input('Digite um numero: ')

#num1=str(print(num.zfill(4)))

num1=num.zfill(4)

print(num1)

print(f'milhar {num1[0]}')
print(f'centena {num1[1]}')
print(f'dezena {num1[2]}')
print(f'unidade {num1[3]}')
