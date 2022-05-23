#Leia uma frase
frase = str(input('Digite uma frase: ')).upper().strip()
#Quantas vezes aparece a letra "A"
print('A letra "A" aparece {} vezes nesta frase.'.format(frase.count('A')))

#Em que posição aparece pela primeira vez e pela última vez
print('A primeira letra "A" apareceu na posição {}.'.format(frase.find('A')+1))
print('A última letra "A" apareceu na posição {}.'.format(frase.rfind('A')+1))