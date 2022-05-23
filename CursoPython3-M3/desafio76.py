#tupla única com nomes dos produtos e seus respectivos preços na sequência. Mostre listagem de preços, organizando dados de forma tabular.
lista = ('Pizza', 35, 
         'Vibrador', 50, 
         'Shredder', 1400, 
         'Amor', 250,
         'Celular', 3000,
         'Computador', 1000,
         'Café', 8)
print('-=' * 20)
print(f'{"Listagem FRENÉTICA de preços":^40}')
print('-=' * 20)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>8.2f}')
print('-=' * 20)