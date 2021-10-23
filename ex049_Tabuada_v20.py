"""
Refaça o DESAFIO 9, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.
"""

numero=int(input('Digite qual tabuada deseja fazer: '))

for i in range(1,11):
    print(f'{numero} x {i:2} = {numero*i}')
