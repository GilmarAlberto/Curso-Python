'''
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
def maior(*num):

    qtd = len(num)

    maior = 0 if qtd <= 0 else max(num)
    
    print('-='*30)
    print('Analisando os valores passados')

    for x in num:
        print(x, end=' ')

    print(f'Foram informados {qtd} valores ao todo')
    print(f'O maior número é {maior}')
    
def main():

    maior(2, 9, 4, 5, 7, 1)
    maior(4, 7, 0)
    maior(1, 2)
    maior(6)
    maior()
    maior(10,9,8,7,6,5,4,3,2,1)

if __name__ == '__main__':
    main()