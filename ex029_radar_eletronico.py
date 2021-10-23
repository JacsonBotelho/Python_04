"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""

v = float(input('Qual a velocidade atual do carro? '))

if v > 80:
    m=(v-80)*7
    print('Multado! Você exedeu o limite permitido que é 80km/h.')
    print('Você vai pagar uma multa de {:.2f}'.format(m))
print('Tenha um bom dia! Dirija com segurança!')