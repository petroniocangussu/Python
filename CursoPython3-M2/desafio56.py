#leia nome, idade, sexo de 4 pessoas, mostre:#média de idade#nome do homem mais velho#Quantas mulheres têm menos de 20
som = 0
somm = 0
somh = 0
idade = 0
velho = ''
for t in range(1,5):
    print('----- {}ª PESSOA -----'.format(t))
    n = str(input('Qual o seu nome? '))
    i = int(input('Qual a sua idade? '))
    s = str(input('Qual o seu sexo? ')).strip().lower()
    som = som + i
    if i < 20 and s in 'mulher, feminino, femea, f':
        somm = somm + 1
    if s == 'homem' or s == 'masculino' or s == 'macho' or s == 'm' or s == 'h':
        somh = somh + 1
        if somh == 1:
            idade = i
            velho = n
        else:
            if i > idade:
                idade = i
                velho = n
print('A média de idade destes 4 indivíduos é de {:.1f} anos.'.format(som / 4))
print('Desta lista {} mulheres possuem menos de 20 anos.'.format(somm))
print('O homem mais velho desta lista tem {} e ele se chama {}.'.format(idade, velho.capitalize()))