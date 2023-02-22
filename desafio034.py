'''
 Escreva um programa que pergunte o salário de um funcionário e calcule o valor
 do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de
 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''

sal = float(input('Digite o salário: '))

if sal > 1250:
    print(f'O novo salário, com aumento de 10%, é {sal*1.10 :.2f}')
else:
    print(f'O novo salário, com aumento de 15%, é {sal*1.15 :.2f}')

