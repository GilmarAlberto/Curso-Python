'''
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

tupla=("Banana",
       "Arara",
       "Numero",
       "Restaurar",
       "Gilmar",
       "Alberto",
       "Abreu",
       "Pinto",
       "Cururu",
       "Caruaru")
vogais = ('a', 'e', 'i', 'o', 'u')

for i in tupla:
    print(f'Na palavra {i.upper()} temos: ',end='')
    for j in i:
        if j.lower() in vogais:
            print(j.lower(),end=' ')
    print("")