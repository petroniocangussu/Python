try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos problemas com os tipos de dados digitados')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
else: 
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
"""except Exception as erro:
    print('Infelizmente tivemos um problema :(')
    print(f'Problema encontrado foi {erro.__class__}')"""

#Desafios aula 23. Ex 113 -> modifique a função leiaint() incluindo possibilidades
#de digitação de número de tipo inválido. #Crie leiafloat() com a mesma função
#ex 114 -> código pra testar se o site pudim está acessível pelo computador.
#ex 115 -> utilize modulo para cadastrar pessoas pelo nome e idade em um arquivo
#de texto simples. Sistema terá duas opções, cadastrar uma pessoa e listar pessoas.