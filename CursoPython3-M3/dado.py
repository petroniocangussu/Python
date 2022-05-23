def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mTivemos problemas com os tipos de dados digitados.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar os dados!\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Infelizmente o dado informado não é compatível com o programa.')
            continue
        except (KeyboardInterrupt):
            print('O usuário decidiu parar o programa.')
            return 0
        else:
            return n

def leiadinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)