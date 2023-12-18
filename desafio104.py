'''
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
'''

def leiaInt(msg):

    while True:
        num = input(msg)

        if num.isnumeric():
            return(int(num))
        else:
            print("\033[91mErro: Digite um número inteiro válido!\033[0m")
        
def main():

    n=leiaInt("Digite um número: ")
    print(f'Você acabou de digitar o número {n}:')

if __name__ == '__main__':
    main()