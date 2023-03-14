'''
Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o
recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo  número: '))
n3 = int(input('Digite o terceiro número: '))


if n1+n2 > n3 and n1+n3 > n2 and n2+n3 > n1:
    if n1 == n2 and n2 == n3:
        print('Triangulo Equilátero!')
    elif (n1 == n2 and n2 != n3) or (n1 == n3 and n2!=n3):
        print('Triângulo Isósceles!')
    else:
        print('Triângulo Escaleno!')
else:
    print('Não é um triângulo!')
