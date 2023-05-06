""" Faça um programa que leia algo pelo teclado
        e mostre na tela o seu tipo primitivo
        e todas as informações possíveis sobre ele
"""

str = input("Digite algo: ")

print(type(str))

print(f"É alfanumérico  (isalnum)      : {str.isalnum()}")
print(f"É alfabético    (isalpha)      : {str.isalpha()}")
print(f"É ascII         (isascii)      : {str.isascii()}")
print(f"É tudo dígito   (isdigit)      : {str.isdigit()}")
print(f"É tudo espaço   (isspace)      : {str.isspace()}")
print(f"É tudo número   (isdecimal)    : {str.isdecimal()}")
print(f"É identificador (is identifier): {str.isidentifier()}")
print(f"É caixa baixa   (islower)      : {str.islower()}")
print(f"É numérico      (isnumeric)    : {str.isnumeric()}")
print(f"É imprimível    (isprintable)  : {str.isprintable()}")
print(f"É titulado      (istitle)      : {str.istitle()}")
print(f"É caixa alta    (isupper)      : {str.isupper()}")
