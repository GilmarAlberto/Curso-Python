'''
Exercício Python 064: Crie um programa que leia vários números inteiros pelo 
teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a 
condição de parada. No final, mostre quantos números foram digitados e qual foi 
a soma entre eles (desconsiderando o flag).'''


def main():

    num = 0
    soma = 0
    qtd = 0

    while num != 999:
        num = int(input('Digite um número. [999 para parar.]: '))

        if num != 999:
            soma+=num
            qtd+=1
    print(f'Você digitou {qtd} números e a soma é {soma}.')
    

main()