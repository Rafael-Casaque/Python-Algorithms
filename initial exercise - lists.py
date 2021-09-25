#Faça um programa que pergunte ao usuário o número de elementos de uma lista A e popule essa lista com números inteiros. 
#Os números digitados pelo usuário precisam ser entre 1 e 10.

#Depois popule uma lista B com o dobro de elementos da lista A. Esses números devem ser gerados randomicamente. 

#Depois informe:

#- a média dos valores da lista A

#- o maior valor das duas listas

#- informe se existem valores na lista A que também estão na lista B. Se existirem valores, coloque em uma lista C e a exiba.

#- informe qual a média de valores é maior, da lista A ou da lista B.
import random

lista_a = []
lista_b = []
lista_c = []

n = int(input('Informe o número de elementos que deseja para a lista A: '))

for i in range(1,n+1):
    while  True:
        numero = int(input(f'\nDigite o {i}º número: '))
        if numero>=1 and numero<=10:
            lista_a.append(numero)
            break       
        else:
            print('\nSó são aceitos números entre 1 e 10')

while len(lista_b)<n*2:
    lista_b.append(random.randrange(0,10))

print('\n\nA média dos valores contidos na lista a é: ',sum(lista_a)/len(lista_a))
print(f'O maior valor da lista a é: {max(lista_a)} e o maior valor da lista b é: {max(lista_b)}')
    
lista_c = list(set(lista_a).intersection(lista_b))

if len(lista_c) == 0:
    print('Não há elementos comuns entre a lista a e b')
else:
    print(f'Os elementos comuns entre as listas a e b são: {lista_c}')

if sum(lista_a)/len(lista_a)>sum(lista_b)/len(lista_b):
    print('A média de valores da lista a é maior do que da lista b')
elif sum(lista_b)/len(lista_b)>sum(lista_a)/len(lista_a):
    print('A média de valores da lista b é maior do que da lista a')
else:
    print('A média de ambas é igual')

# métodos para buscar a intersecção entre listas

# comuns = list(set(list1) & set(list2) & set(list3))

#list(set(list1).intersection(list2).intersection(list3))