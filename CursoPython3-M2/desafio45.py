#Jogar pedra papel tesoura contra o pc
import random
import time
lista = ['pedra', 'papel', 'tesoura']
jog = str(input('pedra, papel ou tesoura?'))
jl = jog.lower()
pc = random.choice(lista)
print('-='*20)
print('Escolhendo...')
print('-='*20)
time.sleep(1)
print('Eu escolho {}.'.format(pc))
if jl == pc:
    print('Empatamos!')
if jl == 'pedra' and pc == 'papel' or jl == 'papel' and pc == 'tesoura' or jl == 'tesoura' and pc == 'pedra':
    print('Eu ganhei, você é ruim.')
if jl == 'pedra' and pc == 'tesoura' or jl == 'papel' and pc == 'pedra' or jl == 'tesoura' and pc == 'papel':
    print('Nããããão, eu perdi!!')
else:
    print('Jogada inválida')