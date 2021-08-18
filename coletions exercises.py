# exercício com lista

lista = []
soma = 0
soma2 = 0
nota = 0
for _ in range(0,5):
    numero = int(input(f'Digite o {_+1}º número : '))
    lista.append(numero)

for i in range(len(lista)):
    soma = soma + lista[i]
 
print('A soma dos números digitados é: ',soma)

# exercício com dicionário

dicionario = {}
soma2 = 0

for _ in range (0,3):
    nome = str(input(f"Digite o {_+1}º nome: "))
    nota = int(input(f"Digite a {_+1}º nota: "))
    dicionario[nome] = nota
for nota in dicionario.values():
    soma2 = nota + soma2

print('A média das notas é : ', soma2/3)

# eercício com matriz
import numpy as np

soma = 0 
matriz = np.array([[3, 4, 1],[3, 1, 5]])

for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        soma += matriz[i][j]
print(soma)

input('\n\nDigite qualquer tecla para encerrar o programa: ')