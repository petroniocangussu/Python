#Programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#Pedir para o usuário tentar descobrir o n escolhido
#Programa deve escrever na tela se o usuário acertou
import random
import time
print('-=-' * 20)
print('Escolhi um número entre 0 e 5, que número eu escolhi?')
print('-=-' * 20)
n = random.randint(0,5)
n2 = int(input('Em que número eu pensei?'))
print('Processando...')
time.sleep(1)
if n2 == n:
    print('Parabéns você\033[32m acertou!\033[m')
else:
    print('\033[31mErrou\033[m, o meu número era o {}, tente de novo!'.format(n))