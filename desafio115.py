from time import sleep
import sys

arq = 'cursoemvideo.txt'

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
    while (True):
        try:
            num = int(input(msg))
        except(ValueError, TypeError):
            print('Erro: por favor, digite um número inteiro válido!')
            continue
        except(KeyboardInterrupt):
            print('\nSistema interrompido pelo usuário.')
            sys.exit()
        else:
            return (num)


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo!")
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("ERRO ao ler o arquivo!")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a=open(arq, 'at')
    except:
        print("Houve um erro na abertura do arquivo!")
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()


if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])

    if resposta == 1:
        ler_arquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema...Até Logo...')
        break
    else:
        cabecalho('Erro: Digite uma opção válida!')
    
    sleep(2)





