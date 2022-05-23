#Refaça o 61 perguntando se ele quer mostrar mais termos. 0 encerra
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
limitador = 1
aditor = 1
contador = 0
t = p
print('-==-'*10)
while aditor != 0:
    print('{} -> '.format(t), end='')
    t = t + r
    contador += 1
    limitador = limitador + 1
    if limitador == 11:
        print('PAUSA')
        aditor = int(input('Quantos termos você quer mostrar a mais?'))
        limitador = limitador - aditor
print('A progressão foi finalizada com {} termos.'.format(contador))