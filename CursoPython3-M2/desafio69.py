#leia idade e sexo de várias pessoas. deve perguntar se quer ou não continuar.
mais = contp = conth = contm = 0
while True:
    i = int(input('Qual a sua idade: '))
    s = str(input('Qual o seu sexo? [H/M]')).strip().upper()[0]
    while s != 'H' and s != 'M':
        s = str(input('Qual o seu sexo? [H/M]')).strip().upper()[0]
    if i >= 18:
        contp += 1
    if s == 'H':
        conth += 1
    if s == 'M' and i < 20:
        contm += 1
    mais = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while mais != 'S' and mais != 'N':
        mais = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if mais == 'N':
        break
print(f'''Você cadastrou {contp} pessoas com mais de 18 anos. 
      {conth} Homens foram cadastrados.
      {contm} Mulheres com menos de 20 anos foram cadastradas.''')