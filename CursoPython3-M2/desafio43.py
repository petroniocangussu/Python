#leia peso e altura, calcule o IMC, mostre o status:
p = float(input('Qual o seu peso? '))
a = float(input('Qual a sua altura em metros? '))
imc = p // (a**2)
print('O seu IMC é de {}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
if imc >= 18.5 and imc < 25:
    print('Você está no peso ideal.')
if imc >= 25 and imc < 30:
    print('Você está com sobrepeso.')
if imc >= 30 and imc < 40:
    print('Você está obeso.')
if imc >= 40:
    print('você é um elefante.')