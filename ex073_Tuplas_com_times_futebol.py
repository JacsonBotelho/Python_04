"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""

times=('Corinthians','Palmeiras','Santos','Vasco',
       'Flamengo','Grêmio','Cruzeiro','Internacional',
       'Fluminense','Atlético', 'Atlético-GO','Atlético-PR',
       'Avaí','Bahia','Ponte Preta', 'Sport Recife','São Paulo',
       'EC Vitória', 'Chapecoense','Curitiba')


print('-='*40)
print(f'Lista de times do Brasileirão: {times}')

print('-='*40)
print(f'Os 5 primeiros são: {times[:5]}')

print('-='*40)
print(f'Os 4 últimos são: {times[16:]}')

print('-='*40)
print(f'Times por ordem alfabética: {sorted(times)}')

print('-='*40)
print(f'O Chapecoense está na: {times.index("Chapecoense")+1}ª posição')
