#duas notas, calcule média, mostre mensagem final de acordo com média
n = float(input('Digite a nota da primeira prova: '))
d = float(input('Digite a nota da segunda: '))
m = (n + d) / 2
print('A sua média final foi {:.1f}.'.format(m))
if m >= 7:
    print('Parabéns você foi\033[032m aprovado!\033[m')
if 7 > m >= 5:
    print('Você foi para a\033[33m recuperação!\033[m')
if m < 5:
    print('Pau no seu cu,\033[31m perdeu de ano!\033[m')