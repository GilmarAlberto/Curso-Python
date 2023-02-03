nome = input("Qual é o seu nome? ")

print(f"Prazer em te conhecer {nome :>20}!")
print(f"Prazer em te conhecer {nome :*^20}!")

n1 = int(input("Entre com um valor: "))
n2 = int(input("Entre com outro valor: "))

print(f'Soma: {n1+n2}')
print(f'Produto: {n1*n2}')
print(f'Divisão: {n1/n2 : .3f}')
print(f'Divisão Inteira: {n1//n2}')
print(f'Potência: {n1**n2}')
