#Programa com nome completo que mostre várias coisas
nome = str(input('Digite seu nome completo: ')).strip()
#Todas as letras maiúsculas
print('Nome com todas as letras maiúsculas: {}'.format(nome.upper()))
#Todas minúsculas
print('Nome com todas as letras minusculas: {}'.format(nome.lower()))
#Quantas letras possui (sem espaços)
print('Seu nome possui {} letras'.format(len(nome) - nome.count(' ')))
#Quantas possui o primeiro nome
print('Seu primeiro nome possui {} letras'.format(nome.find(' ')))
dividido = nome.split()
#print(len(dividido[0]))
#Crie um programa que leia o nome de alguém e diga se ela tem Silva no nome
print('O nome tem Silva? {}'.format('SILVA' in nome.upper()))
#Leia o nome completo, mostrando primeiro e ultimo nome separadamente
print('Seu primeiro nome é: {}. '.format(dividido[0]))
print('Seu último nome é: {}. '.format(dividido[len(dividido)-1]))
