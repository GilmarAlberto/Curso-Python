'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''

from datetime import date

def voto(anoNasc):

    anoAtual = date.today().year

    idade = anoAtual - anoNasc
    
    if idade < 16:
        voto = 'NEGADO'
    elif idade < 18 or idade >= 70:
        voto = 'OPCIONAL'
    else:
        voto = 'OBRIGATÓRIO'

    return(voto)

def main():
    
    anoNasc = int(input("Digite no ano de nascimento: "))

    print(f'VOTO {voto(anoNasc)}')

if __name__ == '__main__':
    main()