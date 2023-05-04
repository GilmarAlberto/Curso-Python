'''
Exercício Python 065: Crie um programa que leia vários números inteiros pelo 
teclado. No final da execução, mostre a média entre todos os valores e qual foi 
o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele 
quer ou não continuar a digitar valores.
'''
num = media = maior = menor = qtd = soma = 0

cont = 'S'

while cont.upper()=='S':
    num = int(input('Digite um número: '))
    qtd +=1
    if qtd == 1:
        menor = maior = num
    elif num < menor:
        menor = num
    elif num > maior:
        maior = num
    soma+=num
    
    cont=str(input('Quer Continuar [S/N]?'))
print(f'Você digitou {qtd} números e a média foi {soma/qtd :.2f} ')
print(f'O maior valor foi {maior} e o menor foi {menor}')
