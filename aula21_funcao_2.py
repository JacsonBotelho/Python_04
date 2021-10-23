"""
Nessa aula, vamos continuar nossos estudos de funções em Python,
aprendendo mais sobre Interactive Help em Python, o uso de docstrings
para documentar nossas funções, argumentos opcionais para dar mais
dinamismo em funções Python, escopo de variáveis e retorno de resultados.
"""

help(print)
help(input)

def contador (i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return:  sem retorno
    """
    c = i
    while c<= f:
        print(f'{c} ', end='')
        c += p
    print('Fim!')

contador(0,100,10)
help(contador)

