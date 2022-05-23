#Aprimore o 93 para várias pessoas. Visualização de detalhe de aproveitamento.
num = soma = cont = 0
time = []
while True:
    soma = 0
    quantidade = []
    geral = {'Nome':'','Gols':quantidade, 'Total':''}
    geral['Nome'] = str(input('Nome: ')).strip().capitalize()
    partidas = int(input(f"Quantas partidas {geral['Nome']} jogou? "))
    for c in range(0, partidas):
        num = int(input(f'Quantos gols na partida {c+1}? '))
        quantidade.append(num)
        soma += num
    geral['Total'] = soma
    time.append(geral.copy())
    cont += 1
    while True:
        continuar = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('-='*20)
print(time)
print('-='*20)
print(f'{"Cod":<5} {"Nome":<5} {"Gols":>10} {"Total":>15}')
for i in range(0, cont):
    print(f"{i:<5} {time[i]['Nome']:<5} {time[i]['Gols']} {time[i]['Total']:>15}")
while True:
    print('-='*20)
    jogador = int(input('Mostrar dados de qual jogador?(999 encerra) '))
    if jogador == 999:
        break
    if jogador >= len(time):
        print(f'Erro, não existe jogador com o código {jogador}.')
    else:
        print(f"Mostrando o levantamento do jogador {time[jogador]['Nome']}")
        for n in range(0, len(time[jogador]['Gols'])):
            print(f"No jogo {n+1} fez {time[jogador]['Gols'][n]} gols.")
print('-='*20)
print('Programa encerrado, volte sempre.')