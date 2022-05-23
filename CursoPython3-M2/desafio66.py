#programa leia vários números. pare no 999, mostre quant de n e a soma
som = n = cont = 0
while True:
    som += n
    n = int(input('Digite um valor: '))
    cont += 1
    if n == 999:
        break
print(f'Você digitou {cont} dígitos que totalizaram: {som}')