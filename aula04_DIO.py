# for x in range(101):
#     print(x)4

# a = int(input('Entre com o número: '))
#
# div = 0
# for x in range (1, a+1):
#     resto = a % x
#     print(a,resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print(f'número {a} é primo.')
# else:
#     print(f'número {a} não é primo.')




# for num in range (101):
#     div = 0
#     for x in range(1,num+1):
#         resto =num % x
#         print(x,resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(f'número {num} é primo.')

# a = int(input('Entre com um valor: '))
# for num in range (a+1):
#     div = 0
#     for x in range(1,num+1):
#         resto =num % x
#         print(x,resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(f'número {num} é primo.')

# a = 0
# while a < 10:
#     print(a)
#     a+=1

nota = int(input('Entre com a primeira nota: '))
while nota > 10:
    nota = int(input('Nota inválida. Entre com a nota correta: '))
print(f'Nota: {nota}')

nota1 = int(input('Entre com a segunda nota: '))
while nota1 > 10:
    nota1 = int(input('Nota inválida. Entre com a nota correta: '))
print(f'Nota: {nota1}')

média = (nota+nota1)/2
print(f'A média é {média}')