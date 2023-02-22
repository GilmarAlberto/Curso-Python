'''
Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e
em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
salário ou então o empréstimo será negado.
'''

valor = float(input('Qual o valor do imóvel: '))
salário = float(input('Qual o valor do salário: '))
anos = float(input('Em quantos anos irá pagar: '))

prestação = valor/(anos * 12)

limite = salário *.3

if prestação > limite:
    print(f'Seu limite é {limite :.2f} e sua prestação deu {prestação :.2f} '
          f'portanto seu emprestimo foi negado!')
else:
    print(f'Seu limite é {limite :.2f} e sua prestação deu {prestação :.2f} '
          f'portanto seu emprestimo foi aprovado!')

