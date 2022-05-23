#velocidade de um carro. Caso ultrapasse 80kmh Multa. Multa 7*cada km ultrapassado
km = int(input('Qual a velocidade do carro?'))
if km >= 80:
    print('O seu carro foi\033[31m multado no valor de {:.2f}R$\033[m'.format((km - 80) * 7))
else:
    print('\033[32mVocê respeitou os limites de velocidade!\033[m')