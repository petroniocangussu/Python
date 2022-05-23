#lista chamada números e duas funções (sorteio() e somapar()). A primeira
#sorteia 5 números e coloca-os dentro da lista. segunda vai mostrar soma
#entre os valores pares sorteados pela função anterior
from random import randint
from time import sleep
números = []
def sorteio(mínimo, máximo):
    temp = 0
    if mínimo > máximo:
        temp = mínimo
        mínimo = máximo
        máximo = temp
    print('Foram sorteados os números: ', end='')
    for i in range(0,quantidade):
        números.append(randint(mínimo, máximo))
        print(f'{números[i]}', end=', ', flush=True)
        sleep(0.5)
    print('fim.')
#somapar
def somapar():
    soma = 0
    print('A soma dos pares nesta lista é: ', end='')
    for n in range(0, quantidade):
        if números[n] % 2 == 0:
            soma += números[n]
    print(soma)
    print('Fim.')

#Programa principal
mínimo = str(input('Número mínimo? '))
while mínimo.isnumeric() == False:
    mínimo = str(input('Número mínimo? '))
mínimo = int(mínimo)
máximo = str(input('Número máximo? '))
while máximo.isnumeric() == False:
    máximo = str(input('Número máximo? '))
máximo = int(máximo)
quantidade = str(input('Quantos números deseja sortear? '))
while quantidade.isnumeric() == False:
    quantidade = str(input('Quantos números deseja sortear? '))
quantidade = int(quantidade)
sorteio(mínimo, máximo)
somapar()
