"""
 Faça um programa que leia o peso de cinco pessoas.
 No final, mostre qual foi o maior e o menor peso lidos.
"""
maior=0
menor=0
for c in range(1,6):
    peso=float(input(f'O Peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'\nO maior peso lido é: {maior}')
print(f'O menor peso lido é: {menor}')