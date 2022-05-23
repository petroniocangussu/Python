#Leia vários números - liste-os. A-Quantos foram. B-Lista decre. C-check 5
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    p = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if p == 'N':
        break
print('-='*30)
print(f'Você adicionou {len(lista)} números à sua lista.')
lista.sort(reverse=True)
print(f'Esta é a sua lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O número 5 faz parte da sua lista.')
else:
    print('O número 5 não foi encontrado na sua lista.')
print('-='*30)