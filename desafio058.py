'''
Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai
"pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer.
'''

import random

numC = random.randint(0,10)



print('Sou seu Computador...')
print('Acabei de pensar num número entre 0 e 10.')
print('Será que vc consegue adivinhar qual foi?')

tentativas = 1
while True:
    numH = int(input('Qual o seu palpite?'))

    if numC == numH:
        print(f'Acertou com {tentativas} tentativas. Parabéns!')
        break
    elif numH < numC:
        print('Mais...Tente outra vez.')
    else:
        print('Menos...Tente outra vez')

    tentativas +=1


