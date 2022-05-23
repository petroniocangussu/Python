#ler números, liste-os, crie 2 listas, pares e impares. mostre as 3 listas.
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    if r == 'N':
        break
print('=-'*30)
print(f'Os números pares da sua lista são: {listapar}.')
print(f'Os números impares da sua lista são: {listaimpar}.')
print(f'A sua lista completa foi: {listapar+listaimpar}.')
print('=-'*30)