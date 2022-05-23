#leia três números e mostre qual o maior e o menor.
n = int(input('Digite um número: '))
n1 = int(input('Digite um número diferente: '))
n2 = int(input('Digite um número diferente dos demais: '))
if n >= n1 and n >= n2:
    print('{} é o maior número'.format(n))
    if (n1 + n2) >= n:
        print('É possível formar um triangulo com esses números')
    else:
        print('Não é possível formar um triangulo com esses números')
    if n1 >= n2:
        print('{} é o menor número'.format(n2))
    else:
        print('{} é o menor número'.format(n1))
else:
    if n >= n1 and n <= n2 or n <= n2 and n >= n1:
        if n1 >= n2:
            print('{} é o menor número e {} o maior'.format(n2, n1))
            if (n + n2) >= n1:
                print('É possível formar um triangulo com esses números')
            else:
                print('Não é possível formar um triangulo com esses números')
        else:
            print('{} é o menor número e {} o maior'.format(n1, n2))
            if (n + n1) >= n2:
                print('É possível formar um triangulo com esses números')
            else:
                print('Não é possível formar um triangulo com esses números')
    else:
        print('{} é o menor número'.format(n))
        if n1 >= n2:
            print('{} é o maior número'.format(n1))
            if (n + n2) >= n1:
                print('É possível formar um triangulo com esses números')
            else:
                print('Não é possível formar um triangulo com esses números')
        else:
            print('{} é o maior número'.format(n2))
            if (n + n1) >= n2:
                print('É possível formar um triangulo com esses números')
            else:
                print('Não é possível formar um triangulo com esses números')
