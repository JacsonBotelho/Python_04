"""
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais
"""
num1=float(input('Primeiro numero: '))
num2=float(input('Segundo numero: '))

if num1 > num2:
    print('O primeiro valor é maior')

if num1 < num2:
    print('O segundo valor é maior')

if num1==num2:
    print('Não existe valor maior, os dois são iguais')