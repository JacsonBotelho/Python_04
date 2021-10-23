"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
"""
nome = str(input('Digite o nome: '))
alt = float(input('Qual é a sua altura (m): '))
peso = float(input('Qual é o seu peso (kg): '))
IMC = (peso/(alt**2))
print(f'O IMC é de:{IMC:.2f}')

if IMC < 18.50:
    print('Vc está ABAIXO do Peso Normal')
elif 18.5 <= IMC < 25:
    print('Parabéns vc está na faixa de Peso Normal')
elif 25 <= IMC <= 30:
    print('Vc está em SOBREPESO')
elif 30 <= IMC <= 40:
    print('Vc está em OBESIDADE!')
elif IMC >= 40:
    print('Vc está em OBESIDADE MÓRBIDA, cuidado!')

