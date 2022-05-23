from dado import leiadinheiro
from moeda import resumo

n = leiadinheiro('Digite um preço: R$')
p = leiadinheiro('Digite valor para aumento: ')
c = leiadinheiro('Digite valor para diminuição: ')
resumo(n, p, c)