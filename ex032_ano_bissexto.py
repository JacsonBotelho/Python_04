"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
quando vc digita 0 ele mostra o ano atual da máquina.
"""
from datetime import date
ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano=date.today().year
if ano % 4 == 0 and ano % 100!= 0 or ano % 400==0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} é não bissexto'.format(ano))