# conjunto = {1,2,3,4}
# print(conjunto)
# print(type(conjunto))
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)

conjunto1= {1,2,3,4,5}
conjunto2= {5, 6, 7, 8}
conjunto_uniao = conjunto1.union(conjunto2)
conjunto_interseccao = conjunto1.intersection(conjunto2)
conjunto_diferenca1 = conjunto1.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto1)
conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)

print(conjunto1)
print(conjunto2)
print(f'União: {conjunto_uniao}')
print(f'Intresecção: {conjunto_interseccao}')
print(f'Diferença entre o primeiro e o segundo conjunto: {conjunto_diferenca1}')
print(f'Diferença entre o segundo e o primeiro conjunto: {conjunto_diferenca2}')
print(f'Diferença Simétrica entre o primeiro e o segundo conjunto: {conjunto_diff_simetrica}')

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)
conjunto_subset1 = conjunto_b.issubset(conjunto_a)
print(conjunto_subset1)
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)

lista = ['cachorro', 'gato', 'elefante']
conjunto_animais = set(lista)
print(conjunto_animais)

