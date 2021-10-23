"""
Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
"""
soma = 0
cont = 0
for i in range(0,7):
    numero=int(input('Digite um número: '))
    if  numero % 2 == 0:
        soma += numero
        cont += 1
print(f'Foram encontrados {cont} números pares. A soma dos números pares é:{soma}')