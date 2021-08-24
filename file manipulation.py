# Manipulação de arquivos 
with open('teste.txt') as text: 
    
    for linha in text:  #estrutura de repetição feita para percorrer as linhas do arquivo
       print(linha)

    #r = text.readlines() #armazena as linhas em índices
    #print(r)
with open('teste2.txt', 'w') as text2: #escreve o arquivo o 'w' é de write, por padrão vem 'r' de read
    text2.write('Ao vencedor as batatas') #escreve a string no arquivo
with open('teste2.txt') as text3:
    for linha in text3:  #estrutura de repetição feita para percorrer as linhas do arquivo
       print(linha)

alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}
aaa = {}
nome = {}

with open('teste3.txt', 'w') as text4:
    for value, key in alunos.items():
        text4.write(f'Nome: {value}, Nota: {key} ') 

input('\n\nDigite qualquer tecla para encerrar o programa: ')





    