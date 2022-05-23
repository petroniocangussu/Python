#Leia dois números inteiros e compare-os (maior, menor ou igual)
n = int(input('Digite um número inteiro: '))
d = int(input('Digite outro número inteiro: '))
if n > d:
    print('{} é maior que {}.'.format(n, d))
if d > n:
    print('{} é maior que {}.'.format(d, n))
if d == n:
    print('Não existe valor maior, {} e {} são iguais.'.format(n, d))