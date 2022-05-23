#função notas(), pode receber várias notas de alunos e retornar um dicionário.
#qnt de notas. maior e menor. média turma. situação (opcional)
def notas(*n, sit=False):
    """
    Função para notas e situação de uma turma.
    n: Notas a adicionar (aceita várias).
    sit: situação do aluno (se deve adicionar ou não), Default:False
    Return: Dicionário com todas as informações.
    """
    dic = {}
    dic['Total'] = len(n)
    dic['Maior'] = max(n)
    dic['Menor'] = min(n)
    dic['Média'] = sum(n) / len(n)
    if sit:
        if dic['Média'] >= 7:
            dic['Situação'] = 'Boa'
        elif 5 <= dic['Média'] < 7:
            dic['Situação'] = 'Média'
        else:
            dic['Situação'] = 'Ruim'
    return dic
#Programa principal
resp = notas(5.5, 0.5, 6.5, 7.5, sit=True)
print(resp)
help(notas)