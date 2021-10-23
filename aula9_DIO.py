# arquivo = open('teste.txt','w') #w para gerar um novo arquivo
# arquivo.write('Minha primeira escrita')
# arquivo.close()

# arquivo = open('teste.txt','a') #a para alterar um arquivo
# arquivo.write('\nTerceira Linha')
# arquivo.close()

def escrever_arquivo(texto):
    arquivo = open('teste.txt','w') #posso colocar o enderço onde quero criar o arquivo.Exemplo:
    arquivo.write(texto)            #c:/projeto/meus_arquivos/teste.txt
    arquivo.close()

def atualizar_arquivo(nome_arquivo,texto):
    arquivo = open(nome_arquivo,'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_nota = x.split(',')
        aluno = lista_nota[0]
        lista_nota.pop(0)
        print(aluno)
        print(lista_nota)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_nota))
        lista_media.append({aluno:media(lista_nota)})
        return lista_media

import shutil
def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/campo/Documents/Nova pasta/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/campo/Documents/Nova pasta/')

if __name__ == '__main__':
    move_arquivo('notas.txt')
    #copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    #escrever_arquivo('Primeira linha.\n')
    #atualizar_arquivo('teste.txt','Terceira linha.\n')
    # aluno = 'Cesar, 7, 9, 3, 8\n'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')