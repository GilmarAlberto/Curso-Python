'''
Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma
pessoa, calcule seu Índice de Massa Corporal (IMC (peso/(altura²))) e mostre
seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

peso = float(input('Digite o peso de uma pessoa: '))
altura = float(input('Digite a altura de uma pessoa: '))

imc=peso/(altura*altura)

if imc < 18.5:
    status='Abaixo do Peso'
elif imc < 25:
    status = 'Peso Ideal'
elif imc < 30:
    status = 'Sobrepeso'
elif imc < 40:
    status = 'Obesidade'
else:
    status = 'Obesidade Mórbida'

print(f'Seu imc é \033[32m{imc :.1f}\033[0m portanto seu status é \033[32m{status}\033[0m.')