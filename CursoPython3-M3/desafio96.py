#Função chamada área() que recebe dimensões de terreno (lar comp) e mostre área
def area(largura, comprimento):
    m2 = (largura * comprimento)
    print(f'A área deste terreno é {m2}m²')
#Programa principal
print('-=-Controle de terrenos-=-')
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)