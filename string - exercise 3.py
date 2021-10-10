#Exercício 3 - Strings
#Um anagrama é uma palavra que é feita a partir da transposição das letras de outra palavra ou frase. 

#Por exemplo, “Iracema” é um anagrama para “America”. 

#Escreva um programa que decida se uma string é um anagrama de outra string, ignorando os espaços em branco. 
#O programa deve considerar maiúsculas e minúsculas como sendo caracteres iguais, ou seja, “a” = “A”.

my_string = str(input('Digite a primeira string: ')).lower()
my_string2 = str(input('Digite a segunda string: ')).lower()

my_list = []
my_list2 = []
my_list3 = my_list2 

for i in range (len(my_string2)):
    my_list2.append(my_string2[i])

for i in range (len(my_string)):
    my_list.append(my_string[i])

if my_list.sort() == my_list2.sort() and len(my_list) == len(my_list2)  :
    print('as palavras digitadas são anagramas!')
else:
    print('as palavras digitadas não são anagramas!')