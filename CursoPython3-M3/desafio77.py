#tupla com várias palavras(não usar acento), deve mostrar as vogais de cada palavra
lista = ('mercado', 'amor', 'computador', 'beijo', 'lindo', 'mesada', 'clima', 'tenso', 'entre', 'os', 'brothers')
for palavras in lista:
    print(f'\nPalavra {palavras} temos:', end=' ')
    for letra in palavras:
        if letra in 'aeiou':
            print(letra, end= ' ')
#for num in lista:
#   if num in 'aeiou':
#       print(num, end=', ')
#for pos, comida in enumerate(lista):
#    print(f'{comida} na posição {pos}')