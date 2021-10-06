#Exercício 2 - Strings
#Dada uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte a quantidade de espaços em branco e a quantidade de vezes que aparecem as vogais a, e, i, o, u.
qtd_espaço_branco = 0
qtd_vogais = []

my_str = str(input('Digite uma palavra: '))

for i in my_str:
    if i==' ':
        qtd_espaço_branco+=1

for i in my_str.lower():
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        qtd_vogais.append(i)
        
print(f"A quantidade de espaços em branco na string é de {qtd_espaço_branco} caracteres.")
print(f"A quantidade de vogais nessa string é de {len(qtd_vogais)} caracteres, sendo eles: {qtd_vogais}")

input('Digite qualquer tecla para fechar o programa: ')
