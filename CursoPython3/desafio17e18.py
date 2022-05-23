#Ler comprimento do cateto oposto e do cateto adjacente, calcule e mostre o comprimento da hipotenusa
from cmath import sqrt
import math
catopo = float(input('Tamanho do cateto oposto: '))
catadj = float(input('Tamanho do cateto adjacente '))
#soma = ((catopo * catopo) + (catadj * catadj)) 
#hip = math.sqrt(soma)
#hi = math.hypot(catopo, catadj)
hi = (catopo ** 2 + catadj ** 2) ** (1/2)
print('Visto que o cateto oposto mede {} e o adjacente mede {}, a hipotenusa é de {:.2f}'.format(catopo, catadj, hi))

#calcular seno cosseno e tangente de um angulo qualquer 
angulo = float(input('Diga um angulo: '))
senoa = catopo / hi
senob = catadj / hi
print('Levando em consideração que o angulo escolhido foi {} o seno de A é {} enquanto o seno de b é {}.'.format(angulo, senoa, senob))

cosa = catadj / hi
cosb = catopo / hi
print('Levando em consideração que o angulo escolhido foi {} o cosseno de A é {} enquanto o cosseno de b é {}.'.format(angulo, cosa, cosb))

tanga = senoa / cosa
tangb = senob / cosb
print('Levando em consideração que o angulo escolhido foi {} a tangente de A é {:.2f} enquanto a tangente de b é {:.2f}.'.format(angulo, tanga, tangb))