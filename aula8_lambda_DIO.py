contador_letras = lambda lista: [len(x) for x in lista]

if __name__ == '__main__':
    lista_animais = ['cachorro', 'gato', 'pato']
    print(contador_letras(lista_animais))

soma = lambda a, b: a+b
print(soma(5,6))

calculadora = {
    'soma': lambda a,b:a+b,
    'Subtração': lambda a,b:a-b,
    'Multiplicação': lambda a,b:a*b,
    'Divisão': lambda a,b:a/b,
}
print(type(calculadora))

soma = calculadora['soma']
subtracao = calculadora['Subtração']
multiplicacao = calculadora['Multiplicação']
divisao = calculadora['Divisão']
print(soma(1,4))
print(multiplicacao(2,5))