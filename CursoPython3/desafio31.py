#Distancia em km e calcule preço da passagem com 2 possibilidades
km = float(input('Qual a distância da viagem?'))
if km >= 200:
    print('Parabéns! você obteve um desconto, considerando R$0,45/km \
o total a pagar é: {}R$'.format(km*0.45))
else:
    print('Cada km custa R$0,50, totalizando {}R$'.format(km*0.5))
#preço = km * 0.5 if km <= 200 else km * 0.45