#Compra de moeda
n = float(input('Quantos reais você possui? R$'))
d = 4.85
d1 = n / d
print('Com R${}, você pode comprar {:.2f}U$, considerando que o dólar está custando {}R$'.format(n, d1, d))