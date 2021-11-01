#Você foi contratado para construir um sistema de uma agência de turismo. No seu sistema
#deve ser possível:

#1. Cadastrar um cliente contendo: nome e idade. Não deve ser possível cadastrar um
#aluno com mesmo nome e a idade deve ser superior a 18 anos.

#2. Cadastrar um destino de viagem: nome, valor da diária, número mínimo de diárias.

#3. Cadastrar uma viagem: deve ser salvo o nome do cliente, o destino e número de
#diárias. O valor total da viagem também deverá ser salvo na viagem cadastrada. Em
#cada cliente também deverá ser salvo o valor total gasto na agência.

#4. Listar as viagens já salvas, categorizadas por destino. Ex: devem ser listadas todas as
#viagens feitas com destino na Cidade X, depois, todas as viagens feitas para a cidade Z,
#e assim por diante.

#5. Listar os clientes.

#6. Contabilizar a pontuação de cada cliente. Com o intuito de fidelizar os clientes na
#agência foi criado um programa de pontuação. A cada 1000 reais em viagens, o cliente
#deve receber 100 pontos. Quando ele totalizar 1500 pontos ele pode escolher uma
#cidade de destino e ganhará 3 diárias para esse local. Após calcular a pontuação exibir
#uma tabela com a lista de pontos por cliente. Dica: utilizar um dicionário. Destacar os
#clientes que estão ganhar a viagem.

#7. Informar o destino mais procurado pelos clientes.

#8. Informar o destino para o qual mais diárias foram vendidas.

#9. Efetuar o pagamento de gastos do cliente: o cliente informa o nome e o sistema exibe
#quanto ele está devendo para a agência. O cliente informa o valor que irá pagar e esse
#valor é abatido das faturas em aberto.

#10. Avaliar status dos clientes: o sistema deve verificar os clientes que possuem mais de
#R$10.000,00 em viagens ainda não pagos. Quando esse valor for atingido não deve ser
#possível mais vender viagens para esse cliente.
clientes_db = []
destinos_db = []
lista_destinos = []
destinos_mais_procurados = {}
viagens_db = []
viagens_db_agrupada = []
clientes_gastos_db = {}
clientes_gastos_db2 = {}
destino_diarias = {}
destino_diarias2 = {}
clientes_pontos = {}

import os

def menu():
    """Retorna o menu de opções para o usuário"""
    os.system('cls')
    print("0 - Finalizar o programa")
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar destino de viagem")
    print("3 - Cadastrar uma viagem")
    print("4 - Listar viagens salvas")
    print("5 - Listar clientes")
    print("6 - Contabilizar a pontuação de cada cliente")    
    print("7 - Informar o destino mais procurado pelos clientes")
    print("8 - Informar o destino para o qual mais diárias foram vendidas")
    print("9 - Efetuar o pagamento de gastos do cliente")
    print("10 - Avaliar status dos clientes")    
    return

def cadastrar_cliente(nome,idade):
    """Realiza o cadastramento de clientes"""
    clientes_db.append([nome,idade])     
    return

def cadastrar_destino(nome,valor_diaria,numero_min_diarias):
    """Realiza o cadastramento de destino da viagem"""
    destinos_db.append([nome,valor_diaria,numero_min_diarias]) 
    return

def cadastrar_viagem(nome,destino,numero_diarias,valor):
    """Realiza o cadastramento de uma viagem e contabiliza os gastos dos clientes"""
    viagens_db.append([nome,destino,numero_diarias,valor]) 
    
    if destino in destino_diarias.keys():
        destino_diarias[destino] = destino_diarias[destino] + numero_diarias
    else:
        destino_diarias[destino] = numero_diarias
    
    if nome in clientes_gastos_db.keys():        
        clientes_gastos_db[nome]=clientes_gastos_db[nome]+valor 
    else:
        clientes_gastos_db[nome]=valor    
    return

def listagem_viagens_agrupadas(viagens_db,viagens_db_agrupada):
    """"Realiza a listagem das viagens agrupadas"""
    for i in range(len(viagens_db)):
        for j in range(len(viagens_db)):
            if viagens_db[i][1] == viagens_db[j][1] and viagens_db[j] not in viagens_db_agrupada :
                viagens_db_agrupada.append(viagens_db[j])    
    return

def calculo_destinos_mais_procurados(viagens_db,lista_destinos,destinos_mais_procurados):
    """Calcula e retorna o destino mais procurado pelos clientes"""
    for i in range(len(viagens_db)):
        lista_destinos.append(viagens_db[i][1])
    for i in range(len(lista_destinos)):
        if lista_destinos[i] not in destinos_mais_procurados.values():
             destinos_mais_procurados[lista_destinos.count(lista_destinos[i])]=lista_destinos[i]
    return

def calculo_destino_mais_diarias(destino_diarias,destino_diarias2):
    for i in destino_diarias:
        destino_diarias2[destino_diarias[i]]=i
    return

def contabilizacao_de_pontuacao(clientes_gastos_db2,clientes_pontos):
    for i in clientes_gastos_db2:
        clientes_pontos[i]=clientes_gastos_db2[i]*0.1
    return

def pagamento_do_cliente(nome,valor,clientes_gastos_db):
    if nome in clientes_gastos_db.keys():
        clientes_gastos_db[nome]=clientes_gastos_db[nome]-valor
    return
while True:
    menu()
    n = str(input('Informe a opção desejada: '))
    if n == '0':
        break
    if n == '1':
        nome = str(input('Digite o nome do cliente: '))
        if len(clientes_db) == 0:
            idade = int(input('Digite a idade do cliente: '))        
            if idade<18:
                    print("Não é permito cadastrar um usuário com idade inferior a 18 anos!")
            else:
                cadastrar_cliente(nome,idade)  
                print("\nCliente cadastrado com sucesso!") 
        else:
            for i in range(len(clientes_db)):
                if nome == clientes_db[i][0]:
                    print('Esse cliente já existe na base de dados!')
                else:
                    idade = int(input('Digite a idade do cliente: '))        
                    if idade<18:
                        print("Não é permito cadastrar um usuário com idade inferior a 18 anos!")
                    else:
                        cadastrar_cliente(nome,idade)   
                        print("\nCliente cadastrado com sucesso!")
        input("\nDigite qualquer tecla para retornar ao menu: ") 
    
    if n == '2':
        nome = str(input('Digite o nome do destino: '))
        valor_diaria = float(input('Digite o valor da diária: '))
        numero_min_diarias = int(input('Digite o número mínimo de diárias: '))
        cadastrar_destino(nome,valor_diaria,numero_min_diarias)
        print("\nDestino cadastrado com sucesso!")
        input("\nDigite qualquer tecla para retornar ao menu: ")
    
    if n == '3':
        nome = str(input('Digite o nome do cliente: '))
        destino = str(input('Digite o nome do destino: '))
        numero_diarias = int(input('Digite o número de diárias: '))
        valor = float(input('Digite o valor total da viagem: '))
        cadastrar_viagem(nome,destino,numero_diarias,valor)
        if len(clientes_gastos_db2) == 0: 
            clientes_gastos_db2 = clientes_gastos_db.copy()
        else:
            if nome in clientes_gastos_db2.keys():        
                clientes_gastos_db2[nome]=clientes_gastos_db2[nome]+valor 
            else:
                clientes_gastos_db2[nome]=valor
        print("\nViagem cadastrada com sucesso!")
        input("\nDigite qualquer tecla para retornar ao menu: ")
    
    if n == '4':
        listagem_viagens_agrupadas(viagens_db,viagens_db_agrupada)
        for i in range(len(viagens_db_agrupada)):        
            print(viagens_db_agrupada[i])    
        input("\nAperte qualquer tecla para retornar ao menu: ")
    
    if n == '5':
        for i in range(len(clientes_db)):
            print(clientes_db[i])
        input("\nAperte qualquer tecla para retornar ao menu: ")
    if n == '6':
        contabilizacao_de_pontuacao(clientes_gastos_db2,clientes_pontos)
        for i in clientes_pontos:
            if clientes_pontos[i]>=1000:
                print(clientes_pontos[i],i," cliente elegível para trocar os pontos no programa fidelidade.")
            else:
                print(clientes_pontos[i],i)
        input('\nDigite qualquer tecla para voltar ao menu: ')

    if n == '7':
        calculo_destinos_mais_procurados(viagens_db,lista_destinos,destinos_mais_procurados)
        print(f"\nO destino mais procurado é {destinos_mais_procurados[max(destinos_mais_procurados.keys())]}, tendo {max(destinos_mais_procurados.keys())} viagens marcadas")
        input('\nDigite qualquer tecla para voltar ao menu: ')
    if n == '8':
        calculo_destino_mais_diarias(destino_diarias,destino_diarias2)
        print(f"O destino com mais diárias reservadas é {destino_diarias2[max(destino_diarias2.keys())]}, tendo um total de {max(destino_diarias2.keys())} diárias reservaas.")        
        input('\nDigite qualquer tecla para voltar ao menu: ')
    if n == '9':
        nome = str(input('Digite o nome do cliente: '))
        valor = int(input('Digite o valor que o cliente deseja pagar: '))
        pagamento_do_cliente(nome,valor,clientes_gastos_db)
        print('Pagamento realizado com sucesso!')
        input('\nDigite qualquer tecla para encerrar o programa: ')
    if n == '10':
        for i in clientes_gastos_db:
            if clientes_gastos_db[i]>10000:
                print(f"{i} não pode mais reservar viagens pois tem mais de R$ 10.000 em dívidas não pagas!")
        input("\nDigite qualquer tecla para retornar ao menu: ")
