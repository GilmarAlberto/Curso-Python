"""Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome."""

nome = input('Digite um nome completo: ')

print(nome)
print(nome.upper())
print(nome.lower())
espaco=(nome.count(' '))

print(espaco)

print(f'Quantidade de letras: {len(nome) - espaco}')

print(f'O primeiro nome tem {nome.find(" ")} letras')


