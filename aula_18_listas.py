teste=[]
teste.append('Gustavo')
teste.append(40)
print(teste)
galera=[]
galera.append(teste[:])
teste[0]='Maria'
teste[1]=30
print()
print(teste)
print(galera)

turma=[['João',40],['Maria',33],['Clara',22],['José',33]]
for p in turma:
    print(p[0])

for p in turma:
    print(p[1])

for p in turma:
    print(f'{p[0]} tem {p[1]} anos de idade.')

lista=[]
dado=[]
totmai = totmen = 0

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    lista.append(dado[:])
    dado.clear() #excluindo lista

for p in lista:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade.')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen +=1

print(f' Temos {totmai} maiores e {totmen} menores de idade.')