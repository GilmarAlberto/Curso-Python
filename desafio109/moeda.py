'''
Módulo utilizado pelo programa desafio109.py
'''
def moeda(valor, formata = True):

    if formata:
        return f'R$ {valor:.2f}'.replace('.', ',')
    else:
        return valor

def aumentar(valor, aumento):
    return valor + aumento

def diminuir(valor, diminui):
    return valor - diminui

def dobro(valor):
    return valor * 2

def metade(valor):
    return valor/2

    