#20 primeiros do brasileirão, mostre: a-os 5 primeiros. b-os 4 últimos. c-lista em ordem alfabética. d-posição do são paulo
brasileirão = ('Corinthians', 'Atlético Mineiro', 'Bragantino', 'Flamengo', 
               'Santos', 'Fluminense', 'São Paulo', 'Coritiba', 
               'América Mineiro', 'Botafogo', 'Cuiabá', 'Ceará', 
               'Internacional', 'Avaí', 'Palmeiras', 'Juventude', 'Goiás', 
               'Atlético Goianiense', 'Fortaleza', 'Atlético Paranaense')
while True:
    n = int(input('''Olá, bem vindo à tabela do Brasileirão, o que gostaria de conferir?
          [ 1 ] Os 5 primeiros colocados.
          [ 2 ] Os 4 últimos colocados.
          [ 3 ] Times em ordem alfabética.
          [ 4 ] Posição do Coritiba.
          [ 5 ] Sair do programa.
          Qual é a sua opção? '''))
    if n == 1:
        print(f'Os 5 primeiros colocados são: {brasileirão[0:5]}')
    elif n == 2:
        print(f'Os 4 últimos colocados são: {brasileirão[-4:]}')
    elif n == 3:
        print(f'Esse são os times em ordem alfabética: {sorted(brasileirão)}')
    elif n == 4:
        print(f'O Coritiba encontra-se na posição: {brasileirão.index("Coritiba") + 1}ª')
    elif n == 5:
        break
    else:
        print('Desculpe, não entendi.')