import sys

def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1

    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())

    opc = leiaInt('Sua opção: ')

    return opc

def leiaInt(msg):
   
   while(True):
        try:
           num = int(input(msg))
        except(ValueError,TypeError):
            print('Erro: por favor, digite um número inteiro válido!')
            continue
        except(KeyboardInterrupt):
            print('\nSistema interrompido pelo usuário.')
            sys.exit()
        else:
            return(num)
