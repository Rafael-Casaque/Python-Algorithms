#Estudos de Coleções

#tuplas:

tupla = ('teste', 'teste1', 'teste2') # variável com multilpas informações =~vetor
print(tupla[0]) # printa o conteúdo do indice informado
print(tupla[1])
print(tupla[2])
print(tupla.index('teste2')) # retorna o indice do conteúdo informado

for descrever in tupla: #printa todos os indices da variável
    print(descrever)

#listas:

lista1 = ['teste1-1', 'teste1-2', 'teste1-3', ]
lista2 = ['teste2-1', 'teste2-2', 'teste2-3', ]

lista3 = lista1+lista2
lista2_2 = lista2*2
print(lista3)
print(lista2_2)
print(lista1[0:2])
lista1.append('teste1-4') #adiciona um conteúdo à lista
print(lista1)
lista1.remove('teste1-4') #remove um conteúdo da lista
print(lista1)
del(lista1) #deleta alista
#print(lista1) #gera um erro pois a variavél não existe

for listagem in lista2_2: #faz a listagem, indice por indice
    print(listagem)

#dicionários: são usados pra guardar nome e valor

dicionario1 = {'um':1, 'dois': 2, 'três': 3}
dicionario2 = {'seis':6, 'sete': 7, 'oito': 8}
print(dicionario1['um']) #retorna o número que acompanha determinada chave
dicionario1['quatro']=4 #adiciona a chave e o valor
del(dicionario1)['um'] #remove um ítem por meio da chave
chaves = dicionario1.keys() #trás somente as chaves
valores = dicionario1.values() #trás somente os valores
print(chaves)
print(valores)
print(dicionario1)
dicionario1.update(dicionario2) #adiciona os itens dao dicionario2 ao dicionario1
print(dicionario1)
print(dicionario1.items()) #exibe todas as chaves e todos os valores

for key, value in dicionario1.items():  #estrutura de repetição para exibir chave e valor
    print(key,'  ',value) 

#conjuntos:

conjunto1 =('um','dois','três','quatro','um','um','um','um','dois','dois','três','três')
print(set(conjunto1)) #exibe apenas os índices que não se repetem
conjunto2 = {1,2,3,4,5}
conjunto3 = {6,5,7,2,1}
conjunto_interseccao = conjunto2.intersection(conjunto3) #exibe os valores que estão na intersecção dos conjuntos
print(conjunto_interseccao)
conjunto_diferenca = conjunto2.difference(conjunto3) #exibe os valores que estão no conjunto2 mas não no conjunto3
print(conjunto_diferenca)
conjunto_diferenca2 = conjunto3.difference(conjunto2) #exibe os valores que estão no conjunto3 mas não no conjunto2
print(conjunto_diferenca2)

input('Digite qualquer tecla para fechar o programa: ')

#estudo de matrizes

import numpy as np #importa a biblioteca e apelida ela, toda vez que precisar é só usar o np
# velocidade de processamento é mais rapido com essa estrutura de dados
matriz1 = np.array([[2,3,1],[4,5,6]])

# nessa estrutura a matriz fica com 2 linhas e 3 colunas, da seguinte forma:

          #c0,c1,c2
#linha0     2,3,1
#linha1     4,5,6

print(matriz1)
print(matriz1.shape) # exibe quantidade de (linhas, colunas)
print(matriz1[0]) #printa os elementos da linha 0
print(matriz1[0][1]) #printa o elemento da linha 0 e coluna 1

for i in range(matriz1.shape[0]):
    #print(matriz1[i])   # printa todos as linhas
    for j in range(matriz1.shape[1]): 
        print(matriz1[i][j]) # printa os elementos individualmente, termina os elementos da linha 0, depois vai pros elementos da linha 1
        
for i in range(matriz1.shape[0]):
    print(matriz1[i][0]) # exibe os elementos individualmente da coluna 0

input('\n\nDigite qualquer tecla para encerrar o programa: ')