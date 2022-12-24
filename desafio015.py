"""
Escreva um programa que pergunte a quantidade de Km percorridos por
um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
R$0,15 por Km rodado.
"""

kmP = float(input("Digite a quantidade de Km percorridos: "))
dias = int(input("Digite a quantidade de dias pelos quais foi alugado: "))

aPagar = (60 * dias) + (0.15 * kmP)

print(f'O Total a Pagar é: R$ {aPagar : .2f}')