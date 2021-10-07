import pandas as pd                                     #faz a importação do pandas e o define como 'pd'

with open('teste.csv','w',encoding='utf-8') as teste:   #faz a criação do arquivo csv
    teste.write('nome,idade,sexo')                      #adiciona as colunas referenciais
    teste.write('\nana,18,feminino')                    #adiciona os registros
    teste.write('\nbeatriz,17,feminino')                #adiciona os registros
    teste.write('\ncaio,16,masculino')                  #adiciona os registros
    teste.write('\ndaniel,20,masculino')                #adiciona os registros

teste_db = pd.read_csv('teste.csv')                     #cria a variável de manipulação de csv do pandas
print(teste_db)                                         #printa a base de dados criada
teste_db.loc[teste_db['nome']=='ana','idade'] = 16      #localiza a coluna que tem o nome ana e muda sua idade para 16
lista = []                                              #cria variável de lista
delimitador = teste_db.shape                            #cria um delimitador com base no tamanho da base de dados
for i in range(0,delimitador[0]):                       #iteração onde o range é de 0 até a quantidade de linhas
        lista.append(f'{teste_db.iloc[i,0]},{teste_db.iloc[i,1]},{teste_db.iloc[i,2]}') #adiciona registro a registro na lista  

with open('teste.csv','w',encoding='utf-8') as teste:   #sobrescreve o arquivo csv criado anteriormente
    teste.write('nome,idade,sexo')                      #reescreve as coluans referenciais
    for i in range(0,len(lista)):                       #iteração onde o range é de 0 até 0 último registro da lista
        teste.write(f'\n{lista[i]}')                    #escreve cada posição da lista
print(teste_db)                                         #printa a base de dados modificada
print(teste_db['idade'].mean())                         #printa a média das idades
print(teste_db['idade'].min())                          #printaa menor idade
print(teste_db.loc[teste_db['idade']==teste_db['idade'].min()]) #printa o nome da pessoa mais nova
print(teste_db.loc[teste_db['sexo']=='feminino','idade'].mean()) #retorna a média das idades apenas de pessoas com sexo feminino