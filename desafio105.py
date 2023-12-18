'''
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''

def notas(*notas, sit = False):
    """
    Função para calcular estatísticas das notas dos alunos.

    Parâmetros:
    *notas: Notas dos alunos.
    sit (bool): Se True, inclui a situação do aluno (Aprovado ou Reprovado).

    Retorna:
    dict: Dicionário com as estatísticas das notas.
    """
    
    qtdNotas = len(notas)
    maior = max(notas)
    menor = min(notas)
    media = sum(notas)/qtdNotas

    if sit:
        msg = "Aprovado" if media >= 7 else "Reprovado"


    dict = {"Qtd Notas": len(notas),"Maior Nota": max(notas),"Menor Nota": min(notas), "Media": media}

    if sit:
        dict["Situação"] = msg

    return dict

def main():

    dict = notas(5, 6, 7, 8, 9, 10, sit = True)

    print(dict)

    dict = notas(6, 7.5, 8.5, 9.5, 10)

    print(dict)

if __name__ == "__main__":
    main()