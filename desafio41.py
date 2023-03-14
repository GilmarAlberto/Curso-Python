'''
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa
leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a
idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''

from datetime import date

anoatual = date.today().year

anonasc= int(input('Digite o ano de nascimento: '))

idade = anoatual - anonasc

if idade <= 9:
    categ = 'MIRIM'
elif idade <= 14:
    categ = 'INFANTIL'
elif idade <= 19:
    categ = 'JÚNIOR'
elif idade <=25:
    categ = 'SÊNIOR'
else:
    categ = 'MASTER'

print(f'O atleta tem {idade} anos portanto a categoria dele é {categ}!')