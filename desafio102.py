"""
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

def fatorial(num, show=False):
    """
    ==> Calcula o Fatorial de um número
    :param num: O numero a ser calculado
    :param show (opcional): Mostra ou não a conta
    :return: O valor fatorial de um número n
    """

    fat = 1
    print("-"*30)
    while num >= 1:
        fat *= num
        if show:
            print(f'{num}',end="")
            if num > 1:
                print(" x ", end = "")
        num -=1
    if show:
        print(" = ", end="")
    return(fat)
    
                
def main():
    
    print("Calculando fatorial com show=True:")
    print(fatorial(5, True))

    print("\nCalculando fatorial com show=False:")
    print(fatorial(5, False))

    print("\nCalculando fatorial sem especificar show (default é False):")
    print(fatorial(6))

    help(fatorial)

if __name__ == '__main__':
    main()