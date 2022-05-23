#Aluguel de carro
dia = int(input('Quantos dias você quer alugar o carro? '))
diaria = float(input('Qual o preço da diária? '))
km = float(input('Quantos km você ira percorrer? '))
gas = float(input('Qual o preço da gasolina? '))
consumo = float(input('Quantos km o carro faz por litro?'))

print('Considerando que você alugará o carro por {} dias e o preço da diária é de {:.2f}R$, o valor total será {:.2f}R$.'.format(dia, diaria, (dia * diaria)))
print('Considerando que você deseja percorrer {:.2f}km, e o consumo do carro ser de {:.2f}km/l, o consumo de combustível será de {:.2f}l'.format(km, consumo, (km / consumo)))
print('Considerando que a gasolina está custando {:.2f}R$ por litro, o seu gasto com combustível será de {:.2f}R$.'.format(gas, (km / consumo * gas)))
print('O gasto total com a sua viagem será de {:.2f}R$. '.format((dia * diaria) + (km / consumo * gas)))