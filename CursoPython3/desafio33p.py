#leia três números e mostre qual o maior e o menor.
a = int(input('Digite um número: '))
b = int(input('Digite um número diferente: '))
c = int(input('Digite um número diferente dos demais: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor é \033[31m{}\033[m'.format(menor))
print('O maior valor é \033[32m{}\033[m'.format(maior))