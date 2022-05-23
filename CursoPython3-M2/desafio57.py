#leia sexo, só aceite M ou F, caso errado peça novamente
s = str(input('Qual seu sexo? [M/F]')).strip().upper()[0]
#while s not in 'MF':
while s != 'M' and s != 'F':
    s = str(input('Dados inválidos, qual seu sexo? [M/F]')).strip().upper()[0]
    if s == 'M':
        print('Seu sexo é o masculino')
    if s == 'F':
        print('Seu sexo é o feminino')