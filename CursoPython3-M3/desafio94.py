#nome, sexo e idade de várias pessoas, guardando-as em um dic. Todos os dic em uma lista. mostre:
#Quantas, média de idade, lista com mulheres, lista com as pessoas com idade acima da média.
pessoa = {'Nome':'','Idade':'','Sexo':''}
geral = []
soma = média = 0
while True:
    pessoa['Nome'] = str(input('Nome:')).strip().capitalize()
    pessoa['Idade'] = int(input('Idade: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    soma += pessoa['Idade']
    geral.append(pessoa.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if continuar == 'N':
        break
print('-='*30)
print(f'Foram registradas {len(geral)} pessoas, a média de idade é de {soma / len(geral):.2f} anos.')
print(f'Mulheres registradas:')
for p in geral:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]}, ', end='')
print('\nLista de pessoas que estão acima da média: ')
for i in range(0,len(geral)):
    if geral[i]['Idade'] >= soma / len(geral):
        print(geral[i])
print('Encerrado')