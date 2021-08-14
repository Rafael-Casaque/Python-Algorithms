#meuvetor = []
#print(dir(meuvetor)) #verifica todos os métodos de uma classe, no caso "meuvetor"

import random

#tam = int(input())

qn = int(input('Digite a quantidade de avaliações: '))
notas = [0]*qn
for i in range(qn):
    notas[i] = float(input('Digite a nota: '))

somanotas = 0
somanotas = sum(notas)
media=somanotas/qn

if (media>=6):
    print('Você está aprovado :)')
else:
    print('Você está reprovado :(')
input('\n\nDigite qualquer tecla para encerrar o programa: ')

