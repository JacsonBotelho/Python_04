
num = [2, 5, 9, 1]
num[2]=3
num.append(7)
num.sort(reverse=True)
num.insert(2,0)
num.pop(2)
print(num)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(f'Essa lista tem {len(num)} elementos')
print('\n',num)

print()
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...', end = '')
print()
for c, v in enumerate(valores):
       print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')
