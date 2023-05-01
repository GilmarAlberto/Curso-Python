'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

from time import sleep

opc = 0

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

while opc != 5:

    print(f'{" MENU " :=^40}')


    print('''
            [ 1 ] somar
            [ 2 ] multiplicar
            [ 3 ] maior
            [ 4 ] novos números
            [ 5 ] sair do programa
    ''')
    opc = int(input('Escolha a opcao: '))

    if opc == 1:
        print(f'A soma de {num1} + {num2} é {num1 + num2}')
    elif opc == 2:
        print(f'A multicação de {num1} * {num2} é {num1 * num2}')
    elif opc == 3:
        if num1 > num2:
            print(f'O maior número é {num1}')
        elif num2 > num1:
            print(f'O maior número é {num2} ')
        else:
            print('Os números são iguais!')
    elif opc == 4:
            print('Digite novos números!')

            num1 = int(input('Digite o primeiro número: '))
            num2 = int(input('Digite o segundo número: '))

    elif opc == 5:
        print('Finalizando...')
    else:
        print('Opcao Incorreta!')

    sleep(2)

    print('Fim do Programa! Volte Sempre!5')

