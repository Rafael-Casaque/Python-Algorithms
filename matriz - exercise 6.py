matriz = [[],[],[],[],[],[],[],[]]
matriz_transposta = [[],[],[],[],[],[],[],[]]

# Primeira Linha

matriz[0].append(0)
for i in range(0,6):
    matriz[0].append(1)
matriz[0].append(8)

# Segunda Linha

matriz[1].append(1)
matriz[1].append(0)
for i in range(0,4):
    matriz[1].append(1)
matriz[1].append(8)
matriz[1].append(2)

# Terceira Linha

for i in range(0,2):
    matriz[2].append(1)
matriz[2].append(0)
for i in range(0,2):
    matriz[2].append(1)
matriz[2].append(8)
for i in range(0,2):
    matriz[2].append(2)

# Quarta Linha

for i in range(0,3):
    matriz[3].append(1)
matriz[3].append(0)
matriz[3].append(8)
for i in range(0,3):
    matriz[3].append(2)

# Quinta Linha

for i in range(0,3):
    matriz[4].append(1)
matriz[4].append(8)
matriz[4].append(0)
for i in range(0,3):
    matriz[4].append(2)

# Sexta Linha

for i in range(0,2):
    matriz[5].append(1)
matriz[5].append(8)
for i in range(0,2):
    matriz[5].append(2)
matriz[5].append(0)
for i in range(0,2):
    matriz[5].append(2)

# Sétima Linha

matriz[6].append(1)
matriz[6].append(8)
for i in range(0,4):
    matriz[6].append(2)
matriz[6].append(0)
matriz[6].append(2)

# Oitava Linha

matriz[7].append(8)
for i in range(0,6):
    matriz[7].append(2)
matriz[7].append(0)

# Transposta

for i in range(8):
    matriz_transposta[0].append(matriz[i][0])
    matriz_transposta[1].append(matriz[i][1])
    matriz_transposta[2].append(matriz[i][2])
    matriz_transposta[3].append(matriz[i][3])
    matriz_transposta[4].append(matriz[i][4])
    matriz_transposta[5].append(matriz[i][5])
    matriz_transposta[6].append(matriz[i][6])
    matriz_transposta[7].append(matriz[i][7])

# Exibição
# Matriz original

for i in range(0,8):
    print(matriz[i])

print('\n')
# Matriz transposta
print('\n')
for i in range(0,8):
    print(matriz_transposta[i])