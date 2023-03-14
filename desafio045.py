import time
import random

'''
Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
'''

print('''
Suas Opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
opc = int(input('Qual a sua jogadas? '))

if opc < 0 or opc > 2:
    print('Opcão incorreta!')
else:
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!')

    opcComp=(random.randint(0,2))

    print('-='*15)
    if(opcComp == 0):
        print('Computador jogou Pedra!')
    elif(opcComp == 1):
        print('Computador jogou Papel!')
    else:
        print('Computador jogou Tesoura!')

    if (opc == 0):
        print('Jogador jogou Pedra!')
    elif (opc == 1):
        print('Jogador jogou Papel!')
    else:
        print('Jogador jogou Tesoura!')

    print('-='*15)

    if (opc == opcComp):
        print('EMPATE!')
    elif (opc == 0):
        if (opcComp==1):
            print('COMPUTADOR VENCE!')
        else:
            print('JOGADOR VENCE!')
    elif(opc ==1):
        if(opcComp == 0):
            print("JOGADOR VENCE!")
        else:
            print('COMPUTADOR VENCE!')
    else:
        if(opcComp == 0):
            print('COMPUTADOR VENCE!')
        else:
            print('Jogador VENCE!')


