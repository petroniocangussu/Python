#leia uma frase, diga se é um palíndromo, desconsiderando os espaços
n = str(input('Digite uma frase: ')).strip().lower()
p = n.split()
j = ''.join(p)
i = ''
for l in range(len(j) - 1, -1, -1):
    i += j[l]
print('O inverso de {} é {}.'.format(j, i))
if i == j:
    print('{} é um palíndromo.'.format(n))
else:
    print('{} não é um palíndromo.'.format(n))
#outra solucão = i == j[::-1]
"""frase = input("Qual a frase? ").upper().replace(" ", "")
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")"""