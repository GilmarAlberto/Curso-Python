# Faça um programa que leia a largura e a altura de uma parede
# em metro, calcule a sua área e a quantidade de tinta necessaria
# para pinto-la, sabendo que cada litro de tinta pinta uma área
# de 2m²

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
m2 = largura*altura

print(f'Sua parede tem dimenção de {largura} x {altura} e sua área é de {m2 :.2f}m².')
print(f'Para pintar essa parede você precisará de {m2/2 :.2f} litros de tinta.')
