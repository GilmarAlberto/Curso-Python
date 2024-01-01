'''
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
'''

from moeda import aumentar, diminuir, dobro, metade

valor = 256.00

print(f"O valor original é R$ {valor}")

valor = aumentar(valor, 256)

print(f"O valor aumentado é R$ {valor}")

valor = diminuir(valor,128)
print(f"O valor diminuído é R$ {valor}")

valor = dobro(valor)
print(f"O dobro do valor é R$ {valor}")

valor = metade(valor)
print(f"A metade do valor é {valor}")

