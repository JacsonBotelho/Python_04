"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome
do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
media=0
nomeVelho = ''
maioridadehomem = 0
somaidade=0
totalMulher = 0
for c in range(1,5):
    print(f"--- {c}ª{(' Pessoa ---'):<20}")
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in'Mm':
        maioridadehomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher += 1
media=somaidade/4
print(f'A Média de idade do grupo é: {media:.2f}')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomeVelho}. ')
print(f'Tem {totalMulher} com idade abaixo de 20 anos.')
