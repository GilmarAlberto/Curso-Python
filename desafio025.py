"""
    Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
"""

nome = input('Digite um nome: ').strip()

nome = nome.upper()
print(f'Seu nome tem Silva? {"SILVA" in nome}')