#Exercício 1 - Strings
#Escreva um programa que reconhece se uma string é um palíndromo, ou seja, se lida do início para o fim é igual se lida do fim para o início. Exemplos: arara, ovo.

my_str = str(input('Digite uma palavra: '))

if my_str[::-1].lower() == my_str.lower():
    print("A palavra digitada é um palíndromo, possui o mesmo significado quando lido ao contrário")
else:
    print("A palavra digitada não é um palíndromo, ela não possui o mesmo significado quando lido ao contrário")
    
input('Digite qualquer tecla para fechar o programa: ')