def main():
    print('='*22)
    print('Sequência de Fibonacci')
    print('='*22)
    qtd = 0
    while qtd <= 0:
        qtd = int(input('Quantos termos você quer mostrar? '))

    print(f'{0} → ',end='')
    num = 1
    ant = 0
    atu = 1
    while num <= qtd:

        print(atu,end=' → ')
        aux = ant
        ant=atu   
        atu+=aux
        num+=1
    print('FIM')


        



main()