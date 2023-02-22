"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""

from calendar import isleap
from datetime import date

ano = int(input('Digite o ano. 0 para o ano atual: '))

if ano ==0:
    ano = date.today().year

if isleap(ano):
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')