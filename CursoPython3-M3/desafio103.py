#função ficha(), nome de jogador e gols marcados. Deverá ser capaz de mostrar
#a ficha do jogador, mesmo que algum dado não tenha sido informado.
def ficha(a = 'Desconhecido', b = 0):
    if a == '':
        a = '<Desconhecido>'
    print(f'Ficha do jogador: {a} fez {b} gols.')
    
    
#Programa principal
a = str(input('Nome do jogador? '))
b = str(input(f'Quantidade de marcados por {a}: '))
if b.isnumeric():
    b = int(b)
else:
    b = 0
ficha(a, b)