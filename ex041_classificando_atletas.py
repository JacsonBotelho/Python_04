"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
"""
from datetime import date
atual=date.today().year
nasc=int(input('Ano de Nascimento: '))
idade=atual-nasc
print(f'O atleta nasceu {nasc} tem {idade} anos em {atual}')

if idade <= 9:
    print('Classificado: Mirim.')

elif idade <=14:
    print('Classificado: Infantil.')

elif idade <=19:
    print('Classificado: Júnior.')

elif idade <=25:
    print('Classificado: Sênior.')

else:
    print('Classificado: Mater.')