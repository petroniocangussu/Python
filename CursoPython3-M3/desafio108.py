import moeda

n = float(input('Digite um preço: R$'))
p = int(input('Digite de aumento ou diminuição: '))
print(f'Metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'Aumentando {p}% temos: {moeda.moeda(moeda.aumentar(n, p))}')
print(f'Diminuindo {p}% temos: {moeda.moeda(moeda.diminuir(n, p))}')