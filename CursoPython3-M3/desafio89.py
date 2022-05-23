#leia nome e duas notas de vários alunos, guarde tudo numa lista composta.
#mostre um boletim, contendo média de cada um, permita ao usuário mostrar
#notas de cada aluno individualmente
boletim = []
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    prova1 = float(input('Nota 1: '))
    prova2 = float(input('Nota 2: '))
    média = (prova1 + prova2) / 2
    aluno = [nome, prova1, prova2, média]
    cont = str(input('Quer continuar? [s/n]')).strip().lower()[0]
    boletim.append(aluno[:])
    aluno.clear()
    if cont == 'n':
        break
print('-=' * 12)
print(f'{"N° -  ":<6}{"Nome  - ":<10}{"Média":>8}')
print('-' * 24)
for c in range(0, len(boletim)):
    print(f'{c:<6}{boletim[c][0]:<10}{boletim[c][3]:>8}')
while True:
    i = int(input('Deseja mostra a nota de quem? (999 para interromper): '))
    if i == 999:
        print('Programa finalizado.')
        break
    else:
        print(f'Notas de {boletim[i][0]} são: {boletim[i][1]} e {boletim[i][2]}.')
print('Volte sempre.')