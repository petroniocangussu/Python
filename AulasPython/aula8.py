import math
import random
import emoji

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'. format(num, raiz))

al = random.randint(1, 10)
print(al)

print(emoji.emojize("Olá, Mundo :earth_americas:", use_aliases=True))