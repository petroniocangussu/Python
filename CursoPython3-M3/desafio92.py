#nome, ano, CTPS, cadastre-os com a idade. Se CTPS!=0, dicionário deve receber
#ano de contratação. Calcule e acrescente com quantos anos vai se aposentar.
from datetime import date
geral = {'Nome':'','Idade':'','CTPS':''}
geral['Nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
geral['Idade'] = date.today().year-ano
geral['CTPS'] = int(input('CTPS (0 não tem): '))
if geral['CTPS'] != 0:
    geral['Contratação'] = int(input('Ano de contratação: '))
    geral['Aposentadoria'] = (geral['Contratação'] + 35) - ano
    geral['Salário'] = int(input('Salário: R$'))
else:
    geral['CTPS'] = str('Você não possui trabalho.')
for k, v in geral.items():
    print(f'{k} tem valor {v}')