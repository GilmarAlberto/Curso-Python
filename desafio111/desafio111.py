'''
Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
'''
from utilidadescev import moeda
from utilidadescev import dado

valor = float(input("Digite um valor: "))
incr  = int(input("Digite um percentual de incremento: "))
decr  = int(input("Digite um percentual de decremento: "))

moeda.resumo(valor, incr, decr)



