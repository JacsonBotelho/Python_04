"""
Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar
dicionários em Python. Os dicionários são variáveis compostas
que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves literais. """

estado =dict()
brasil = list()
for c in range (0,3):
    estado ['uf'] = str (input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)

for e in brasil:
    for k, v in estado.items():
        print(f'O Campo {k} tem valor {v}')

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()