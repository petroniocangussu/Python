#Programa que leia número de 0 a 9999 e mostra os dígitos separados
#exemplo: 1834 - unidade 4 - dezena 3 - centena 8 - milhar 1
numero = int(input('Digite um número entre 0 e 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Milhar: {}.'.format(m))
print('Centena: {}.'.format(c))
print('Dezena: {}.'.format(d))
print('Unidade: {}.'.format(u))