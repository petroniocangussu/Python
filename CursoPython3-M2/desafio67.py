#programa leia vários números. faça tabuada, pare no negativo.
while True:
    n = int(input('Digite um número para ver a sua tabuada [negativo para sair]: '))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n * c}')
print('Você encerrou o programa!')