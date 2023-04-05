'''
Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se
ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA,
O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
'''

frase = input('Digite uma frase: ').strip().upper()

frase = frase.replace(" ","") #frase sem espaços

inverso = ''

for i in range(len(frase),0,-1):

    inverso+=frase[i-1]

print(f'O inverso de {frase} é {inverso}')

if frase == inverso:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palímdromo!')

