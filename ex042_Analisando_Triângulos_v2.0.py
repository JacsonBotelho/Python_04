"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
"""
print('-='*20)
print('Analisadar de Triangulos')
print('-='*20)
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triângulo!')
    if r1 == r2 == r3:
        print('EQUILÁTERO:todos os lados iguais')
    if r1 != r2 != r3 != r1:
        print('ESCALENO: dois lados iguais, um diferente')
    else:
        print('ISÓSCELES: dois lados iguais, um diferente')
else:
    print('Os segmentos acima não podem formar triângulo!')