pessoas = {'nome': 'Gustavo','sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for k in pessoas.values():
    print(k)

for k,v in pessoas.items():
    print(f'{k} {v}')

del(pessoas['sexo'])

for k,v in pessoas.items():
    print(f'{k} {v}')

pessoas['nome'] = 'Gilmar'

print(pessoas.values())

pessoas['peso'] = '96'

print(pessoas.values())

brasil = []

estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)

estado = {}
brasil = []

for c in range(0,3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())

print(brasil)

for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}')



