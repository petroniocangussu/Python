def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
    """print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')"""
def contador(* núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('Fim!')
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números. ')
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    
#Programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(2, 4, 9)
"""soma(b=4, a=3)
soma(4+4, 5+5)"""
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)