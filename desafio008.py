# Escreva um programa que leia um valor em metros e o exiba
# convertido em centímetros e milímetros.

num = float(input('Digite um valor em metros: '))

print(f'{num} metros equivalem a:')
print(f'{num/1000} km')
print(f'{num/100} hm')
print(f'{num/10} dam')
print(f'{num*10} dm')
print(f'{num*100} cm')
print(f'{num*1000} mm')

