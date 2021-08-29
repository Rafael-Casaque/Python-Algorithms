# Construa um algoritmo que calcule a média aritmética de um conjunto de números inteiros, pares, fornecidos pelo usuário. 
# O valor de parada será 0. O usuário poderá entrar números ímpares, porém, eles não devem ser considerados nos cálculos.
lista=[]
while True:
    try:
        numero = int(input('\nDigite um número par que seja inteiro, caso queira parar digite 0: '))
        if numero ==0:
            break
        if numero % 2 == 1:
            print('\nEsse número não é par!')
        else:
            lista.append(numero)
    except ValueError:
        print('\nEsse valor não é inteiro!')
<<<<<<< HEAD
print(f"\nA média aritmética dos valores digitados é: {sum(lista)/len(lista)}")

input('\n\nDigite qualquer tecla para encerrar o programa: ')
=======
print(f"\nA média aritmética dos valores digitados é: {sum(lista)/len(lista)}")
>>>>>>> be20a3946e33dbb3c2d7a86404062c651a695ca4
