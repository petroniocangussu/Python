#soma entre números impares, múltiplos de 3, entre 1 e 500
#Impares
soma = 0
cont = 0
for imp in range(1, 501, 2):
    if imp % 3 == 0:
        soma = soma + imp
        cont = cont + 1
print('A soma dos valores é {}.'.format(soma))
print('A quantidade de números é {}.'.format(cont))