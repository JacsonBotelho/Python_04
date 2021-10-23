lista = [12,10,7,5]
lista_animal = ['cachorro', 'gato', 'elefante', 'arara', 'jacaré']

lista.sort()
lista_animal.sort()

print(lista)
print(lista_animal)
lista_animal.reverse()
print(lista_animal)
print(lista_animal[1])

# for x in lista_animal:
#     print(x)
#
# soma = 0
#
# for x in lista:
#     print(x)
#     soma+= x
#
# print(soma)

# print(sum(lista))
# print(max(lista))
# print(min(lista))
# print(max(lista_animal))
#
#
# if 'gato' in lista_animal:
#     print('existe um gato na lista')
# else:
#     print('não existe um gato na lista')
#
# lista_animal.append('lobo')
#
# print(lista_animal)
#
# lista_animal.pop(1)
# print(lista_animal)
#
# lista_animal.remove('elefante')
# print(lista_animal)

tupla = (1, 10, 12, 14)
print(tupla) #vc não consegue fazer alteração nas tuplas
print(len(tupla)) #Conta quantos elementos consta na tupla
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)
