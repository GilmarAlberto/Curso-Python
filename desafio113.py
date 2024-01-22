'''
Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''

import sys

def leiaInt(msg):
   
   while(True):
        try:
           num = int(input(msg))
        except(ValueError,TypeError):
            print('Erro: por favor, digite um número inteiro válido!')
            continue
        except(KeyboardInterrupt):
            print('\nSistema interrompido pelo usuário.')
            sys.exit()
        else:
            return(num)
        
def leiaFloat(msg):
   
   while(True):
        try:
           num = float(input(msg))
        except(ValueError,TypeError):
            print('Erro: por favor, digite um número real válido!')
            continue
        except(KeyboardInterrupt):
            print('\nSistema interrompido pelo usuário.')
            sys.exit()
        else:
            return(num)


        
def main():

    numInt   = leiaInt("Digite um número inteiro: ")
    numFloat = leiaFloat("Digite um número real: ")
    
    print(f'Você acabou de digitar o número inteiro {numInt} e o número real {numFloat}.')

if __name__ == '__main__':
    main()