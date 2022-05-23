#cria vários números, mostre a média entre eles, o maior valor e o menor. #programa deve perguntar se usuário quer continuar ou não
from time import sleep
c = n = som = maior = menor = 0
continuar = 'S'
while continuar != 'N':
    n = int(input('Adicione um número: '))    
    sleep(0.5)
    som += n
    c += 1
    print('A soma destes {} números é {}, a média desse valores é {:.2f}.'.format(c, som, (som / c)))
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    print('O maior número digitado foi {}, enquanto o menor número digitado foi {}.'.format(maior, menor))
    continuar = str(input('Deseja adicionar mais números?[S/N] ')).strip().upper()[0]
print('FIM')