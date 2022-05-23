#Aumento de salário
n1 = float(input('Qual é o salário? R$'))
n2 = float(input('Qual o percentual de aumento que lhe foi prometido? '))
a = n1 * n2 / 100
s = n1 + a
print('Considerando que o seu salário é de {} e o aumento é de {} porcento, o seu novo salário será de {}, acrescentando um montante de {} reais'.format(n1, n2, s, a))
