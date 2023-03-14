'''
Exercício Python 044: Elabore um programa que calcule o valor a ser pago por
um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

opc = 0


print(f'{" Lojas GAAP " :=^40}')


compra = float(input('Preço de compra: '))

print('\nFORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

opc=int(input('Qual a opção: '))

if opc == 4:
    parc=int(input('Quantas parcelas: '))

    valorfinal=compra*1.2
    valorparc=valorfinal/parc

    print(f'Sua compra será parcelada em \033[32m{parc}x de R$ {valorparc :.2f}\033[0m COM JUROS!')
elif opc == 3:
    print(f'Você pagará \033[32m2x de R$ {compra/2 :.2f}\033[0m')
elif opc ==2:
    print(f'Você pagará \033[32m1x de R$ {compra*.95 :.2f}\033[0m')
elif opc ==1:
    print(f'Você pagará \033[32m1x de R$ {compra*.90 :.2f}\033[0m')
else:
    print('\033[041mOpção Inválida!\033[0m')