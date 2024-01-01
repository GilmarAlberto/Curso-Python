'''
Módulo utilizado pelo programa desafio108.py
'''
def moeda(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')

def aumentar(valor, aumento):
    return valor + aumento

def diminuir(valor, diminui):
    return valor - diminui

def dobro(valor):
    return valor * 2

def metade(valor):
    return valor/2

    