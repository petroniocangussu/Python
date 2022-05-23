#Refaça o desafio 9, mostrando  de um número escolhido, usando laço for
n = float(input('Escolha um número: '))
for m in range(1, 11):
    print('{} x {:.0f} = {:.2f}'.format((m), (n), (n * m)))