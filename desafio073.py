'''
Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time do Coritiba.
'''

times = ('Botafogo', 'Grêmio', 'Flamengo','Palmeiras','Red Bull','Fluminense','São Paulo','Internacional','Athletico','Atlético','Fortaleza', 'Cruzeiro', 'Cuiabá','Santos','Bahia','Corinthians','Goiás','Vasco','América','Coritiba')

print('=-='*10)
print(f'Lista de times do brasileirão: {times}')
print('=-='*10)
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print('=-='*10)
print(f'Os quatro últimos colocados são: {times[-4:]}')
print('=-='*10)

ordenados = tuple(sorted(times))

print(f'Times em ordem alfabética: {ordenados}')

posição = times.index('Coritiba')

print('=-='*10)
print(f'O Coritiba está na {posição+1}ª posição')