#Leia o primeiro termo e a razão de uma PA, mostre os 10 primeiros termos
from time import sleep
ti = -1
print('-==-'*10)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
while ti + 1 != 10:
    pa = p + (ti + 1) * r
    print('{}'.format(pa), end='')
    print('. ' if ti + 2 == 10 else ', ', end ='')
    ti += 1
print('Esses são os 10 primeiros termos desta PA.')