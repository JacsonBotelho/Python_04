print('\033[4;33;41mAula de cores do terminal.\033[m')

a = 3
b = 5
print('Os valores são \033[4;31m{}\033[m e \033[4;31m{}\033[m'. format(a,b))

nome ='JACSON BOTELHO'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['azul'], nome, cores['limpa']))