#função contador(), receba três parâmetros: início, fim e passo, realizando contagem
#realizar três contagens: de 1 até 10 1 em 1. 10 a 0 2 em 2 e personalizada.
#Se 0 igual 1. Se negativo, inverter início e fim
from time import sleep
def contador(i, f, p):
    if p < 0:
        p = -p
    if p == 0:
        p = 1
    print(f'Contagem de {i} a {f} de {p} em {p}.')
    if i > f:
        p = -p
        f -= 1
    if i <= f:
        f += 1
    for c in range(i, f, p):
        print(c, end=', ', flush=True)
        sleep(0.2)
    print('fim!')
#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora faça uma progressão personalizada: ')
i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
contador(i, f, p)