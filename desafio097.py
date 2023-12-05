'''
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex: 
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~
'''

def escreva(texto):
    largura = len(texto)

    print('~'*(largura+2))
    print(f'{texto:^{largura+2}}')
    print('~'*(largura+2))

def main():

    texto = input("Digite um texto: ")

    escreva(texto)

if __name__ == "__main__":
    main()
