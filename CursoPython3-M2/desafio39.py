#leia ano de nascimento e informe: se ainda vai se alistar, se é hora de se alistar, se já passou do tempo
#mostrar o tempo que falta ou que passou do prazo
import datetime
ano = int(input('Qual o ano do seu nascimento? '))
atual = datetime.date.today().year
idade = atual - ano
g = str(input('Você é Homem?'))
if g.lower() == 'não' or g.lower() == 'nao':
    print('Mulher é privilegiada no brasil, pode ir pra casa.')
else:
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
    if idade == 18:
        print('É ano de se alistar!')
    if idade < 18:
        print('Ainda não é hora de se alistar, faltam {} anos.'.format((18 - idade)))
        print('Seu alistamento será em {}.'.format((atual + (18 - idade))))
    if idade > 18:
        print('Você se alistou há {} anos.'.format((idade - 18)))
        print('Seu alistamento foi em {}.'.format((ano + 18)))