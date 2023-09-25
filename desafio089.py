'''
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

lista0=[]
lista1=[]
opc = "S"

while opc.upper() == "S":
    lista0.append(input('Nome: '))
    lista0.append(float(input('Nota 1: ')))
    lista0.append(float(input('Nota 2: ')))
    lista1.append(lista0[:])
    lista0.clear()

    opc = input('Deseja continuar? S/N: ')
    
print('=-'*11)

print('No\tNome\tMedia')
print('-'*22)
for i,j in enumerate(lista1):
    print(i, end='')
    print(f'\t{j[0]}', end='')
    print(f'\t{(j[1]+j[2])/2}')

opc = 0

while opc != 999:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe):'))

    if opc >= 0 and opc < len(lista1):
        lista0 = lista1[opc]
        print(f'Notas do {lista0[0]} são [{lista0[1]}, {lista0[2]}]')
        print('-'*30)

print('FINALIZANDO...')
print('VOLTE SEMPRE...')
