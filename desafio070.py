'''
Exercício Python 070: Crie um programa que leia o nome e o preço de vários 
produtos. O programa deverá perguntar se o usuário vai continuar ou não. 
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 
'''

maisbarato = ""
vlrmaisbarato = 0
totalgasto = 0
qtdmaior1000 = 0

print('*'*19)
print('LOJA DO GILMARZÃO'.center(20))
print('*'*19)


while True:
    produto = ""
    preco = 0.0
    continua = " "

    while produto == "":
        produto = str(input('Nome do produto: ')).strip()

    while preco == 0:
        preco = float(input('Preço: R$ '))

    if totalgasto == 0 or preco < vlrmaisbarato:
        maisbarato = produto
        vlrmaisbarato = preco
    elif preco > 1000:
        qtdmaior1000 += 1

    totalgasto += preco

    while continua not in ('SN'):

        continua = str(input('Continua? [S/N]')).strip().upper()[0]

    if continua == 'N':
    
        break

print(f'{" Fim do programa " :*^30}')
print(f'O total da compra foi {totalgasto} ')
print(f'Temos {qtdmaior1000} produtos custando mais do que R$ 1000,00')
print(f'O produto mais barato foi {maisbarato} que custou {vlrmaisbarato}')

