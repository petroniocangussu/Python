print('Bem vindo ao Bancaum')
valor = int(input('Quanto deseja sacar?'))
total = valor
cédula = 50
totalcédula = 0
while True:
    if total >= cédula:
        total = total - cédula
        totalcédula = totalcédula + 1
    else:
        if totalcédula > 0:
            print(f'Total de {totalcédula} cédulas de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 5
        elif cédula == 5:
            cédula = 1
        totalcédula = 0
        if total == 0:
            break
print('Volte sempre')