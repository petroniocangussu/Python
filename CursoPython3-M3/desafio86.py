#crie um programa que crie umamatriz de dimensão 3x3 e preencha com valores
#lidos pelo teclado, no final mostre a matriz na tela com a forma correta.
matriz = [[], [], []]
for c in range (0, 3):
    matriz[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
    matriz[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
    matriz[2].append(int(input(f'Digite um valor para [2, {c}]: ')))
print('=-'*30)
print(f'Sua matriz foi: \n{matriz[0]}\n{matriz[1]}\n{matriz[2]}')