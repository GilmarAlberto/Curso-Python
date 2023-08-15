'''
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
'''

lista = []
num = 0
opc = "S"

while opc.upper() == "S":
    num=int(input('Digite um valor: '))

    if num in lista:
        print('Valor duplicado não vou adicionar')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    
    opc = input('Deseja continuar? S/N: ')

lista.sort()
print('=-'*30)

print(f'Você digitou os valores {lista}')