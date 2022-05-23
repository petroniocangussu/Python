lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
print(lanche[3])
print(lanche[-1])
print(lanche[1:3])
print(lanche[-2:])
print(lanche[-3:])
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')
print(len(lanche))
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(sorted(c))
print(len(c))
print(c.count(5))
print(c.index(8))

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
del(pessoa)
print(a)