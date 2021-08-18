# Lista de exercícios 1

import os

print('Olá, bem vindo à lista de exercícios de lógica de programação do Professor André')

i = 0
while i<1:
    resposta_inicial = (input("\nDigite 'sim' para ir ao promeiro exercício e 'não' para fechar o programa: "))
    if (resposta_inicial == 'sim' or resposta_inicial == 'SIM'):
        i = 2
        os.system("cls")
    elif (resposta_inicial == 'não' or resposta_inicial == 'NÃO'):
        exit()

#Programação do Exercício 1

print('Eercício 1')
print('____________')
numero = [0]*2
numero [0] = float(input('Digite um número: '))
numero [1] = float(input('Digite outro número: '))
if (numero[0]>numero[1]):
    print(f'O número {numero[0]} é maior que o número {numero[1]}')    
elif(numero[1]>numero[0]):
    print(f'O número {numero[1]} é maior que o número {numero[0]}')
else:
    print('Os números têm o mesmo valor!')

i = 0
while i<1:
    resposta_inicial = (input("\nDeseja continuar? 'sim' para ir ao promeiro exercício e 'não' para fechar o programa: "))
    if (resposta_inicial == 'sim' or resposta_inicial == 'SIM'):
        i = 2
        os.system("cls")
    elif (resposta_inicial == 'não' or resposta_inicial == 'NÃO'):
        exit()

#Programação do Exercício 2

print('Eercício 2')
print('____________')
numero = [0]*3
numero [0] = float(input('Digite um número: '))
numero [1] = float(input('Digite outro número: '))
numero [2] = float(input('Digite outro número: '))
maior = max(numero[0:3])
if (numero[0]==numero[1] and numero[0]==numero[2]):
    print('Todos os números são iguais!')
else:
    print (f"o maior valor é: {maior}")


i = 0
while i<1:
    resposta_inicial = (input("\nDeseja continuar? 'sim' para ir ao promeiro exercício e 'não' para fechar o programa: "))
    if (resposta_inicial == 'sim' or resposta_inicial == 'SIM'):
        i = 2
        os.system("cls")
    elif (resposta_inicial == 'não' or resposta_inicial == 'NÃO'):
        exit()

#Programação do Exercício 3

print('Eercício 3')
print('____________')
numero = [0]*5
numero [0] = float(input('Digite um número: '))
numero [1] = float(input('Digite outro número: '))
numero [2] = float(input('Digite outro número: '))
numero [3] = float(input('Digite outro número: '))
numero [4] = float(input('Digite outro número: '))

j=0

filtro = [x for x in numero if x > 10] # o laço de repetição percorre todos os indices e o if seleciona os indices maiores que 10

print(f'Os números {filtro} são maiores que 10')

i = 0
while i<1:
    resposta_inicial = (input("\nDeseja continuar? 'sim' para ir ao promeiro exercício e 'não' para fechar o programa: "))
    if (resposta_inicial == 'sim' or resposta_inicial == 'SIM'):
        i = 2
        os.system("cls")
    elif (resposta_inicial == 'não' or resposta_inicial == 'NÃO'):
        exit()

# Programação exercício 4

print('Eercício 4')
print('____________')
nota_prova = float(input('Digite a nota da prova: '))
nota_trabalho = float(input('Digite a nota do trabalho: '))
frequencia = float(input('Digite a frequência de 0 a 100: '))

nota_final = nota_prova*0.7+nota_trabalho*0.3

if (nota_final>=6 and frequencia>=75):
    print(f'Aprovado! Com nota final {nota_final} e frequência {frequencia}')
elif (nota_final>=4 and nota_final<6 and frequencia>=75):
    print(f'Em Recuperação! Com nota final {nota_final} e frequência {frequencia}')
elif (nota_final<4 and frequencia<75):
    print(f'Reprovado! Com nota final {nota_final} e frequência {frequencia}')

i = 0

input('O questionário acabou, digite qualquer tecla para fechar o programa: ')

# Programação exercício 5






