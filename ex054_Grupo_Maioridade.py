"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date
atual= date.today().year
totmaior=0
totmenor=0
for i in range(1,8):
    nasc=int(input(f'Em que ano a {i}ª pessoa nasceu: '))
    idade = atual - nasc
    if idade >=21:
        totmaior+= 1
    else:
        totmenor+= 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'Ao todo tivemos {totmenor} pessoas maiores de idade')



