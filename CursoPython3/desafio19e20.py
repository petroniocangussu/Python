#Professor quer sortear um dos 4 alunos para limpar o quadro, lendo o nome deles e escrevendo RANDOM o nome do escolhido
from random import choice, shuffle
aluno1 = str(input('Selecione um aluno: '))
aluno2 = str(input('Outro aluno: '))
aluno3 = str(input('Mais um: '))
aluno4 = str(input('Último: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print('O aluno selecionado para limpar o quadro foi {}.'.format(escolhido))

#Agora um programa que os organize em ordem
shuffle(lista)
print('Eles apresentarão o trabalho na seguinte ordem: ')
print(lista)