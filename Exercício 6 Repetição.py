#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
#usuário. Ex.: 5!=5.4.3.2.1=120

import math #importa a biblioteca math

n = int(input('Digite um número inteiro para ser calculado seu fatorial: '))
print(f"\nO fatorial de {n} é: ",math.factorial(n)," calculado a partir da biblioteca math") #função para retornar a fatorial

#calcular do zero, sem a biblioteca math
fatorial = 1
for i in range (1,n+1):
    fatorial = fatorial*i
print(f"O fatorial de {n} é: ",fatorial," calculado do zero")
input('\n\nDigite qualquer tecla para encerrar o programa: ')
    
    

