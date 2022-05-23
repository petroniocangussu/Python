import uteis
num = int(input('Digite um valor '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'*2={uteis.dobro(num)}, *3={uteis.triplo(num)}')