#Considere o cenário de lançamento de dados sobre óbitos por Covid19. Você deverá fazer um menu de opções no qual será possível:

#- lançar casos de óbito pela doença a cada dia. O usuário vai adicionando os dados dia a dia.

#- exibir os dados de óbitos de todos os dias

#- informar o dia em que houve a maior quantidade de mortes.

#- informar o dia em que houve a menor quantidade de mortes.

#- calcular a média móvel de óbitos nos últimos 7 dias. Caso haja menos de 7 dias lançados, avisar o usuário e informar a média dos dias disponíveis.

#- atualizar os dados de um dia: você deve pedir ao usuário qual dia ele quer atualizar. Imagine que o primeiro registro será o dia 1, o segundo será o dia 2 e assim por diante. Ex: se o usuário disser que quer atualizar os dados do dia 35 você deve informar ao usuário quantas mortes estão registradas neste dia e pedir a ele um novo valor. O usuário digita esse novo valor e a informação deste dia será atualizada.

#- verificar se a tendencia de óbitos é de aumento, diminuição ou estabilidade. Para isso você deve comparar a média móvel do último dia com a média móvel de 7 dias atrás. Se for maior que 15% significa aumento. Se ficar entre 15% e -15%, estabilidade. Do contrário (menor que      -15%) será diminuição.

#- zerar a lista com o lançamento dos dados

#- gerar dados aleatoriamente de mortes. Você deve perguntar para o usuário o total de dias que ele quer lançado, um valor mínimo e um valor máximo. Depois os lançamentos de óbitos devem ler lançados automaticamente no sistema.

import os,random

lista = []
a = 1
i = 1
soma = 0

while a == 1:
   print('\n----- menu de opções -----') 
   print('\n1 - Lançar casos de óbito.')
   print('2 - Exibir dados de óbitos diários.')
   print('3 - Exibir o dia com maior quantidade de óbitos.')
   print('4 - Exibir o dia com menor quantidade de óbitos.')
   print('5 - Exibir a média móvel de óbitos dos últimos 7 dias.')
   print('6 - Atualizar os dados de um determinado dia.')
   print('7 - Exibir a tendência dos óbitos.')
   print('8 - Zerar a base de dados.')
   print('9 - Gerar dados aleatórios.')
   print('0 - Finalizar o programa.')

   n = int(input('\n\nInforme a operação desejada: '))
   
   if n == 1:
       os.system('cls')
       lista.append(int(input(f'Digite a quantidade de óbitos do {i}º dia: ')))
       i += 1
       input('\n\nDigite qualquer tecla para retornar ao menu principal: ')
       os.system('cls')
   elif n == 2:
       os.system('cls')
       print('Quantidade de óbitos diários:')
       for j in range(0,len(lista)):
           print(f'\n{j+1}º dia - {lista[j]} óbitos')
       input('\n\nDigite qualquer tecla para retornar ao menu principal: ')
       os.system('cls')
   elif n == 3:
       os.system('cls')
       maior_qtd_obito = max(lista)
       pos_maior_qtd_obito = lista.index(maior_qtd_obito)
       print(f'O dia com maior quantidade de óbito é o {pos_maior_qtd_obito+1}º, tendo tido {max(lista)} óbitos')
       input('\n\nDigite qualquer tecla para retornar ao menu principal: ')
       os.system('cls')
   elif n == 4:
       os.system('cls')
       menor_qtd_obito = min(lista)
       pos_menor_qtd_obito = lista.index(menor_qtd_obito)
       print(f'O dia com maior quantidade de óbito é o {pos_menor_qtd_obito+1}º, tendo tido {min(lista)} óbitos')
       input('\n\nDigite qualquer tecla para retornar ao menu principal: ')
       os.system('cls')
   elif n == 5:
       os.system('cls')       
       if len(lista)<6:
           print('A quantidade de registros é menor que 7 dias')
           print(f'A média móvel de óbitos dos últimos {len(lista)} dias é de {sum(lista)/len(lista)} ')
       else:
           for j in range(len(lista)-1,len(lista)-8,-1):
               soma += lista[j]               
           print(f'A média móvel de óbitos dos últimos 7 dias é de {soma/7} ')
           soma = 0

       input('\n\nDigite qualquer tecla para retornar ao menu principal: ')
       os.system('cls')
   elif n == 6:
       os.system('cls')
       dia = int(input('Digite o dia em que você deseja atualizar os dados: '))
       lista[dia-1] = int(input('Digite o novo valor: '))
       
       input('\n\nDigite qualquer tecla para retornar ao menu principal: ')
       os.system('cls')
   elif n == 7:
#- verificar se a tendencia de óbitos é de aumento, diminuição ou estabilidade. Para isso você deve comparar a média móvel do último dia com a média móvel de 7 dias atrás. Se for maior que 15% significa aumento. Se ficar entre 15% e -15%, estabilidade. Do contrário (menor que      -15%) será diminuição.
       os.system('cls')
       for j in range(len(lista)-1,len(lista)-8,-1):
               soma += lista[j]
               media = soma/7
       if lista[-1]>media+media*0.15:
            print('\nComparando a média móvel do último dia, com a média móvel dos últimos 7 dias a tendência é de aumento.')
       elif lista[-1]<=media+media*0.15 and lista[-1]>=media+media*-0.15:
            print('\nComparando a média móvel do último dia, com a média móvel dos últimos 7 dias a tendência é de estabilidade.')
       elif lista[-1]<=media+media*-0.15:
            print('\nComparando a média móvel do último dia, com a média móvel dos últimos 7 dias a tendência é de dimuição.')        
       input('\n\nDigite qualquer tecla para retornar ao menu principal: ')
       os.system('cls')
   elif n == 8:
       os.system('cls')
       lista[:]=[]
       i=1
       input('\n\nDigite qualquer tecla para retornar ao menu principal: ')
       os.system('cls')
   elif n == 9:
       os.system('cls')
       qtd_dias = int(input('Digite a quantidade de dias que deseja preencher com dados aleatórios: '))
       minimo = int(input('Digite o valor mínimo de alcance de aleatoriedade: '))
       maximo = int(input('Digite o valor maximo de alcance de aleatoriedade: '))
       for j in range(0,qtd_dias):
           lista.append(random.randint(minimo,maximo))
       i = qtd_dias+1
       input('\n\nDigite qualquer tecla para retornar ao menu principal: ')
       os.system('cls')
   elif n == 0:
       a = 0
