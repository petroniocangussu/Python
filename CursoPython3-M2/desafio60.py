#leia um número qualquer e mostre o seu fatorial
from math import factorial
from time import sleep
n = 1
while n != 0:
    n = int(input('Digite um número para obter o seu valor fatorial (0 para sair): '))
    print('O fatorial de {} é {}.'.format(n, factorial(n)))
    sleep(1)
print('Finalizando.')