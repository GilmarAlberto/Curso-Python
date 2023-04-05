'''
Exercício Python 054: Crie um programa que leia o ano de nascimento de sete
pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e
quantas já são maiores.
'''

from datetime import date

anoatual = date.today().year

anonasc=['']*7

menores = maiores = 0

for i in range(len(anonasc)):

    anonasc[i]=int(input(f'Em que ano a {i+1}ª pessoa nasceu: '))

    idade = anoatual - anonasc[i]

    if idade<18:
        menores+=1
    else:
        maiores+=1

print(f'Ao todo tivemos {maiores} maiores de idade')
print(f'E também tivemos {menores} menores de idade')






