"""
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
"""

frase = input('Digite uma frase: ').upper().strip()

print(f' A quantidade de A que aparece é {frase.count("A")}')
print(f' O primeiro A que aparece é na posição {frase.find("A")+1}')
print(f' O último A que aparece é na posição {frase.rfind("A")+1}')