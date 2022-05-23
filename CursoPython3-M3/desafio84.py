#nome e peso de vários. liste-os. a-quantas. b-mais pesados. c-mais menors
"""lista = list()
pessoas = list()
dado = list()
cont = menor = maior = 0
while True:
    cont += 1
    print('Olá, bem vindo ao verificador de peso.')
    nome = pessoas.append(str(input('Qual o seu nome? ')))
    peso = dado.append(float(input('Qual o seu peso? quilos')))
    lista.append(nome)
    lista.append(peso)
    if cont == 1:
        maior = peso
        menor = peso
    if cont > 1:
        if dado[len(dado)-1] > dado[len(dado) -2]:
            maior = dado[-1]
    mais = str(input('Quer continuar? [S/N]')).strip().lower()[0]
    if mais == 'n':
        break
print(f'Você adicionou {cont} pessoas à sua lista.')
print(f'O maior peso foi {maior}quilos')"""
temp = []
princ = []
menor = maior = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    mais = str(input('Quer continuar? [S/N]')).strip().lower()[0]
    if mais == 'n':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas. ')
print(f'O maior peso foi de {maior}quilos. Peso de: ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end ='')
print(f'\nO menor peso foi de {menor}quilos. Peso de: ', end ='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end = '')