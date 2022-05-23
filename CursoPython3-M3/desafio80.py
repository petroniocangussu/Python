#usuário digita 5 valores, liste-os na posição correta de inserção (n usar sort)
#mostre lista ordenada na tela
valor = []
for c in range(0, 5):
    valor.append(int(input('Digite um número: ')))
    valor.append(int(c))
print('Os números escolhidos foram: ', end='')
for pos in range(0, len(valor)):
    if pos % 2 == 0:
        print(f'{valor[pos]}', end=', ')
print('\n')
print('-='*20)
print(f'{"Números e posições":^40}')
print('-='*20)
for pos in range(0, len(valor)):
    if pos % 2 == 0:
        print(f'\n{valor[pos]:.<30}', end = '')
    else:
        print(f'{valor[pos]:.>10}', end = '')