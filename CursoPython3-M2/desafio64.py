#leia vários números. programa para com 999 #mostre quantos foram digitados e qual a soma (sem o 999)
c = n = som = 0
while n != 999:
    som += n
    n = int(input('A soma destes {} números é {}, digite outro número (999 para parar):'.format(c, som)))
    c += 1
print('Fim')