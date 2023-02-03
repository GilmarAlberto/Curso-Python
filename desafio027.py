"""
Primeiro e último nome de uma pessoa
"""

nome = input('Digite um nome completo: ')

pos = nome.find(' ')
pos1= nome.rfind(' ')+1
print(f'primeiro e último nome: {nome[0:pos]} {nome[pos1:]}')




