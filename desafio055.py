'''
Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No
final, mostre qual foi o maior e o menor peso lidos.
'''

for i in range(5):
    peso=float(input(f'Digite o peso da {i+1}ª pessoa: '))
    if i==0:
        maior=menor=peso
    elif peso<menor:
        menor=peso
    elif peso>maior:
        maior=peso

print(f'O maior peso lido foi de {maior :.1f}Kg.')
print(f'O menor peso lido foi de {menor :.1f}Kg.')
