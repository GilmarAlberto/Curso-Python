from math import sqrt

'''
 Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
 de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''

catop = float(input("Digite o Cateto Oposto: "))
catad = float(input("Digite o Cateto Adjacente: "))
hip = sqrt((catop*catop)+(catad*catad))

print(f'O valor da hipotenusa é {hip : .2f}')