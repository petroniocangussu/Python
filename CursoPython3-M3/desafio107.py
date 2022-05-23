#Crie um módulo moeda.py, funções: aumentar(), diminuir(), dobro(), metade().
#Faça um programa que importe esse módulo e use algumas dessas funções.
import moeda

n = float(input('Digite um preço: R$'))
p = int(input('Digite de aumento ou diminuição: '))
print(f'Aumentando {p}% temos: R${moeda.aumentar(n, p):.2f}')
print(f'Diminuindo {p}% temos: R${moeda.diminuir(n, p):.2f}')
print(f'O dobro de R${n} é R${moeda.dobro(n):.2f}')
print(f'Metade de R${n} é R${moeda.metade(n):.2f}')