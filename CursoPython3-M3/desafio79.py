#usuário digita vários valores numéricos diferentes (não adicionar iguais)
#Exibir os valores únicos em ordem crescente
valor = []
while True:
    n = int(input('Adicione um valor: '))
    if n in valor:
        print('Número repetido, tente novamente.')
    else:
        print('Número adicionado com sucesso.')
        valor.append(n)
    c = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if c == 'N':
        break
valor.sort()
print(f'Digitou {valor}')