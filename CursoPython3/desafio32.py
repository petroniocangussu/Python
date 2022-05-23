#Leia um ano e mostre se ele é bissexto
import datetime
ano = int(input('Digite um ano, 0 para o atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ((ano / 4) == int(ano / 4)) and ((ano / 100 != int(ano/100))):
    print('Seu \033[32m ano \033[m é bissexto, divisível por 4, não divisível por 100')
else:
    if (ano / 400) == int(ano / 400):
        print('Seu ano é divisível por 400, logo é bissexto')
    else:
        print('\033[31m{}\033[m não é bissexto.'.format(ano))

#Esse aqui me deu orgulho.
#solução do professor if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
