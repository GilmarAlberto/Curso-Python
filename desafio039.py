'''Python 039: Faça um programa que leia o ano de nascimento de um jovem e
informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço
militar, se é a hora exata de se alistar ou se já passou do tempo do
alistamento. Seu programa também deverá mostrar o tempo que falta ou que
passou do prazo.'''

from datetime import date

anoatual = date.today().year

anonasc= int(input('Digite o ano de nascimento: '))

idade = anoatual - anonasc


if idade < 18:
    print(f'Faltam {18 - idade} anos para se alistar!')
elif idade > 18:
    print(f'Passaram {idade - 18} anos do alistamento!')
else:
    print('Está na hora de se alistar!')
