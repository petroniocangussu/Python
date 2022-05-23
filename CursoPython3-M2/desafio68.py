#jogar par ou impar
from random import randint
from time import sleep
cont = 0
while True:
    jogador = str(input('Par ou impar?')).strip().lower()
    while jogador not in 'pi':
        jogador = str(input('Par ou impar?')).strip().lower()
    pc = randint(0,10)
    n = int(input('Jogarei um número entre 0 e 10, qual o seu número?'))
    som = n + pc
    sleep(1)
    if jogador[0] == 'p' and som % 2 == 0 or jogador[0] == 'i' and som % 2 == 1:
        print(f'Você ganhou, eu escolhi o número {pc}, o resultado foi {som} que é {jogador}.')
        cont += 1
    else:
        break
print(f'Eu escolhi {pc}, totalizando {som}, você perdeu. {cont} pra você, 1 pra mim.')
