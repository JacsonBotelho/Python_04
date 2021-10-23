valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])

for p in galera:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'p[0]} é menor de idade')
        totmen +=1
print(f'Temos {totmai} maiores e {totalmen} menores de idade.')