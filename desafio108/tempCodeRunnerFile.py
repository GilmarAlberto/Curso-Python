'''
Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
'''

from moeda import aumentar, diminuir, dobro, metade, moeda

valor = 256.00

print(f"O valor original é {moeda(valor)}")

valor_aumentado = aumentar(valor, 256)
print(f"O valor aumentado é {moeda(valor_aumentado)}")

valor_diminuido = diminuir(valor, 128)
print(f"O valor diminuído é {moeda(valor_diminuido)}")

valor_dobro = dobro(valor)
print(f"O dobro do valor é {moeda(valor_dobro)}")

valor_metade = metade(valor)
print(f"A metade do valor é {moeda(valor_metade)}")