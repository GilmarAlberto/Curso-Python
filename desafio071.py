"""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

print('='*36)
print(f'Banco GAAP'.center(36))
print('='*36)
valor = int(input("Qual valor você quer sacar? R$ "))

cinquenta = valor//50
if cinquenta>0:
    valor = valor%50
vinte = valor//20
if vinte>0:
    valor = valor%20
dez = valor//10
if dez>0:
    valor = valor%10

print(f'Total de {cinquenta} notas de R$50')
print(f'Total de {vinte} notas de R$20')
print(f'Total de {dez} notas de R$10')
print(f'Total de {valor} notas de R$1')
print('='*36)
print('Volte sempre ao Banco GAAP! Tenha um bom dia!')

