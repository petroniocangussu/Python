#Mostre contagem regressiva para fogos de artifício, de 10 a 0, pausa de 1seg
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print('Feliz ano novo')