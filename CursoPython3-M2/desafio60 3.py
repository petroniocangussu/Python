#Fatorial utilizando for
n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
for c in range(n,0,-1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))