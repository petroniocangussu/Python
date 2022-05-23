#Leia o peso de 5 pessoas, mostre qual o maior e o menor.
from time import sleep
s = 0
maior = 0
menor = 0
n = int(input('Quantas pessoas você deseja verificar o peso?'))
for p in range(1, n + 1):
    peso = float(input('Qual é o peso da {}ª pessoa?'.format(p)))
    s = s + peso
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O peso das {} pessoas somadas é {:.1f}Kg.'.format(n, s))
sleep(1)
print('A média de peso dessas pessoas é {:.1f}Kg.'.format(s // n))
sleep(1)
print('O maior peso lido foi {:.1f}Kg.'.format(maior))
sleep(1)
print('O menor peso lido foi {:.1f}Kg.'.format(menor))
