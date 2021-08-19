# estudo de funções

# funções são trechos de programas que podem ser reutilizadas sendo chamadas

#___________________________________
#Função sem parâmetro e sem retorno
#___________________________________
def funcao1(): #declara uma função
    print('Essa é a função 1') #tudo após a identação pertence à função 
funcao1() #chamada de função
#___________________________________
#Função com passagem de parâmetro
#___________________________________
def funcao2(string): #define a variável string como sendo o parametro da função
    print(string)
funcao2('Essa é a função 2') #atribui o valor ao parâmetro
def funcao3(numero1,numero2): #define as variáveis n1 e n2 como parâmetros
    print(f'a soma dos parâmetros da função3 é {numero1+numero2}')
funcao3(10,15)
#___________________________________
#Função com passagem de parâmetro e retorno
#___________________________________
def funcao4(numero3,numero4):
    return numero3 + numero4    #retorna para a função apenas o resultado
resultado = funcao4(5,15)       #armazena o retorno da função dentro da variável

print(f'a soma dos parâmetros da função4 é {resultado}')

import math
def funcao5(cat1,cat2):
    '''
    Calcula o valor da Hipotenusa, tendo como parâmetros, os valores dos catetos 
    ''' #maneira de inserir descrição na fução
    hip = cat1**2 + cat2**2
    return math.sqrt(hip)

print(f'A hipotenusa do cateto 30 e 40 é {funcao5(30,40)}')

help(funcao5) # chama a descrição da função, importante para documentar