import moeda

n = float(input('Digite um preço: R$'))
p = int(input('Digite de aumento ou diminuição: '))
print(f'Metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f'Aumentando {p}% temos: {moeda.aumentar(n, p, True)}')
print(f'Diminuindo {p}% temos: {moeda.diminuir(n, p, True)}')