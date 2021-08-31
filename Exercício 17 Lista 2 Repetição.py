#EX 17 - Lista2
#Faça um programa que receba a idade, peso e altura de N pessoas. Calcule e mostre: 

#a. A média das idades das N pessoas 

#b. A quantidade de pessoas com peso superior a 90 quilos e altura inferior a 1,50 m. 

#c. A percentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1,90 m. 

#Pergunte ao usuário do programa quantas pessoas serão cadastradas (valor de N).

lista_altura = []
lista_idade = []
lista_peso = []
i = 1
n = int(input('Digite quantas pessoas serão cadastradas: '))
k = 0
l = 0

while True:
    altura = float(input(f'\nDigite a altura da {i}ª pessoa: '))
    lista_altura.append(altura)
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))
    lista_idade.append(idade)
    peso = float(input(f'Digite o peso da {i}ª pessoa: '))
    lista_peso.append(peso)

    i+=1

    if (n == i-1):
        break

for j in range(n):
    if (lista_altura[j]<1.5 and lista_peso[j]>90):
        k += 1
for j in range(n):
    if (lista_idade[j]>10 and lista_idade[j]<30):
        l += 1

print(f'\nA média de idades das pessoas cadastradas é de: {sum(lista_idade)/n}')
print(f'A quantidade de pessoas com peso maior que 90 kg e altura menor que 1.5 m é: {k}')
print(f'A quantidade de pessoas com idade entre 10 e 30 anos é: {l}')

input('\nDigite qualquer tecla para fechar o programa: ')