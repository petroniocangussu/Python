#Leia ano de nascimento e mostre sua categoria
from datetime import date
ano = int(input('Qual o ano do seu nascimento? '))
atual = date.today().year
idade = date.today().year - ano
print('O atleta possui {} anos.'.format(idade))
if idade <= 9:
    print('A sua categoria é a mirim.')
elif idade <= 14:
    print('A sua categoria é a infantil.')
elif idade <= 19:
    print('A sua categoria é a junior.')
elif idade <= 25:
    print('A sua categoria é a sênior.')
else:
    print('A sua categoria é a master.')