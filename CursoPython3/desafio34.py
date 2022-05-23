#Qual salário? Dar aumento para salários maiores ou menores que 1250
s = int(input('Qual o seu salário?'))
if s >= 1250:
    print('O seu novo salário é {:.2f}R$, um aumento de {:.2f}R$, referente a 10%.'.format((s + (s * 10 / 100)), (s * 10 / 100)))
else:
    print('O seu novo salário é {:.2f}R$, um aumento de {:.2f}R$, referente a 15%.'.format((s + (s * 15 / 100)), (s * 15 / 100)))