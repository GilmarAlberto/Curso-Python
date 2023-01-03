"""
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
"""
cidade = input("Digite uma cidade: ")

cidade = cidade.upper().strip()

print(cidade[0:5])

print('SANTO' in cidade[0:5])