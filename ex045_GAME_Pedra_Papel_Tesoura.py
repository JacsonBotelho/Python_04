"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""

print("""Suas opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA""")
jogador = int(input('Qual a sua jogada? '))

if jogador >2:
    print('JOGADA INVÁLIDA')

if jogador <=2:
    from random import randint
    from time import sleep
    itens = ('PEDRA','PAPEL','TESOURA')
    computador = randint(0,2)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    print('-='*11)
    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}')
    print('-='*11)

    if jogador ==0:
        if computador == 0:
            print('EMPATE')
        elif computador ==1:
            print('COMPUTADOR VENCE')
        elif computador ==2:
            print('JOGADOR VENCE')

    elif jogador == 1:
        if computador == 0:
            print('JOGADOR VENCE')
        elif computador ==1:
            print('EMPATE')
        elif computador ==2:
            print('COMPUTADOR VENCE')

    elif jogador == 2:
        if computador == 0:
            print('COMPUTADOR VENCE')
        elif computador ==1:
            print('JOGADOR VENCE')
        elif computador ==2:
            print('EMPATE')
