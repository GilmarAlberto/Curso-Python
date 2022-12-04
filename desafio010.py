#Crie um programa que leia quanto dinheiro uma pessoa tem na
#carteira e mostre quanto dólares ela pode comprar.
#Considere: US$ 1,00 = R$ 3,27

num=float(input("quanto de dinheiro você tem na carteira? R$ "))

print(f'Com R$ {num} você pode comprar US$ {num/3.27 :.2f} ')
