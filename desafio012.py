# Faça um algoritmo que leia o preço de um produto e mostre seu
# novo preço com 5% de desconto

preco = float(input('Digite o preço do produto: R$ '))

print(f'O preço do produto com desconto de 5% é R$ {preco * .95 :.2f}')