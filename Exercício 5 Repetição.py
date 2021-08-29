#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
#Faça um programa que gere a série até que o valor seja maior que 500.

import time
n = 500
anterior = 0
proximo = 0
inicio_while = time.time()
while True:
    print(proximo, end=' ')
    proximo = proximo + anterior
    anterior = proximo - anterior
    if(proximo == 0):
        proximo = proximo + 1
    elif proximo>n:
        break

input('\n\nDigite qualquer tecla para encerrar o programa: ')
