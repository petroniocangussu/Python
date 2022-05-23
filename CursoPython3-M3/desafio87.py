#aprimore o 86 a-soma dos pares b-soma da 3a coluna c-maior da segunda linha
matriz = [[], [], []]
somapar = somaterceira = maior = 0
for c in range (0, 3):
    matriz[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
    if c == 1:
        maior = matriz[0][1]
    matriz[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
    if c == 1 and matriz[1][1] > maior:
        maior = matriz[1][1]
    matriz[2].append(int(input(f'Digite um valor para [2, {c}]: ')))
    if c == 1 and matriz[2][1] > maior:
        maior = matriz[2][1]
    if matriz[0][c] % 2 == 0:
        somapar += matriz[0][c]
    if matriz[1][c] % 2 == 0:
        somapar += matriz[1][c]
    if matriz[2][c] % 2 == 0:
        somapar += matriz[2][c]
print('=-'*30)
print(f'Sua matriz foi: \n{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
print(f'A soma dos pares foi: {somapar}.')
print(f'A soma dos números da terceira coluna foi {matriz[0][2] + matriz[1][2] + matriz[2][2]}.')
print(f'O maior número da segunda coluna foi: {maior}')