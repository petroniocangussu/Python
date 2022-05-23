num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.pop(2)
num.remove(2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.sort()
print(num)

#valores = []
#for cont in range(0,5):
#   valores.append(int(input('Digite um valor: ')))
#for v in valores:
#   print(f'{v}...', end='')
#for c, v in enumerate(valores):
#   print(f'Na posição {c} encontrei o valor {v}!')
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(a)
print(b)
print(b[0])
print(a.count(3))