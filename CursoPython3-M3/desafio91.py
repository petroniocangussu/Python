#4 jogador joguem um dado, guarde-os num dicionário. Coloque-os em ordem.
#Diga o vencedor
from random import randint
from time import sleep
from operator import itemgetter
geral = []
geral2 = {'jogador1': randint(1,6), 'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4': randint(1,6)}
print('Valores sorteados:')
for k, v in geral2.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
ranking = list()
ranking = sorted(geral2.items(), key=itemgetter(1), reverse=True)
print (ranking)
for i, v in enumerate(ranking):
    print(f'{i+1}°: {v[0]} com {v[1]}.')
    sleep(0.5)
"""for c in range(0,4):
    jogador = {'Nome':'','Dado':''}
    jogador['Nome'] = str(input('Nome:')).strip().capitalize()
    jogador['Dado'] = randint(1,6)
    geral.append(jogador.copy())
#    geral2.copy(jogador.copy())
for d in range(0,4):
    print(f'O jogador {geral[d]["Nome"]} rolou {geral[d]["Dado"]} no dado.')
    sleep(0.5)
for e in range(0,4):
    print(f'{e+1}° lugar: {geral[e]["Nome"]} com {geral[e]["Dado"]}')"""