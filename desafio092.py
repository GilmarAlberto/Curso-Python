'''
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import datetime

ano_corrente = datetime.now().year

cadastro = {}

cadastro['nome'] = input('Nome: ')
nasc = int(input('Ano de Nascimento: '))
cadastro['idade'] = ano_corrente - nasc
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = (cadastro['contratação']-nasc)+30

print("=-"*30)

for k,v in cadastro.items():
    print(f'{k} tem o valor {v} ')






