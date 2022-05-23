#35 + dizer qual tipo de triangulo será formado
print('-='*20)
print('Analisando o seu triângulo')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses segmentos\033[32m formam triângulo.\033[m ', end='')
    if r1 != r2 != r3 != r1:
        print('Esse triângulo é escaleno.')
    elif r1 == r2 == r3:
        print('Esse triângulo é equilátero.')
    else:
        print('Esse triângulo é isósceles.')
else:
    print('Esses segmentos\033[31m não formam triangulo.\033[m')
