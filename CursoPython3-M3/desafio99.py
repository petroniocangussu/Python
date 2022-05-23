#função maior(), receba vários parâmetros inteiros.
#programa deve dizer quantos valores e qual o maior.
def maior(* núm):
    from time import sleep
    print(f'-=-=-=-=-=-=-=-=- Analisando os números -=-=-=-=-=-=-=-=-')
    if (len(núm)) == 0:
        print('A sua sequência não possui números.')
    else:
        print(f'Recebi os valores {núm}, são ao todo {len(núm)} números. \nO maior destes números é {max(núm)} ')
    sleep(1)
#programa principal
maior(1, 3, 5, 7)
maior(123, 5, 4, 14)
maior(3, 6, 7, 15)
maior(2, 4)
maior(1)
maior()