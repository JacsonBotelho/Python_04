def soma(a,b):
    print(f'A = {a} e B = {b}')
    s=a+b
    print(f'A soma A + B = {s}')

# Programa Principal


soma(b=4,a=5)
soma(8,9)
soma(2,1)

def contador(*núm):
    print(núm)
    for valor in núm:
        print(f'{valor}', end=' ')
    print('FIM!')
    #tam = len(núm)
    #print(f'Recebi os valores {núm} e são ao todo {tam} números')



contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)