"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
ANOTARAM A DATA DA MARATONA.
"""
"""
frase=str(input('Digite uma frase: ')).strip().upper()
palavras =frase.split()
junto = ''.join(palavras)
inverso = junto [::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!!')
else:
    print('A frase digitada não é um palíndromo!')
"""
frase=str(input('Digite uma frase: ')).strip().upper()
palavras =frase.split()
print(palavras)
junto = ''.join(palavras)
print(junto)
inverso = ''
print(inverso)
for letra in range(len(junto)-1,-1, -1):
    inverso+= junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!!')
else:
    print('A frase digitada não é um palíndromo!')
