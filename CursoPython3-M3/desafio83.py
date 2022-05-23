#digite uma expressão que use parênteses. Deve analisar se os parênteses
#estão abertos e fechados na ordem correta.
expr = str(input('Digite uma expressão:'))
pilha = []
for símbolo in expr:
    if símbolo == '(':
        pilha.append('(')
    elif símbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada.')

#exp = str(input('Digite uma expressão: '))
#print('A expressão está correta!' if exp.count('(') == exp.count(')') else 'A expressão está errada')