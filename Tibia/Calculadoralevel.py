from datetime import date, timedelta
atual = date.today()
level = int(input('Que level você deseja alcançar? '))
exp = 50/3*((level ** 3) - (6 * (level ** 2)) + (17 * level)) - 12
exp2 = round(exp)
print(f'A experiência necessária para o level {level} é de: {exp2}.')
exp3 = int(input('Qual a sua exp atual? '))
exp4 = exp2 - exp3
print(f'Você precisa de {exp4} para alcançar o level {level}.')
expd = int(input('Qual a sua experiência média diária?'))
objetivo = exp4 / expd + 1
print(f'Com essa média diária, alcançará o seu objetivo em {objetivo:.0f} dias.')
final = timedelta(objetivo) + atual
print(f'Alcançará seu objetivo no dia {final}.')