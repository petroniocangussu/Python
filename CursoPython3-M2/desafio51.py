#Leia o primeiro termo e a razão de uma PA, mostre os 10 primeiros termos
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = p + (10 - 1) * r
for c in range(p, d + r, r):
    print('{} '.format(c), end='->')
print('esses são os 10 primeiros termos da sua PA')