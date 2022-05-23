#Área e tinta necessária para pintar uma parede e preço
a = float(input('Qual a altura em metros da parede?: '))
l = float(input('Qual a largura em metros da parede?: '))
m = a * l
b = m / 2
print('Considerando que a parede possui {} metros de altura e {} de largura, está parede possui {:.2f}m²'.format(a, l, m))
print('Considerando que um balde de tinta é suficiente para pintar 2m², serão necessários {:.2f} baldes'.format(b))
p = float(input('Qual o preço do balde de tinta?: R$'))
pf = b * p
print('Considerando que cada balde custa {}R$, o preço final será de {:.2f}R$'.format(p, pf))