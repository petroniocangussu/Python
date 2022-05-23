#gerar 5 números aleatórios e colocar em uma tupla
from random import randint
print('Vou gerar 5 números aleatórios para você.')
n = (randint(0, 10000), randint(0, 10000), randint(0, 10000), randint(0, 10000), randint(0, 10000))
print(f'\nEsses foram os números que gerei: {n}', end='')
print(f'\nO menor dos valores foi: {sorted(n)[0]}', end='')
print(f'\nO maior dos valores foi: {sorted(n)[-1]}', end='')