#EX 14 Lista 2
#Faça um programa que gere números aleatórios entre 0 e 50 até o número 32 ser gerado. Quando isso ocorrer, informar: 

#a. A soma de todos os números gerados 

#b. A quantidade de números gerados que é impar 

#c. O menor número gerado
import random

lista =[]
lista_impares=[]

while True:
    numero_aleatorio = random.randint(0,50) # printa um número inteiro aleatório no intervalo de 0 a 50
    print(numero_aleatorio)
    lista.append(numero_aleatorio)
    if numero_aleatorio%2 ==1:
        lista_impares.append(numero_aleatorio)
    elif (numero_aleatorio == 32):
        break
print(f'\nA soma de todos os números gerados é: {sum(lista)}')
print(f'A quantidade de números ímpares gerados é: {len(lista_impares)}')
print(f'O menor número gerado é: {min(lista)}')
print(f'O maior número gerado é: {max(lista)}')

input('\nDigite qualquer tecla para fechar o programa: ')