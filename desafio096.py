'''
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

def area(largura, comprimento):
    return largura * comprimento
    

def main():

    largura = float(input("Digite a largura do terreno: "))
    comprimento = float(input("Digite o comprimento do terreno: "))

    print(f'A area do terreno é {area(largura, comprimento)} m2')

if __name__ == "__main__":
    main()
