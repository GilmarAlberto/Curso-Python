'''
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''
import random
import time

def sorteia(lista):

    print("Sorteando 5 valores da lista: ", end='')
    for i in range(5):
        num = random.randint(1,10)
        print(f'{num}',end=' ')
        lista.append(num)
        time.sleep(1)
    print('PRONTO!')
        
    

def somaPar(lista):
    soma = 0 
    for i in lista:
        if i%2 == 0:
            soma += i
    print(f'Somando os números pares de {lista}, temos {soma}')

def main():

    lista = []

    sorteia(lista)
    somaPar(lista)

if __name__ == '__main__':
    main()