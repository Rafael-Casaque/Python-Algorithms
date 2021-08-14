# some todos os números ímpares que são múltiplos de três e que estão no conjunto de números de 1 a 100
# add up all the odd numbers that are multiples of three and that are in the set of numbers from 1 to 100

# estrutura de repetição for
print('Lista de todos os divisores por 3 de 0 a 100:\n')
for num in range(0,101):
    if num % 3 == 0:
       print(num, end=' ')
print('\n\n\n\n\nLista de todos os divisores por 5 de 0 a 100:\n')

# estrutura de repetição while
i = 0
while i<101:
    if i % 5 == 0:
       print (i, end=' ')
    i=i+1
j=0

# estrutura de repetição =~ do while

print('\n\n\n\n\nLista de todos os divisores por 5 de 0 a 100:\n')
while True:
   if j % 7 == 0:
    print(j, end=' ')
   j = j+1
   if not j<101:
        break

input('\n\nDigite qualquer tecla para encerrar o programa: ')

print('Teste')