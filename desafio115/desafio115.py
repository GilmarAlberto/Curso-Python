from lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])

    if resposta == 1:
        cabecalho('opcao 1')
    elif resposta == 2:
        cabecalho('opcao 2')
    elif resposta == 3:
        cabecalho('Saindo do Sistema...Até Logo...')
        break
    else:
        cabecalho('Erro: Digite uma opção válida!')
    
    sleep(2)



