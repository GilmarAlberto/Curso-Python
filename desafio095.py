'''
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
listão =[]

while True:
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

    listão.append(cadastro)
    
    while True:
        opc = input('Quer continuar [S/N]? ')
        if opc.upper()[0] in 'SN':
            break

        print('Erro: Por favor digite apenas S/N')

    if opc.upper() == 'N':
        break

print('=-'*23)
print('cod\tnome\t\tgols\t\ttotal')
print('-'*45)
for item, cadastro in enumerate(listão):
        print(f'{item}\t{cadastro["nome"]}\t\t{cadastro["gols"]}\t{cadastro["total"]}')
print('-'*45)

while True:
    
    opc = int(input('Mostrar Dados de qual jogador? (999 pra parar) '))

    if opc == 999:
        break

    if opc < len(listão):
        print('-=' * 23)
        print(f'-- Levantamento do jogador {listão[opc]["nome"]}')
        for i, gol in enumerate(listão[opc]['gols']):
            print(f'   No jogo {i+1} fez {gol} gols.')
        print('-=' * 23)
    else:
        print('Erro: Jogador não encontrado. Tente novamente.')