#leia dois valores e mostre um menu na tela
#1 somar; 2 multiplicar; 3 maior; 4 novos numeros; 5 sair do programa
from time import sleep
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
m = 0
while m != 5:
    m = int(input('''Bem vindo ao menu, o que deseja fazer com esses números?
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Verificar qual o maior
    [ 4 ] Selecionar novos números
    [ 5 ] Sair do programa
    Qual a sua opção? '''))
    if m == 1:
        print('{} + {} = {}.'.format(n1, n2, n1 + n2))
    elif m == 2:
        print('{} x {} = {}.'.format(n1, n2, n1 * n2))
    elif m == 3 and n1 > n2:
        print('{} é maior que {}.'.format(n1, n2))
    elif m == 3 and n2 > n1:
        print('{} é maior que {}.'.format(n2, n1))
    elif m == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
    elif m == 5:
        print('Finalizando...')
    else:
        print('Comando inválido, tente novamente.')
    sleep(1)
    print('=-==-'*10)
print('Fim do programa')