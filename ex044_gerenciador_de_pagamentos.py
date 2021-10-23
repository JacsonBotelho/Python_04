"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
"""

print(f"{(' LOJAS GUANABARA '):=^40}")

preço = float(input('Preço das compras: R$'))
print("""FORMAS DE PAGAMENTO
      [1] à vista dinheiro/cheque
      [2] à vista cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão""")
op=int(input('Qual é a opção: '))

if op == 1:
    desc = (preço * 10)/100
    print(f'Sua compra à vista dinheiro/cheque de R${preço:.2f}, tem 10% de desconto R${desc:.2f}')
    print(f'Valor a ser pago: R${preço-desc:.2f}')

elif op == 2:
    desc = (preço * 5) / 100
    print(f'Sua compra à vista no cartão de R${preço:.2f}, tem 5% de desconto R${desc:.2f}')
    print(f'Valor a ser pago: R${preço - desc:.2f}')

elif op == 3:
    valor = preço / 2
    print(f'Sua compra de R${preço:.2f} será parcelada em 2x de R${valor:.2f}')
    print(f'Valor total da compra: R${preço:.2f}')

elif op == 4:
    parcela = int(input('Digite o número de parcelas: '))
    valor = preço+((preço*20)/100)
    print(f'Sua compra de R${preço:.2f}, será parcelada em {parcela:.2f}x de R${valor/parcela:.2f}')
    print(f'Valor total da compra: R${valor:.2f}')
else:
    print(f'Forma de Pagamento Inválida, sua compra é de R$ {preço:.2f}')