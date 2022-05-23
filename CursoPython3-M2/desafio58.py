#Desafio 28, acertando até adivinhar, mostrando quantos palpites foram necessários
import random
print('-=-' * 20)
print('Escolhi um número entre 0 e 5')
print('-=-' * 20)
c = random.randint(0,5)
r = int(input('Em que número eu pensei?'))
co = 0
while c != r:
    co = co + 1
    r = int(input('Você errou, tente novamente: '))
print('Você acertou o número, você precisou de {} tentativas.'.format(co+1))

#acertou = false
#while not acertou: jogador = int(input('Qual o seu palpite?'))