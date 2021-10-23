"""
Nessa aula, vamos aprender como utilizar módulos em Python
utilizando os comandos import e from/import no Python.
Veja como carregar bibliotecas de funções e utilizar vários
recursos adicionais nos seus programas utilizando módulos
built-in e módulos externos, oferecidos no Pypi.
math:
ceil , floor, trunc, pow, sqrt, factorial
"""

import math
num=int(input('Digite um número: '))
raiz=math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num,raiz))


num=int(input('Digite um número: '))
raiz=math.sqrt(num)            #ceil faz o arredondamento para cima
print('A raiz de {} é igual a {:.2f}'.format(num,math.ceil(raiz)))

num=int(input('Digite um número: '))
raiz=math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num,math.floor(raiz)))

from math import sqrt  # importando a função sqrt(raiz quadrada)
num=int(input('Digite um número: '))
raiz=sqrt(num)
print('A raiz de {} é igual a {}'.format(num,math.ceil(raiz)))

from math import sqrt, floor  # importando a função sqrt(raiz quadrada)
num=int(input('Digite um número: '))
raiz=sqrt(num)                   #floor faz o arredondamento para baixo
print('A raiz de {} é igual a {:.2f}'.format(num,floor(raiz)))