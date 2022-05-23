p = float(input('Preço de 250TCs? R$'))
q = int(input('Quantas TCs você deseja comprar?'))
pacote = q / 250
individual = p / 250
print(f'Você precisa comprar {pacote} pacotes de 250TCs para adquirir o montante que seja.')
print(f'Cada tc custará pra você R${individual:.2f}.')
print(f'O valor total dessa transação é de: R${p * pacote:.2f}')