#função leiaint() que funcione semelhante ao input, só que validando para aceitar
#apenas um valor numérico. isnumeric.
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
#Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')