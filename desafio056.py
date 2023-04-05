'''
Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4
pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome
do homem mais velho e quantas mulheres têm menos de 20 anos.
'''

somaidade = 0
maisvelho = 0
nomevelho = ''
qtdmulheres = 0

for i in range(4):
    nome=input('Digite o nome: ')
    idade=int(input('Digite a idade: '))
    sexo=input('Digite o sexo: ').upper()

    somaidade+=idade

    if sexo == 'M':
        if idade > maisvelho:
            maisvelho = idade
            nomevelho=nome
    elif sexo == 'F':
        if idade < 20:
            qtdmulheres += 1

print(f'A media de idade do grupo foi de {somaidade/4} anos.')
print(f'O homem mais velho tem {maisvelho} e se chama {nomevelho}')
print(f'Ao todo são {qtdmulheres} mulheres com menos de 20 anos')




