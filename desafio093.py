'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

cadastro = {}

cadastro['nome'] = input('Nome do Jogador: ')

qtdPart = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))

lista = []
totGols = 0

for i in range(0,qtdPart):
    lista.append(int(input(f'Quantos gols na partida {i}? ')))
    totGols += lista[i]

cadastro['gols'] = lista[:]
cadastro['total'] = sum(cadastro['gols'])

print('=-'*30)
print(cadastro)
print('=-'*30)

for k,v in cadastro.items():
    print(f'O campo {k} tem o valor {v} ')

print('=-'*30)
print(f'O jogador {cadastro["nome"]} jogou {len(cadastro["gols"])} partidas')

for k,v in enumerate(cadastro['gols']):
    print(f'=> Na partida {k}, fez {v} gols.')

print(f'Foi um total de {cadastro["total"]}')

