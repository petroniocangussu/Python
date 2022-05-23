from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas', 'Cadastrar novas', 'Sair do sistema'])
    if resposta == 1:
        #Listar conteúdo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        #Cadastrar pessoas
        cabeçalho('Cadastrar novas')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema!')
        break
    else:
        print('\033[31mErro, digite novamente: \033[m')
    sleep(1)