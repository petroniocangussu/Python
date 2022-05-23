cont = 1
while True:
    print(cont)
    cont += 1
    if cont == 10:
        break
print("acabou")
print(f'A contagem é {cont}')
nome = 'José'
idade = 33
salário = 974.35
print(f'O {nome:-^20} tem {idade} anos e ganha R${salário:.3f}.')
