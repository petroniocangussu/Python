#leia ano de nascimento de 7 pessoas. Quantas são de maior e quantas de menor?
from datetime import date
ca = 0
cb = 0
cc = 0
for c in range(1,8):
    a = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(c)))
    if date.today().year - a >= 21:
        ca = ca + 1
    if date.today().year - a < 21:
        cb += +1
    if date.today().year < a:
        cc += +1
print('{} são maiores e {} são menores.'.format(ca, cb))        
print('{} pessoas ainda não nasceram.'.format(cc))