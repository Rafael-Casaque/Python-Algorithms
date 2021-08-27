# Elabore um programa que mostre os n termos da Série a seguir:
#a. S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
#Imprima no final a soma da série. Leia o valor de (n)

n = int(input("Digite um valor inteiro: "))
j = 1
somatotal = 0
for i in range(1,n+1):
    soma = i/j    
    j = i+i+1    
    somatotal += soma    
print(somatotal)