'''
Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele 
quer mostrar mais alguns termos. O programa encerrará quando ele disser que 
quer mostrar 0 termos.
'''
def main():
    print('Gerador de PA')
    print('=-'*7)

    termo = int(input('Digite o Primeiro Termo: '))
    razão = int(input('Digite a razão: '))
    qtd = 0

    for i in range(0,10):
        print(termo, end=' → ')
        termo+=razão
        qtd+=1
    print('PAUSA')
    termos = 1
    while termos != 0:
        termos = int(input('Quantos termos você quer mostrar a mais? '))
        for i in range(0,termos):
            print(termo, end=' → ')
            termo+=razão
            qtd+=1
        print('PAUSA')

    print(f'Progressao finalizada com {qtd} temos mostrados')
    print('ACABOU!')

main()