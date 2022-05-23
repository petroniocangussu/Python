#7 valores numéricos, liste-os(única), mantenha separado pares de impares.
#no final, mostre os valores pares e ímpares em ordem crescente
temp = []
princ = [[], []]
while True:
    temp.append(int(input(f'Digite o {(len(princ[0]) + len(princ[1]) + 1)}° número: ')))
    if temp[0] % 2 == 0:
        princ[0].append(temp[:])
    else:
        princ[1].append(temp[:])
    temp.clear()
    if len(princ[0]) + len(princ[1]) == 7:
        break
print('=-'*30)
print(f'Os valores digitados foram {princ}.')
princ[0].sort()
print(f'Os valores pares são: {princ[0]}')
princ[1].sort()
print(f'Os valores ímpares são: {princ[1]}')