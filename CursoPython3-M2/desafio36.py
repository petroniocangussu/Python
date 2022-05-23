#Escreva programa para aprovar empréstimo
#Programa pergunta valor da casa, salário e quantos anos vai pagar.
#Calcular valor da prestação, não podendo exceder 30% do salário
import time
print("""Olá, bem vindo ao Banco Nicaixa, por favor responda as perguntas a seguir 
      para que possamos avaliar a aprovação do seu crédito SEM JUROS""")
casa = int(input('Qual o valor da casa que deseja adquirir? '))
salario = int(input('Qual o seu salário mensal?'))
mes = int(input('Em quantos meses deseja pagar?'))
p = casa // mes
print('Calculando valor da prestação mensal...')
time.sleep(1)
print('O valor mensal que você deverá despender é de R${:.2f}.'.format(p))
print('Processando...')
time.sleep(1)
if p >= salario * 30 // 100:
    print('Considerando que a prestação mensal não pode exceder\033[33m 30%\033[m do salário (R${:.2f}), o seu crédito\033[31m não foi aprovado.\033[m'.format((salario * 30 // 100)))
else:
    print('Considerando que a prestação mensal não pode exceder\033[33m 30%\033[m do salário (R${:.2f}), o seu crédito\033[32m foi aprovado.\033[m'.format((salario * 30 // 100)))