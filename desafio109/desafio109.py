'''
Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''

from moeda import aumentar, diminuir, dobro, metade, moeda

valor = 256.00

print(f"O valor original é {moeda(valor, True)}")

valor_aumentado = aumentar(valor, 256)
print(f"O valor aumentado é {moeda(valor_aumentado, False)}")

valor_diminuido = diminuir(valor, 128)
print(f"O valor diminuído é {moeda(valor_diminuido, True)}")

valor_dobro = dobro(valor)
print(f"O dobro do valor é {moeda(valor_dobro, False)}")

valor_metade = metade(valor)
print(f"A metade do valor é {moeda(valor_metade, True)}")