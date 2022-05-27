from cmath import sqrt
from datetime import date, timedelta
from numpy import cbrt, sqrt
atual = date.today()

print('-='*35)
print('Bem vindo a calculadora, quer saber quando e em que level você ultrapassará sua competição?')
print('-='*35)
print('Para começar, faremos do método mais simples')
suaexp = int(input('Digite sua exp total: '))
suaexpmensal = int(input('Digite sua exp mensal: '))
alvoexp = int(input('Digite a exp total de quem você quer disputar: '))
alvoexpmensal = int(input('Digite a exp mensal do seu alvo: '))
if suaexpmensal < alvoexpmensal:
    print('Você faz menos experiência do que o seu alvo, não sendo possível o passar.')
else:
    print('-='*35)
    print(f'A diferença de experiência entre vocês é de {alvoexp - suaexp} pontos de experiência.')
    print(f'Você faz {suaexpmensal - alvoexpmensal} a mais de experiência por mês.')
    meses = (alvoexp - suaexp) / (suaexpmensal - alvoexpmensal)
    print(f'Essas médias se mantendo, você alcançará seu alvo em {meses:.1f} meses, ou {meses * 30:.0f} dias.')
    final = timedelta(meses * 30) + atual
    print(f'Alcançará o seu objetivo no dia {final}.')
    expfeita = meses * suaexpmensal
    exp = suaexp + expfeita
    print(f'Neste período você terá feito {expfeita:.0f} pontos de experiência, atingindo o total de: {exp:.0f}.')
    exp = float(exp)
    a = cbrt(1.732 * sqrt((243 * (exp**2)) - (48600 * exp) + 3680000) + (27 * exp) - 2700)
    round(a)
    level = a / 9.6548 - (5 * 4.6415) / (1.4422 * a) + 2
    print(f'Você ultrapassará seu alvo no level {level:.1f}.')
    print('-='*20)
    print('RESUMO'.center(40))
    print('-='*20)
    print(f'{"Diferença inicial:":<20}{alvoexp - suaexp:>20}')
    print(f'{"Diferença mensal:":<20}{suaexpmensal - alvoexpmensal:>20}')
    print(f'{"Dias para alcançar:":<20}{meses * 30:>20.0f}')
    print(f'{"Experiência necessária:":<25}{expfeita:>15.0f}')
    print(f'{"Experiência final:":<20}{exp:>20.0f}')
    print(f'{"Level final:":<20}{level:>20.0f}')
    print(f'{"Dia final:":<30}{final}')