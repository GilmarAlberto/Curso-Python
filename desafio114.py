'''
Exercício Python 114: Crie um código em Python que teste se o site pudim (este site não está mais no ar!) está acessível pelo computador usado.
Para testar o acesso vamos utilizar o www.uol.com.br
'''
from urllib import request, error

url = 'http://www.uol.com.br'

try:
    response = request.urlopen(url)
    # Verifica se o código de status é 200 (OK)
    if response.getcode() == 200:
        print(f'O site {url} está acessível.')
    else:
        print(f'O site {url} retornou um código de status {response.getcode()}.')
except error.URLError as e:
    print(f'Não foi possível conectar ao site {url}. Erro: {e.reason}')
except Exception as e:
    print(f'Ocorreu um erro inesperado: {e}')
else:
    print('Tudo ok!')