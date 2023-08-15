'''
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

lista = []; par = []; impar = []
num = 0
opc = "S"

while opc.upper() == "S":
    num=int(input('Digite um valor: '))

    lista.append(num)
       
    opc = input('Deseja continuar? S/N: ')

for i in lista:
    if i%2 == 0:
        par.append(i)
    else:
        impar.append(i)

print("=-"*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')

