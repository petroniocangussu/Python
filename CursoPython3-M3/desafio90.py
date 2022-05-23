#leia nome e média de UM aluno, guardando a situação do aluno
# guardando num dicionário. no final mostre o conteúdo da estrutura
aluno = {'Nome': '', 'Média': '', 'Situação':''}
aluno['Nome'] = str(input('Nome: ')).strip().capitalize()
aluno['Média'] = float(input('Média: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] >= 5 and aluno['Média'] <= 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-'*27)
for k, v in aluno.items():
    print(f'{k:<12} - {v:>12}')
print('Volte sempre')