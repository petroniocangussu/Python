from datetime import date, timedelta
atual = date.today()
boostpreço = [30, 75, 165, 345, 645]
exphoras = []
level = int(input('Que level você deseja alcançar? '))
exp = 50/3*((level ** 3) - (6 * (level ** 2)) + (17 * level)) - 12
exp2 = round(exp)
multiplicador = 1.5
print(f'A experiência necessária para o level {level} é de: {exp2}.')
exp3 = int(input('Qual a sua exp atual? '))
exp4 = exp2 - exp3
print(f'Faltam {exp4} pontos de experiência para alcançar o level {level}.')
expdia = cont = 0
stamina = float(input('Quantas horas você possui de stamina [6 minuto = 0.1]? '))
boost = boost2 = int(input('Deseja boostar quantas vezes? [0 = não boostar]'))
bonus = stamina - 39
raw2 = int(input('Qual a sua exp/h na raw? '))
while True:
    raw = raw2
    exphora = 0
    cont += 1
    if boost < 1 and bonus <= 0:
        exphora += raw
    if boost >= 1:
        raw = raw * multiplicador
        boost -= 1
    while 1 > bonus > 0:
        minutobonus = bonus * 60
        minutorestante = 60 - minutobonus
        bonusminuto = raw // 60
        horabonus = minutobonus * bonusminuto * multiplicador
        horaraw = minutorestante * bonusminuto
        print(f'Você teve {minutobonus} minutos de bonus, que te deu {horabonus:.0f} na verde e {horaraw:.0f} na laranja.')
        exphora = horabonus + horaraw
        bonus -= 1
    if bonus >= 1:
        expbonus = raw * multiplicador
        exphora += expbonus
        bonus -= 1
    print(f'Você fez {exphora} de exp na sua {cont}ª hora.')
    exphoras.append(exphora)
    expdia += exphora
    print(f'Sua exp feita no dia foi: {expdia:.0f}.')
    continuar = str(input('Deseja caçar mais uma hora? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
objetivo = exp4 // expdia
final = timedelta(objetivo) + atual
print('-='*15)
for i in range(0, cont):
    print(f'Exp da {i+1}ª hora: {exphoras[i]:>14.0f}')
print('-='*15)
print('RESUMO'.center(30))
print('-='*15)
print(f'{"Level desejado:":<20}{level:>10}')
print(f'{"Exp necessária:":<20}{exp4:>10}')
print(f'{"Horas bônus/dia:":<20}{stamina - 39:>10.0f}')
print(f'{"Boosts/dia:":<20}{boost2:>10}')
print(f'{"Média diária:":<20}{expdia:>10.0f}')
print(f'{"TCs necessárias:":<20}{boostpreço[boost2-1] * objetivo:>10.0f}')
print(f'{"Dia final:":<20}{final}')