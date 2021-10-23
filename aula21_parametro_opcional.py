"""
Nessa aula, vamos continuar nossos estudos de funções em Python,
aprendendo mais sobre Interactive Help em Python, o uso de docstrings
para documentar nossas funções, argumentos opcionais para dar mais
dinamismo em funções Python, escopo de variáveis e retorno de resultados.
"""

def somar (a=0,b=0,c=0):
    s=a+b+c
    print(f'A soma vale {s}')

somar(2,3)
