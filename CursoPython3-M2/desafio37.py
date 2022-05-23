#Leia um número inteiro e peça a base de conversão
n = int(input('Digite um número inteiro: '))
print("""Escolha uma base de conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal""")
b = int(input('Sua opção: '))
if b == 1:
    print('Você optou por binário, seu número é: {}.'.format(bin(n)[2:]))
elif b == 2:
    print('Você optou por octal, seu número é {}.'.format(oct(n)[2:]))
elif b == 3:
    print('Você optou por hexadecimal, seu número é {}.'.format(hex(n)[2:]))
else:
    print('Desculpe, não entendi.')