"""
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint

sorteio = {'Jogador 1': randint(1,6),'Jogador 2': randint(1,6), 'Jogador 3': randint(1,6), 'jogador 4': randint(1,6)}

print('Valores sorteados:')
for k,v in sorteio.items():
    print(f'{k} tirou {v} no dado.')

print('=-'*30)

ordenado = dict(sorted(sorteio.items(), key=lambda item: item[1], reverse = True))

print('==RANKING DE JOGADORES==')
for i, (k,v) in enumerate(ordenado.items(), start=1):
    print(f'{i}º lugar: {k} com {v} pontos.')





