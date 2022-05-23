def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3

def escreva(a):
    print('~'*len(a))
    print(a)
    print('~'*len(a))

def area(largura, comprimento):
    m2 = (largura * comprimento)
    print(f'A área deste terreno é {m2}m²')

def contador(i, f, p):
    from time import sleep
    if p < 0:
        p = -p
    if p == 0:
        p = 1
    print(f'Contagem de {i} a {f} de {p} em {p}.')
    if i > f:
        p = -p
        f -= 1
    if i <= f:
        f += 1
    for c in range(i, f, p):
        print(c, end=', ', flush=True)
        sleep(0.2)
    print('fim!')

def maior(* núm):
    from time import sleep
    print(f'-=-=-=-=-=-=-=-=- Analisando os números -=-=-=-=-=-=-=-=-')
    if (len(núm)) == 0:
        print('A sua sequência não possui números.')
    else:
        print(f'Recebi os valores {núm}, são ao todo {len(núm)} números. \nO maior destes números é {max(núm)} ')
    sleep(1)
    
def sorteio(mínimo, máximo, quantidade):
    from random import randint
    from time import sleep
    números = []
    temp = 0
    if mínimo > máximo:
        temp = mínimo
        mínimo = máximo
        máximo = temp
    print('Foram sorteados os números: ', end='')
    for i in range(0,quantidade):
        números.append(randint(mínimo, máximo))
        print(f'{números[i]}', end=', ', flush=True)
        sleep(0.5)
    print('fim.')

def somapar(*números, quantidade):
    soma = 0
    print('A soma dos pares nesta lista é: ', end='')
    for n in range(0, quantidade):
        if números[n] % 2 == 0:
            soma += números[n]
    print(soma)
    print('Fim.')

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

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    print(f'O fatorial de {num} é {f}')
    show = str(input('Deseja mostrar a multiplicação? [S/N]')).strip().upper()[0]
    if show == 'S':
        for c in range(num, 0, -1):
            if c > 1:
                print(f'{c}', end=' x ')
            else:
                print(f'{c}', end=' = ')
        print(f)
    else:
        print('Fim!')
    help = str(input('Deseja ajuda? [S/N]')).strip().upper()[0]
    if help == 'S':
        help(fatorial)
    else:
        print('Fim do programa.')

def ficha(a = 'Desconhecido', b = 0):
    if a == '':
        a = '<Desconhecido>'
    print(f'Ficha do jogador: {a} fez {b} gols.')

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            return n

def notas(*n, sit=False):
    """
    Função para notas e situação de uma turma.
    n: Notas a adicionar (aceita várias).
    sit: situação do aluno (se deve adicionar ou não), Default:False
    Return: Dicionário com todas as informações.
    """
    dic = {}
    dic['Total'] = len(n)
    dic['Maior'] = max(n)
    dic['Menor'] = min(n)
    dic['Média'] = sum(n) / len(n)
    if sit:
        if dic['Média'] >= 7:
            dic['Situação'] = 'Boa'
        elif 5 <= dic['Média'] < 7:
            dic['Situação'] = 'Média'
        else:
            dic['Situação'] = 'Ruim'
    return dic