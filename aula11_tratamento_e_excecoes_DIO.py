lista = [1,10]
arquivo = open('teste.txt','r')
try:
    texto = arquivo.read()
    divisao = 10/0
    numero = lista[1]
    #x = a
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except IndexError:
    print('Erro ao acessar um indece inválido da lista')
except BaseException as ex:
    print(f'Erro desconhecido. Erro: {ex}')
else:
    print('Execulte quando não ocorrer excessão')
finally:
    print('sempre execulta')
    print('fechando arquivo')
    arquivo.close()