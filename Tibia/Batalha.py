from random import randint
from time import sleep
#knight
knight = {}
knight['level'] = int(input('Escolha um level para o seu knight: '))
knight['skill'] = int(input('Defina um skill para o seu knight: '))
knight['hp'] = 150 + (knight['level'] * 15)
knight['arma'] = int(input('Ataque da arma: '))
dano = 0.085 * knight['arma'] * knight['skill']
knight['dano'] = round(dano)
cont = 0
print(knight)
#criatura
ataquesmin = []
ataquesmáx = []
criatura = {'nome':'','hp':'','ataquesmin':ataquesmin,'ataquesmáx':ataquesmáx}
criatura['nome'] = str(input('Qual criatura está enfrentando?')).strip().capitalize()
criatura['hp'] = int(input('Qual o life dessa criatura?'))
quantidade = int(input('Quantos ataques deseja adicionar à criatura: '))
for c in range (0, quantidade):
    ataquemin = int(input(f'Dano mínimo do ataque {c+1}°: '))
    ataquesmin.append(ataquemin)
    ataquemáx = int(input(f'Dano máximo do ataque {c+1}°: '))
    ataquesmáx.append(ataquemáx)
print(criatura)
#batalha
print('A grande batalha começa')
print(f"O knight começa atacando o {criatura['nome']}.")
while True:
    cont += 1
    print(f'-=-=-=-=-=-=-=-= Turno {cont} -=-=-=-=-=-=-=-=')
    print(f'Knight = {knight["hp"]} x {criatura["hp"]} = {criatura["nome"]}')
    knight['ataque'] = randint(0,knight['dano'])
    sleep(1.5)
    print(f"Knight ataca: {knight['ataque']}.\n{criatura['nome']} possui {criatura['hp'] - knight['ataque']}HP restante.")
    criatura['hp'] = criatura['hp'] - knight['ataque']
    if criatura['hp'] <= 0:
        print(f'O {criatura["nome"]} foi derrotado')
        break
    for n in range (0, quantidade):
        sleep(1.5)
        criatura[f'ataque{n}'] = randint(criatura['ataquesmin'][n], criatura['ataquesmáx'][n])
        print(f"{criatura['nome']} ataca: {criatura[f'ataque{n}']}.\nKnight possui {knight['hp'] - criatura[f'ataque{n}']}HP restante.")
        knight['hp'] = knight['hp'] - criatura[f'ataque{n}']
    if knight['hp'] <= 0:
        print('O knight foi derrotado.')
        break
print('A grande batalha acabou.')