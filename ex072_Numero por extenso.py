"""
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo
por extenso.
"""
lista=('Zero','Um','Dois','Três','Quatro',
       'Cinco','Seis','Sete','Oito','Nove',
       'Dez','Onze','Doze','Treze','Catorze',
       'Quinze','Dezesseis','Dezessete','Dezoito',
       'Dezenove','Vinte')
while True:
    numero=(int(input('Digite um número de 0 a 20: ')))
    if 0 <= numero <=20:
        print(f'O numero escolhido foi {lista[numero]}')
        resp = ' '
        if resp not in 'SN':
            resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if resp == 'N':
                break
    else:
        print('Tente Novamente. ', end='')


