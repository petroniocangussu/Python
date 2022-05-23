def aumentar(n = 0, p = 0, c = False):
    n = n + n * p / 100
    return n if c != True else moeda(n)
    
def diminuir(n = 0, p = 0, c = False):
    n = n - n * p / 100
    return n if c != True else moeda(n)
    
def dobro(n = 0, c = False):
    n = n * 2
    return n if c != True else moeda(n)
    
def metade(n = 0, c = False):
    n = n / 2
    return n if c != True else moeda(n)
    
def moeda(n= 0, moeda='R$'):
    return(f'{moeda}{n:.2f}').replace('.',',')

def resumo(n = 0, p = 0, c = 0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'{"Preço analisado:":<20}{moeda(n):>10}')
    print(f'{"Dobro do preço:":<20}{dobro(n, True):>10}')
    print(f'{"Metade do preço:":<20}{metade(n, True):>10}')
    print(f'{f"{p:.1f}% de aumento":<20}{aumentar(n, p, True):>10}')
    print(f'{f"{c:.1f}% de diminuição":<20}{diminuir(n, c, True):>10}')       