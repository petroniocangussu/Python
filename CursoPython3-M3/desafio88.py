#ajude o jogador da megasena a criar palpites. Perguntar quantos jogos gerar
#e sortear 6 números entre 1 e 60 por jogo, cadastrando em uma lista composta.
from random import randint
from time import sleep
print('=-'*30)
n = int(input('Olá, quantos bilhetes você quer que eu preencha para você? '))
megasena = []
todos = list()
sleep(0.7)
print(f'Tudo bem, preencherei {n} bilhetes para você')
sleep(0.7)
for c in range (1, n+1):
    while True:
        num = randint(1,60)
        if num not in megasena:
            megasena.append(num)
        if len(megasena) == 6:
            break
    megasena.sort()
    todos.append(megasena[:])
    print(f'Jogo {c}: {megasena}')
    megasena.clear()
    sleep(0.7)
print(f'{"Boa sorte":^40}')
print('=-'*30)
"""print('-=' * 3, f' Sorteando {n} jogos:')
for i, l in enumerate(todos):
    print(f'Jogo {i+1}: {l}')"""