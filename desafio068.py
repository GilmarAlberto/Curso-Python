'''
Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de 
vitórias consecutivas que ele conquistou no final do jogo. 
'''
from random import randint

print('=-'*26)
print('VAMOS JOGAR PAR OU IMPAR!')
print('=-'*26)

qtd = qtdV = 0

while True:
    num = int(input('Digite um valor: '))

    numC= randint(1,9)

    while esc not in 'PI':
        esc = input('Par ou Impar?').upper()

    soma = num+numC

    if soma%2 == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'

    print('-'*26)
    print(f'Você jogou {num} e o computador {numC}. Total de {soma} DEU {result}!')
    print('-'*26)

    if (soma%2==0 and esc =='P') or (soma%2!=0 and esc=='I'):
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-'*26)
        qtdV += 1
    else: 
        print('Você PERDEU!')
        print('=-'*26)
        print(f'GAME OVER! Você venceu {qtdV} vezes!')
        break

        
