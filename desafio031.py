"""
 Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o
 preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
 parta viagens mais
"""

dist = int(input('Qual a distância da viagem? '))

if dist > 200:
    preço = dist*0.45
else:
    preço = dist*0.5

print(f'O preço da viagem é R$ {preço : .2f}')