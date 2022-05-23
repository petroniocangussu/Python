#tupla totalmente preenchida com uma contagem por extenso de zero a vinte. seu program deve ler um número digitado e mostra-lo por extenso.
números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 
           'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20. '))
while n < 0 or n > 20:
    n = int(input('Digite um número entre 0 e 20. '))
print(números[n])