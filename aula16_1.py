"Aula de Tuplas"
lanche = ('Hamburguer','Suco','Pizza','Pudim','Batata Frita')

for cont in range (0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')

# (enumerate - enumera posição)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição - {pos}')

#Colocar a tupla em ordem

print(sorted(lanche))