def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')
if par(n):
    print('É par!')
else:
    print('Não é par!')