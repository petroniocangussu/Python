#Conversor de temperatura
c = float(input('Qual a temperatura em Celsius? '))
f = c * 9 / 5 + 32
k = c + 273.15
print('{}°C é igual a {:.2f}°F ou {:.2f}K'.format(c, f, k))