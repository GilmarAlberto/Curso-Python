'''
Exercício Python 069: Crie um programa que leia a idade e o sexo de várias 
pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário 
quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
'''


while True:

    idade = qtd18 = qtdh = qtdm = 0
    sexo = continua = " "

    print('-'*30)
    print('CADASTRE UMA PESSOA'.center(30))
    print('-'*30)

    idade = int(input('Idade: '))

    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]

    if idade >= 18:
        qtd18 += 1
    if sexo == 'M':
        qtdh += 1
    if sexo == 'F' and idade < 20:
        qtdm += 1

    while continua not in 'SN':
        continua = input('Quer continuar [S/N]').strip().upper()[0]

    if continua == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {qtd18}')
print(f'Ao todo temos {qtdh} homens cadastrados')
print(f'E temos {qtdm} mulher com menos de 20 anos')


