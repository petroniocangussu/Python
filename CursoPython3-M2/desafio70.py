#nome e preço de vários produtos. Perguntar se quer continuar. Quantos custam mais de 1000. total gasto. nome do prod mais barato
soma = prodb = preço = contg = contm = preçob = 0
print('-=-*-=- Bem vindo a Milenas Shop -=-*-=-')
while True:
    nome = str(input('Olá, que item deseja adquirir? '))
    preço = float(input('Qual o preço do seu produto? R$'))
    soma += preço
    contg += 1
    if preço >= 1000:
        contm += 1
    if contg == 1 or preço < preçob:
        prodb = nome
        preçob = preço
    mais = ' '
    while mais != 'N' and mais != 'S':
        mais = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if mais == 'N':
        break
print(f'Seu saldo total foi de {soma}, você adquiriu {contm} itens que custam mais de R$1000,00 e o seu produto mais barato foi {prodb} e custou R${preçob}. Volte sempre.')        