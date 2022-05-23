#Função voto(), recebe como parâmetro ano de nascimento, retornando valor
#LITERAL, indicando se a pessoa tem voto negado, opcional ou obrigado.
def voto(n = 0):
    from datetime import date
    ano = date.today().year - n
    print(f'Hora de verificar a sua situação eleitoral. \n=-=-=-=-=-=-=-=-Processando-=-=-=-=-=-=-=-=\nVocê possui {ano} anos de idade. ', end='')
    if ano < 16:
        print('Voto negado.')
    elif 16 <= ano < 18 or ano > 65:
        print('Voto opcional.')
    else:
        print('Voto obrigatório.')
#Programa principal
n = str(input('Qual o ano do seu nascimento?? '))
while n.isnumeric() == False:
    n = str(input('ANO! '))
n = int(n)
#ano = int(input('Qual o ano do seu nascimento? '))
voto(n)