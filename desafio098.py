'''
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''

import time

def contador(num1, num2, passo):
    temp = passo
    temp *= -1 if passo < 1 else 1
    
    print('-='*30)
    print(f'Contagem de {num1} ate {num2} de {temp} em {temp}')

    if num2 < num1 and passo > 0:
        passo *= -1

    for i in range(num1, num2, passo):
        print(i,end=' ')
        time.sleep(1)
    print('Fim!')

def main():

    # a) de 1 até 10, de 1 em 1
    contador(1,10,1)

    # b) de 10 até 0, de 2 em 2
    contador(10, 0, 2)

    # c) uma contagem personalizada
    print('-='*30)
    print('Agora é a sua vez de personalizar a contagem.')

    num1 = int(input('Início: '))
    num2 = int(input('Fim: '))
    passo = int(input('Passo: '))

    contador(num1, num2, passo)

if __name__ == '__main__':
    main()