#Elabore um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da 
# turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média 
# calculada. (Leia o valor de n)

n = int(input("digite a quantidade total de pessoas: "))
idades = []
for i in range(n):
    idade = int(input(f"\ndigite a idade da {i+1}ª pessoa: "))
    idades.append(idade)
if sum(idades)/len(idades)>=0 and sum(idades)/len(idades)<=25:
    print(f"\nEssa é uma turma jovem, sua média de idade é: {sum(idades)/len(idades)}")
if sum(idades)/len(idades)>=26 and sum(idades)/len(idades)<=60:
    print(f"\nEssa é uma turma adulta, sua média de idade é: {sum(idades)/len(idades)}")
if sum(idades)/len(idades)>60:
    print(f"\nEssa é uma turma idosa, sua média de idade é: {sum(idades)/len(idades)}")