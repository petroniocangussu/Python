#leia um número inteiro, diga se é primo
n = int(input('Digite um número inteiro: '))
m = str(n)
if n == 2 or n == 3 or n == 5 or n == 7:
    print('{} é um número primo.'.format(n))
elif n % 2 == 0 or n % 3 == 0 or n % 7 == 0:
    print('{} não é um número primo.'.format(n))
    if m[-1:] == 0 or m[-1:] == 5:
        print('Números com final "0" ou "5" nunca são primos.'.format(n))
else:
    print('{} é um numero primo.'.format(n))