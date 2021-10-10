matriz = []
linha_1 = []
linha_2 = []

for i in range(0,4):
    
    linha_1.append(0)
    linha_1.append(1)    
    linha_2.append(1)
    linha_2.append(0)
    matriz.append(linha_1)
    matriz.append(linha_2)

for i in range(0,8):
    print(matriz[i])

input('Digite qualquer tecla para fechar o programa: ')