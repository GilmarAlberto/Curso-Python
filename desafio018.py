'''
   Faça um programa que leia um ângulo qualquer e mostre na tela o
valor do seno, cosseno e tangente desse ângulo.
'''

import math

angulo = float(input("Digite um ângulo: "))

print(f'O seno de {angulo} é {math.sin(math.radians(angulo)) :.2f}')
print(f'o cosseno de {angulo} é {math.cos(math.radians(angulo)) :.2f}')
print(f'A tangente de {angulo} é {math.tan(math.radians(angulo)) :.2f}')


