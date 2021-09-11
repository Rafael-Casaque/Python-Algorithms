import random

lista_numeros = []
qtd_numeros_primos = []
checagem_n1 = [[],[],[],[],[],[],[],[],[],[]]

for i in range(0,10): lista_numeros.append(random.randint(1,1000))

def prime_number(a):
    for i in range(1,lista_numeros[a]+1):
        if lista_numeros[a] % i == 0: checagem_n1[a].append(i)
    return checagem_n1[a]

for i in range(0,10):
    if len(prime_number(i)) == 2:
        qtd_numeros_primos.append(lista_numeros[i]) 

print(qtd_numeros_primos)
print(lista_numeros)