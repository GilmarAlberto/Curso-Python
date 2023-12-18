'''
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''

def ficha(nome = "<desconhecido>", gols = 0):

    if type(nome) is not str:
        nome = "<desconhecido>"

    if type(gols) not in (int, float):
        gols = 0

    print(f'O jogador {nome} fez {gols} gols.')

def main():

    print("Sem parâmetros")
    ficha()

    print("passando somente o nome")
    ficha("Gilmar")

    print("passando somente gols")
    ficha(gols=3)

    print("passando nome e gols")
    ficha("Gilmar", 3)

    print("passando parâmetro errado")
    ficha("Gilmar", "três")

    print("Passando parâmetro errado II")
    ficha(0, "Gilmar")

if __name__ == '__main__':
    main()