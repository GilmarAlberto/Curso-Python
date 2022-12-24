"""
Escreva um programa que converta uma temperatura digitando em graus
Celsius e converta para graus Fahrenheit.

F = C x 1,8 + 32

"""

graus = float(input('Informe a temperadura em °C: '))

far = graus * 1.8 + 32

print(f'A temperadura de {graus}°C equivale a {far :.1f}°F.')

