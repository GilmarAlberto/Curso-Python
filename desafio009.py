# Faça um programa que leia um número inteiro qualquer e mostre
# na tela a a sua tabuada.

num=int(input("Digite um número que deseje ver a tabuada: "))

print(f"Tabuada do número {num}")
print('='*20)

for i in range (1,11):
    print(f"{i :2} x {num :2} = {i * num} ")



