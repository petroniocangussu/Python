for c in range(0, 6):
    print('Oi')
for c in range(0, 7, 2):
    print('Teli')
n = int(input('Digite um número: '))
for c in range (0, n+1):
    print(c)
#Início, fim, passo
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
#somatório
s = 0
for c in range(0, 5):
    m = int(input('Digite um valor: '))
    s += m
print('O somatório dos valores foi {}.'.format(s))