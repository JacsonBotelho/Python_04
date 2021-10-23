"""
 Crie um programa que leia a idade e o sexo de várias pessoas.
 A cada pessoa cadastrada, o programa deverá perguntar se o usuário
 quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""
print('--'*15)
print ('   CADASTRE UMA PESSOA')
print('--'*15)
somaM = somaIdade = somaF =  0
while True:
    idade=int(input('Idade: '))
    sexo= ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >=18:
        somaIdade += 1
    if sexo == 'M':
        somaM += 1
    if sexo =='F' and idade < 20:
        somaF += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
    if op == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {somaIdade}')
print(f'Ao todo temos {somaM} homens cadastrados.')
print(f'Temos {somaF} mulheres menor de 20 anos.')


