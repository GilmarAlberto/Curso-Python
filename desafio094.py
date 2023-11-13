'''
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

lista = []
soma_idades = 0
while True:
    dic = {}

    while True:
        dic['nome'] = input('Nome: ')
        if not dic['nome']:
            print('Erro: Nome não pode ser vazio.')
        else:
            break

    while True:
        dic['sexo'] = input('Sexo: ')
        if not dic['sexo'].upper() in 'MF':
            print('Erro: Por favor digite apenas M/F.')
        else:
            break

    while True:
        try:
            dic['idade'] = int(input('Idade: '))
            if dic['idade'] <= 0:
                print('Erro: Insira uma idade válida.')
            else:
                break
        except ValueError:
            print('Erro: Insira uma idade válida.')

    soma_idades+=dic['idade']

    while True:
        opc = input('Quer continuar [S/N]? ')
        if not opc.upper() in 'SN':
            print('Erro: Por favor digite apenas S/N')
        else:
            break

    lista.append(dic)

    if opc.upper() == 'N':
        break

print('=-'*30)

media_idade = soma_idades / len(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas')
print(f'B) A media de idade é {media_idade: .2f}')
print(f'C) As mulheres cadastradas foram ',end='')

for k,v in enumerate(lista):
    if v['sexo'].upper() == 'F':
        print(f'{v["nome"]} ', end='')

print('')
print(f'D) Lista de pessoas que estão acima da média: ')

for k,v in enumerate(lista):
    if v['idade'] > media_idade:
        print(f'     nome: {v["nome"]};', end=' ')
        print(f'sexo: {v["sexo"]};', end=' ')
        print(f'idade: {v["idade"]};')

print('<< ENCERRADO >>')