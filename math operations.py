import math #importa a biblioteca de funções matemáticas

numero = 15
numero2 = 15.3454
print(f'{numero} elevado ao quadrado é igual a: ',numero**2) #função de exponenciação
print('a raiz quadrada de ',numero**2,'é igual a: ', math.sqrt(numero**2)) #função de radiciação 
print(f'a aproximação de {numero2} é: ', round(numero2, 0)) #função para arredondamento, o segundo indice indica a quantidade de casas decimais
print(f'a tangente de {numero} é: ',math.tan(numero)) #função para retornar o valor da tangente
print(f'o cosseno de {numero} é: ',math.cos(numero)) #função para retornar o valor do cosseno
print(f'o seno de {numero} é: ',math.sin(numero)) #função para retornar o valor do seno
print(math.factorial(numero)) #função para retornar a fatorial
print(math.radians(numero)) #função para converter o angulo em radianos (pi)
print(math.hypot(3,4)) #função para retornar o valor da hipotenusa
print(math.degrees(3.14)) #função para converter o angulo em graus

input('\n\nDigite qualquer tecla para encerrar o programa: ')
