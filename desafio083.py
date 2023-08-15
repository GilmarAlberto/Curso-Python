'''
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

expressao = input('Digite uma expressão: ')

pilha = []

for caractere in expressao:
    if caractere == '(':
        pilha.append(caractere)
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(caractere)
            break

if len(pilha) == 0:
    print('Expressão válida: os parênteses estão balanceados.')
else:
    print('Expressão inválida: os parênteses não estão balanceados.')