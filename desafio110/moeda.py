'''
Módulo utilizado pelo programa desafio110.py
'''

def resumo(valor, incr, decr):

    print(f"O valor original é {moeda(valor, True)}")

    valor_aumentado = aumentar(valor, incr)
    print(f"O valor aumentado é {moeda(valor_aumentado, False)}")

    valor_diminuido = diminuir(valor, decr)
    print(f"O valor diminuído é {moeda(valor_diminuido, True)}")

    valor_dobro = dobro(valor)
    print(f"O dobro do valor é {moeda(valor_dobro, False)}")

    valor_metade = metade(valor)
    print(f"A metade do valor é {moeda(valor_metade, True)}")

def moeda(valor, formata = True):

    if formata:
        return f'R$ {valor:.2f}'.replace('.', ',')
    else:
        return valor

def aumentar(valor, aumento):
    return valor * ((100+aumento)/100)

def diminuir(valor, diminui):
    return valor * ((100-diminui)/100)

def dobro(valor):
    return valor * 2

def metade(valor):
    return valor/2

    