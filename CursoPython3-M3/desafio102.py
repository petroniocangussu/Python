#Função fatorial, dois parâmetros: o número a calcular e o 'show' que será
#opcional indicando se será mostrado ou não na tela o processo de cálculo.
def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    print(f'O fatorial de {num} é {f}')
    show = str(input('Deseja mostrar a multiplicação? [S/N]')).strip().upper()[0]
    if show == 'S':
        for c in range(num, 0, -1):
            if c > 1:
                print(f'{c}', end=' x ')
            else:
                print(f'{c}', end=' = ')
        print(f)
    else:
        print('Fim!')
    help = str(input('Deseja ajuda? [S/N]')).strip().upper()[0]
    if help == 'S':
        help(fatorial)
    else:
        print('Fim do programa.')
#Programa Principal
num = int(input('Qual o número que deseja ver o fatorial? '))
fatorial(num)
