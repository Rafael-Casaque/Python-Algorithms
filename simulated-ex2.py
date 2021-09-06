#Simulado - Ex 2

#Faça um programa que gere números aleatórios entre 88 e 298 (sem considerar o 88 nem o 298) até que um número divisível
#por 34 seja gerado. Quando isso ocorrer, informar:

#a- A média de todos os números divisíveis por 17 que foram gerados.
#b- O percentual de números pares entre 100 e 200 que foram gerados.
#c- A quantidade de números divisíveis por 7 e maiores que 183 que foram gerados.

import random

lista_numeros_aleatorios = []
lista_numeros_divisiveis_por_17 = []
filtrados = []

while True:
    numero_aleatorio = random.randint(88,298)
    lista_numeros_aleatorios.append(numero_aleatorio)
    if numero_aleatorio % 34 == 0:
        break

# parte a

    for i in range(0,len(lista_numeros_aleatorios)):
        if lista_numeros_aleatorios[i] % 17 == 0:
            lista_numeros_divisiveis_por_17.append(lista_numeros_aleatorios[i])
try:
    media = sum(lista_numeros_divisiveis_por_17)/len(lista_numeros_divisiveis_por_17)   #tratamento de erros, pois não pode haver divisão por 0
except ZeroDivisionError:
    media = 'Não há nenhum número divisível por 17'

# parte b

filtro = len([i for i in lista_numeros_aleatorios if i%2 == 0 and i > 100 and i < 200]) # filtrar quantidade de numeros maiores que x em uma lista
filtrados = [i for i in lista_numeros_aleatorios if i%2 == 0 and i > 100 and i < 200] # filtra e armazena os valores filtrados
percentual = filtro/len(lista_numeros_aleatorios)*100

# parte c 

filtro_parte_c = len([i for i in lista_numeros_aleatorios if i%7==0 and i>183])


print('A média dos números divisíveis por 17 é de: ',media)
print('A porcentagem de números pares gerados entre 100 e 200 é de: ',round(percentual,2),'%')
print('A quantidade de números divisíveis por 7 e maiores que 183 é: ',filtro_parte_c)
     
input('\n\nDigite qualquer tecla para encerrar o programa: ')
