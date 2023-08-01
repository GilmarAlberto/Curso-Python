'''
Exercício Python 072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
numeros_por_extenso = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte"
)

num = int(input('Digite um número entre 0 e 20: '))

while num > 20:
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Voce digitou o número {numeros_por_extenso[num]}')