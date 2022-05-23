#simule funcionamento de um caixa. Pergunte valor a ser sacado. programa informa quantas cédulas de cada valor serão entregues.
#caixa possui cédulas de 1, 10, 20, 50
print('-=-*-=- Bem vindo ao Bancaum -=-*-=-')
restante = 0
while True:
    reais = int(input('Quanto deseja sacar? '))
    c = reais // 50
    restante += reais % 50
    v = restante // 20
    restante = restante % 20
    ci = restante // 5
    restante = restante % 5
    u = restante // 1
    restante = restante % 1
    print(restante)
    break
print(f'Seu saque: {c} x R$ 50. {v} x R$ 20. {ci} x R$ 5. {u} x R$ 1.')