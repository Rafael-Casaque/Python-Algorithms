nome = input('digite o nome: ')
sobrenome = input('digite o sobrenome: ')
print ('Usuário: ',nome+ ' ' + sobrenome)
print('\n')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

operation = str(input('Digite a operação desejada: '))

if operation == "soma" or operation == "SOMA":
    n3 = n1+n2
elif operation == "subtração" or operation == "SUBTRAÇÃO":
    n3 = n1-n2
elif operation == "multiplicação" or operation == "MULTIPLICAÇÃO":
    n3 = n1*n2
elif operation == "divisão" or operation == "DIVISÃO":
    n3 = n1/n2
else:
    print('Erro, você não digitou a operação corretamente!')

print('\nA operação de', operation, 'entre ',n1,' e ',n2, 'é igual a: ',n3)
input('\n\nDigite qualquer tecla para encerrar o programa: ')
