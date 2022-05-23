#Preço com desconto
preço = float(input('Qual o preço do produto? R$'))
desconto = float(input('Qual o desconto aplicado no produto? '))
dedução = preço * desconto / 100
final = preço - dedução
print('O valor de {:.2f}R$, com {:.2f} porcento de desconto é {:.2f}R$, considerando que {:.2f}R$ foram subtraídos'.format(preço, desconto, final, dedução))