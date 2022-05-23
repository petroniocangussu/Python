#Programa que calcule o valor a ser pago levando em consideração a condição
print('Calculadora de preço, como deseja pagar? No dinheiro ou cheque tem desconto.')
prod = float(input('Qual o preço do produto? '))
vezes = str(input('Deseja pagar "a vista" ou "parcelado"?'))
if vezes.lower() == 'a vista':
    modo = str(input('No dinheiro, cheque ou cartão?'))
    if modo.lower() == 'dinheiro' or 'cheque':
        print('Você obteve 10% de desconto, você deve pagar R${:.2f}.'.format((prod - (prod * 10 / 100))))
    else:
        print('Você obteve 5% de desconto, você deve pagar R${:.2f}.'.format((prod - (prod * 5 / 100))))
if vezes.lower() == 'parcelado':
    modo2 = int(input('Em quantas vezes pretende parcelar?'))
    if modo2 == 2:
        print('Você deve pagar o preço cheio do produto, R${:.2f}.'.format(prod))
    if modo2 > 2:
        print('Um juros de 20% incidirá, seu novo valor é de {:.2f}.'.format((prod + (prod * 20 / 100))))