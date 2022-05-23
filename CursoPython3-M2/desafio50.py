#leia 6 números, some os pares
s = 0
co = 0
for c in range(0, 6):
    m = int(input('Digite um número:'))
    if m % 2 == 0:
        s = s + m
    if m % 2 == 1:
        co = co + 1
print('O somatório dos números pares é {}.'.format(s))
print('{} numeros impares não foram considerados.'.format(co))