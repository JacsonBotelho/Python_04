notas = []
cont = 0;
contAlunos = 0
while cont <= 10:
    soma = 0
    media = 0
    n1 = float(input('Informe o primeiro nota: '))
    n2 = float(input('Informe o segundo nota: '))
    n3 = float(input('Informe o terceiro nota: '))
    n4 = float(input('Informe o quarto quarta: '))
    soma = n1 + n2 + n3 + n4
    media = soma / 4
    print('------------------------------')
    if (media >= 7.0):
        notas.append(media)
        contAlunos += 1

    cont = cont + 1
print('Tem ', contAlunos, 'com média maior ou igual a 7.0.')
