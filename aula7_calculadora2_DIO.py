
class Calculadora:
    def __init__(self):
        pass

    def soma (self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao (self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

calculadora = Calculadora()
print(calculadora.soma(10, 2))
print(calculadora.subtracao(44,10))
print(calculadora.multiplicacao(5,5))