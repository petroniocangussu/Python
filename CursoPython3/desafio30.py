n = int(input('Digite um número inteiro: '))
if (n / 2) == int(n / 2):
    print('Seu número é par')
else:
    print('Seu número é impar')

#Resolução do professor:
resultado = n % 2
if resultado == 0:
    print('O seu número é par.')
else:
    print('O seu número é impar.')