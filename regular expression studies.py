# Expressões Regulares

# Técnica para fazer busca sofisticada por padrões

# Exemplo1: Procurar apenas palavras que começam com 'a' e terminam com 'e'
# Exemplo2: Procurar e-mails, telefones, cep´s

# Método Search: Usado para encontrar as posições de padrões dentro de uma string
# Método Match: Usado para encontrar se o começo de uma string faz parte de um determinado padrão
# Método Findall: Usado para encontrar todas as substrings em uma string que correspondam a um padrão  

#Metacaracteres: 

# '.' indica qualquer caractere (exceto nova linha)
# '\w' indica qualquer caractere alfanumérico
# '\W' indica qualquer caractere não-alfanumérico
# '\d' indica qualquer caractere que seja um dígito (0,9)
# '\D' indica qualquer caractere que não seja um dígito 
# '\s' indica qualquer espaço em branco
# '^' indica qualquer palavra que começa com... ex: ^a
# '$' indica qualquer palavra que termina com... ex: $a
# '\' usados antes de metacaracteres para especificar seu sentido literal ex: '\.' encontrar os pontos 

#Quantificadores

#'[]' indica um padrão opcional ex: [a,b] - pode ter a ou pode ter b e se não tiver a e b, também vai seguir
#'()' captura um grupo de caracteres
#'*' indica que o determinado caracter pode aparecer de zero a mais vezes 
#'?' indica que o determinado caractere pode aparecer de zero a apenas uma vez
#'+' indica que o determinado caractere deve aparecer se uma a mais vezes 
#'{m,n}' indica que o determinado caractere deve aparecer de m a n vezes  

import re

#Função Search = procura a primeira ocorrência de uma expressão regular

frase1 = 'Aqui é do bom dia & cia, nosso número é (11)4002-8922'
frase2 = 'A placa do carro que comprei é ABC-1234' 
frase3 = 'Fico à disposição nomeusuario@hotmail.com nomeusuario@hotmail.br nomeusuario@hotmail.net '
frase4 = 'usuariosos@gmail.com'
frase5 = 'telefone padrao são paulo é (11)9999-8888 belo horizonte é (31)67097-1242 piracicaba é (19)97863-2642'

print(re.search('\(\d{2}\)\d{4,5}-\d{4}',frase1)) #estrutura usada para filtragem a partir dos metacaracteres
# span é a posição que a cadeia ocupa na string
print(re.search('[a-z-A-Z]{3}-\d{4}', frase2))
print(re.search('\w+@\w+\.com', frase3))

#Função Match = retorna se a função está no início da string

print(re.match('[a-z-A-Z]{3}-\d{4}', frase2)) #retorna se o determinado padrão está no início da string
print(re.match('\w+@\w+\.com', frase4))

#Função Findall = retorna todos os padrões encontrados

print(re.findall('\(\d{2}\)\d{4,5}-\d{4}',frase5))
print(re.findall('\w+@\w+\.\w+', frase3))

#Exercício para treinar

frase5 = ' 12 1232 12342 12212 13231-124 14634-642 18124-753 https://www.google.com.br http://www.facebook.com.br https://www.github.com'

print(re.findall('\d+', frase5))
print(re.findall('\d{5}-\d{3}', frase5))
print(re.findall('https?://[A-Z-a-z0-9./]+', frase5))

input('\n\nDigite qualquer tecla para encerrar o programa: ')