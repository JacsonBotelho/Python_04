"""
Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar
dicionários em Python. Os dicionários são variáveis compostas
que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves literais. """

pessoas = {'Nome': 'Gustavo','Sexo': 'M', 'Idade':22}
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['Sexo']
pessoas['Nome'] = 'Leandro'
pessoas['Peso'] = 98.5
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
brasil=[]
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ' }
estado2 = {'uf': 'São Paulo', 'sigla': 'SP' }

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[1])
print()
print(brasil[0]['sigla'])