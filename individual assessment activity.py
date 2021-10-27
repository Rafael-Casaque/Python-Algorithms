import os

lista_filmes_cadastrados = []
lista_generos_cadastrados = []
lista_tempos_cadastrados = []
lista_notas_cadastradas = []

lista_notas_ordenadas = []
lista_filmes_ordenados = []
lista_generos_ordenados = []
lista_tempos_ordenados = []

def menu():
    os.system('cls')
    print("1 - Cadastrar filme")
    print("2 - Consultar todos os filmes cadastrados")
    print("3 - Atualizar informações de um filme")
    print("4 - Exluir filme do banco de dados")
    print("5 - Consultar filmes com base no gênero")
    print("6 - Consultar a média de duração dos filmes cadastrados")    
    print("7 - Consultar os filmes com base no ranking de avaliações")
    print("0 - Finalizar o programa")
    return

def cadastro(nome,genero,tempo,nota):
    lista_filmes_cadastrados.append(nome)
    lista_generos_cadastrados.append(genero)
    lista_tempos_cadastrados.append(tempo)
    lista_notas_cadastradas.append(nota)
    return print('O filme foi cadastrado com sucesso!')     
def validacao0(nome):
    if nome in lista_filmes_cadastrados:
        return print('Esse filme já existe na base de dados!')
    else:
        pass
def validacao(nome):
    if nome in lista_filmes_cadastrados:
        pass
    else:
        return print('Esse filme não existe na base de dados!')
def validacao2(genero):
    if genero in lista_generos_cadastrados:
        pass
    else:
        return print('Esse gênero não existe na base de dados!')
def exclusao(posicao):
    del lista_filmes_cadastrados[posicao]
    del lista_generos_cadastrados[posicao]
    del lista_tempos_cadastrados[posicao]
    del lista_notas_cadastradas[posicao]
    return print('O filme foi excluído com sucesso!')     
def atualizacao(nome,genero,tempo,nota,posicao):
    lista_filmes_cadastrados[posicao] = nome
    lista_generos_cadastrados[posicao] = genero
    lista_tempos_cadastrados[posicao] = tempo
    lista_notas_cadastradas[posicao] = nota
    return print('O filme foi atualizado com sucesso!')     
def media_duracao():
    soma = 0
    for i in range(len(lista_tempos_cadastrados)):
        soma += lista_tempos_cadastrados[i]
    media = soma/len(lista_tempos_cadastrados)
    return print('A média de tempo de duração dos filmes cadastrados é ',media)
def ranking_notas(lista_filmes_cadastrados,lista_generos_cadastrados,lista_tempos_cadastrados,lista_notas_cadastradas):

    for i in range(len(lista_filmes_cadastrados)):
        lista_notas_ordenadas.append(max(lista_notas_cadastradas))
        posicao = lista_notas_cadastradas.index(max(lista_notas_cadastradas))
        lista_filmes_ordenados.append(lista_filmes_cadastrados[posicao])
        lista_tempos_ordenados.append(lista_tempos_cadastrados[posicao])
        lista_generos_ordenados.append(lista_generos_cadastrados[posicao])
        lista_notas_cadastradas[posicao]=0
    return lista_filmes_ordenados,lista_generos_ordenados,lista_tempos_ordenados,lista_notas_ordenadas

while True:
    menu()
    i = str(input('Informe a opção desejada: '))

    if i =="1":
        nome = str(input('\nDigite o nome do filme: '))
        validacao0(nome)
        if nome not in lista_filmes_cadastrados:
            genero = str(input('Digite o gênero do filme: '))
            tempo = float(input('Digite o tempo de duração do filme: '))
            nota = float(input('Digite a nota de avaliação do filme: ')) 
            cadastro(nome,genero,tempo,nota)
        input('\ndigite qualquer tecla para retornar ao menu principal: ')
    elif i =="2":        
        for i in range(len(lista_filmes_cadastrados)):
            print(lista_filmes_cadastrados[i],lista_generos_cadastrados[i],lista_tempos_cadastrados[i],lista_notas_cadastradas[i])
        input('\ndigite qualquer tecla para retornar ao menu principal: ')
    elif i =="3":
        nome = str(input('\n\nDigite o nome do filme que deseja alterar: '))
        validacao(nome)
        if nome in lista_filmes_cadastrados:
            posicao = lista_filmes_cadastrados.index(nome)
            nome = str(input('\nDigite o nome atualizado do filme: '))
            genero = str(input('Digite o genero atualizado do filme: '))
            tempo = str(input('Digite o tempo atualizado do filme: '))
            nota = str(input('Digite a nota atualizada do filme: '))
            atualizacao(nome,genero,tempo,nota,posicao)            
        input('\ndigite qualquer tecla para retornar ao menu principal: ')
    elif i =="4":
        nome = str(input('\n\nDigite o nome do filme que deseja excluir: '))
        validacao(nome)
        if nome in lista_filmes_cadastrados:
            posicao = lista_filmes_cadastrados.index(nome)
            exclusao(posicao)
        input('\ndigite qualquer tecla para retornar ao menu principal: ')
    elif i =="5":
        genero = str(input('\nDigite o gênero desejado: '))
        validacao2(genero)
        if genero in lista_generos_cadastrados:
            for i in range(len(lista_generos_cadastrados)):
                if lista_generos_cadastrados[i] == genero:
                    print(lista_filmes_cadastrados[i],lista_generos_cadastrados[i],lista_tempos_cadastrados[i],lista_notas_cadastradas[i]) 
        input('\ndigite qualquer tecla para retornar ao menu principal: ')
    elif i =="6":        
        if len(lista_tempos_cadastrados) == 0:
            print('\nO banco de dados está vazio!')
        else:
            media_duracao()
        input('\ndigite qualquer tecla para retornar ao menu principal: ')
    elif i =="7": 
        ranking_notas(lista_filmes_cadastrados,lista_generos_cadastrados,lista_tempos_cadastrados,lista_notas_cadastradas)
        print('\n')
        for i in range(len(lista_filmes_ordenados)):
            print(lista_filmes_ordenados[i],lista_generos_ordenados[i],lista_tempos_ordenados[i],lista_notas_ordenadas[i])
        input('\ndigite qualquer tecla para retornar ao menu principal: ')
    elif i =="0":
        break

