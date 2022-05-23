#Programa que calcule o valor a ser pago levando em consideração a condição
prod = float(input('Qual o preço do produto? R$'))
print("""Calculadora de preço, como deseja pagar? No dinheiro ou cheque tem desconto.
      [1] À vista dinheiro/cheque
      [2] À vista cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão""")
vezes = int(input('Qual a sua opção?'))
if vezes == 1:
    print('Você obteve 10% de desconto, você deve pagar R${:.2f}.'.format((prod - (prod * 10 / 100))))
elif vezes == 2:
    print('Você obteve 5% de desconto, você deve pagar R${:.2f}.'.format((prod - (prod * 5 / 100))))
elif vezes == 3:
    print('Você deve pagar o preço cheio do produto (R${:.2f}), 2 parcelas de R${:.2f}.'.format(prod, (prod // 2)))
elif vezes == 4:
    print('Um juros de 20% incidirá, seu novo valor é de {:.2f}.'.format((prod + (prod * 20 / 100))))
    parcelas = int(input('Deseja parcelar em quantas parcelas?'))
    print('Você deverá pagar {} parcelas de R${:.2f}.'.format(parcelas, (((prod + (prod * 20 / 100)) / parcelas))))
else:
    print('Opção inválida, tente novamente.')