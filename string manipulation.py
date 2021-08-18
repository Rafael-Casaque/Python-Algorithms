a = 'teste'
b = 'TESTE'
c = '   teste   '
d = 15
e = 5
f = 'teste1 teste2 teste3 teste4 teste5'
maiuscula = a.upper() #transforma todo o conteúdo da variável em letras maiusculas
minuscula = b.lower() #transforma todo o conteúdo da variável em letras minusculas
primeira_letra = a.capitalize() #trnasforma a primeira letra em maiuscula
cortar_palavra = a[0:3] #corta a palavra com base nos indices informados 0 até 3 (2)
ultimas_letras = a[3:] #corta de tal indice até o final
troca = a.replace ('tes', 'be') #troca o primeiro termo informado pelo segundo
encontrar_string = a.find('s') #retorna em qual posição encontra o primeiro caractere informado (retorna -1 quando o caractere não existe)
remove_espaços = c.strip() #remove os espaços em branco
separar_palavras = f.split() #recorta as palavras e armazena em vetores
print(maiuscula)
print(minuscula)
print(primeira_letra)
print(cortar_palavra)
print(ultimas_letras)
print(troca)
print(encontrar_string)
print(len(a)) # retorna o tamanho da variável
print(remove_espaços)
print(separar_palavras)
print(separar_palavras[2]) #imprime o vetor desejado
# uso de váriaveis em print
print(f'Dividindo {d} por {e} o resultado é: {d/e}')

input('\n\nDigite qualquer tecla para encerrar o programa: ')




