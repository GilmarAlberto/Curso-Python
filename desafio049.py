'''
Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.
'''

num=int(input("Digite um número que deseje ver a tabuada: "))

print(f"Tabuada do número {num}")
print('='*20)

for i in range (1,11):
    print(f"{i :2} x {num :2} = {i * num} ")