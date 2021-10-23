from aula7_televisao_DIO import Televisao
from aula07_calculadora1_DIO import Calculadora

if __name__ == 'main':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora  = Calculadora(10,2)
    print(calculadora.soma())