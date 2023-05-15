'''
Exercício Python 067: Faça um programa que mostre a tabuada de vários números, 
um de cada vez, para cada valor digitado pelo usuário. O programa será 
interrompido quando o número solicitado for negativo. 
'''
while True:
    
    num = int(input('Quer ver a tabuada de qual número? '))
    
    if num < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    print('-'*34)
    for qtd in range(1,11):
        print (f'{num} x {qtd} = {num*qtd}')
    print('-'*34)
