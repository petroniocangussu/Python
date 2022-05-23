#Crie um programa que leia o nome de uma cidade e diga se começa ou não com o nome 'Santo'
cidade = str(input('Digite o nome de uma cidade: ')).strip()
print('O nome da cidade começa com a palavra "Santo"?')
print(cidade[:5].upper() == 'SANTO')