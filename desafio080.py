'''
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

lista = []

num = 0

for i in range(5):
    num = int(input('Digite um valor: '))

    if(not(lista)):
        print('Adicionado ao final da lista...')
        lista.append(num)
    else:

        inserido = False
        
        for j in range(0,len(lista)):

            if num < lista[j]:
                print(f'Adicionando na posição {j} da lista...')
                lista.insert(j,num)
                inserido = True
                break
        if not inserido:
            print('Adicionado ao final da lista...')
            lista.append(num)
print("=-"*30)
print(f'Os valores digitados em ordem foram {lista}')


