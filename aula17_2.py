teste = list()
teste.append('Jacson')
teste.append(45)
galera = list()
galera.append(teste[:])
teste[0] = 'Botelho'
teste[1] = 25
galera.append(teste[:])

print(galera)
print()
galera = [['joão', 19],['ana', 33],['joaquim', 13],['maria',45]]
print(galera)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print()
print(f'Temos {totmai} maiores e {totmen} menores de idade')
print(galera)
