# Estudo dos tipos de erros em Pyhton

# • NameError: a variável não foi definida 
# • TypeError: tipos de dados incompatíveis 
# • RunTimeError: erro de execução
# • SyntaxError: sintaxe digitada é inválida e não reconhecida 
# • ZeroDivisorErro: divisão por zero
# • IndexError: o índice está fora da coleção
# • ValueError: o tipo de dado inserido é incompativel

#tratamento de exceções
while True: # estrutura de validação, enquanto houver erro, continuára repetindo
    try:    # estrutura para tratar erro sem afettar a execução do código
        n1 = int(input('Digite um numero inteiro: '))
    except ValueError: # dado que será emitido caso haja erro 
        print('Esse valor não é inteiro')
    else:   # dado que será emitido caso não haja erro 
        print('Segue o baile')
        break

input('\n\nDigite qualquer tecla para encerrar o programa: ')
