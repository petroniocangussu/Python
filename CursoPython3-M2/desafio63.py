#Leia um numero n inteiro e mostre os n primeiros elementos seq.fibo
numero = int(input('Digite um número inteiro para ver esta quantidade de dígitos em fibo:'))
fibo1 = 0
fibo2 = 1
c = 2
if numero == 0:
    print('Parabéns imbecíl, aqui estão seus 0 números: .,/,.')
if numero == 1:
    print('{}. '.format(fibo1))
if numero == 2:
    print('{}, {}. '.format(fibo1, fibo2))
while numero > 2 and numero != c:
    print('{}, {}, '.format(fibo1, fibo2), end='')
    while numero != c:
        fibo3 = fibo1 + fibo2
        print('{}'.format(fibo3), end='')
        fibo1 = fibo2
        fibo2 = fibo3
        c += 1
        print('. ' if c == numero else ', ', end='')
print('Fim')