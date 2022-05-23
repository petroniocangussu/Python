#leia quatro valores inteiros e os coloque em uma tupla, mostre: quantas vezes apareceu o 9, qual a posição do 3, quais foram números pares.
num = (int(input('Digite um número: ')), int(input('Digite outro: ')),
       int(input('Digite outro: ')), int(input('Digite outro: ')))
print(num)
print(f'O número 9 foi escolhido {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1} posição.')
else:
    print('O número 3 não foi escolhido.')
print('Os valores pares digitados foram:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')