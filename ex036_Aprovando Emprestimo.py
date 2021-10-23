"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""
casa=float(input('Valor da casa: R$'))
salario=float(input('Salário do comprador: R$'))
a=int(input('Quantos anos de financiamento? '))
p=casa/(a*12)
mSal=(salario*30)/100
print(f'Para pagar um casa de {casa} em {a} anos a prestação será de R${p:.2f}')

if p <= mSal:
    print('Emprestimo CONCEDIDO')
else:
    print('Emprestimo NEGADO')