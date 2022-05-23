#aproveitamento jogador. ler nome, qtd de partidas. depois qtd de gols em CADA partida
#guardar num dicionário e totalizar gols do campeonato.
#aproveitamento quer que seja lista?
quantidade = []
num = soma = 0
geral = {'Nome':'','Gols':quantidade, 'Total':''}
geral['Nome'] = str(input('Nome: ')).strip().capitalize()
partidas = int(input(f"Quantas partidas {geral['Nome']} jogou? "))
for c in range(0, partidas):
    num = int(input(f'Quantos gols na partida {c+1}? '))
    quantidade.append(num)
geral['Total'] = sum(geral['Gols'])
print('-='*30)
print(geral)
print('-='*30)
for k, v in geral.items():
    print(f'{k}: {v}.')
print('-='*30)
print(f"O jogador {geral['Nome']} jogou {partidas} partidas e fez {geral['Total']} gols no total.")
for i in range(0, partidas):
    print(f"Na partida {i+1} fez {geral['Gols'][i]} gols.")