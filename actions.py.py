#Fazer uma opção na qual o usuário pode vender parte das ações que tem. Você deve:

#- verificar se é possível vender a quantidade de ações

#- informar se o usuário teve lucro ou prejuízo, considerando o valor da ação

#- atualizar a quantidade de ações do usuário

listaPetro = []
listaBB = []
listaMagalu = []

opcao = -1
while opcao !=0:
    print('Menu')
    print('0 - sair')
    print('1 - Cadastrar Dados Petrobras')
    print('2 - Cadastrar Dados Banco do Brasil')
    print('3 - Cadastrar Dados Magalu')
    print('4 - Listar')
    print('5 - Buscar valor investido com Petro')
    print('6 - Encontrar o dia com o maior valor da acao')
    print('7 - Informar se o usuario ganhou ou perdeu dinheiro com a ação. ')
    print('8 - Informar a tendencia da acao: ')
    print('9 - Informar a tendendica comparando com a ultima semana: ')
    print('10 - Informar o preço medio na primeira semana')
    print('11 - Vender parte das ações')
    opcao = int(input('Digite a opcao: '))
    if opcao == 1:
        if len(listaPetro) == 0:
            listaPetro.append('Petrobras')
            qtddAcoes = int(input('Digite quantas ações vc tem: '))
            listaPetro.append(qtddAcoes)
            valorAcao = float(input('Digite o valor de compra da ação: '))
            listaPetro.append(valorAcao)
        else:
            valorAcao = float(input('Digite o valor atualizado da ação: '))
            listaPetro.append(valorAcao)
    elif opcao ==4:
        print(listaPetro)
    elif opcao ==5:
        if len(listaPetro) > 0:
            ultimoValor = listaPetro[len(listaPetro)-1]
            qtddAcoes = listaPetro[1]
            valor = ultimoValor*qtddAcoes
            print('Valor em ações Petro = ' + str(valor))
    elif opcao ==6: #maior valor da ação
        if len(listaPetro) > 0:#cadastrei algum valor
            maior = listaPetro[2]
            dia = 1
            for i in range(2, len(listaPetro)):
                if listaPetro[i] > maior:
                    maior = listaPetro[i]
                    dia = i - 1
            print('Maior valor: ' + str(maior) + ' - dia: ' + str(dia))
    elif opcao ==7:
        if len(listaPetro) > 0:
            valorInicial = listaPetro[1]*listaPetro[2]
            valorFinal = listaPetro[1]*listaPetro[-1] #indice -1 pega o ultimo elemento da lista
            saldo = valorFinal - valorInicial
            if saldo > 0:
                print('Lucro: ' + str(saldo))
            elif saldo ==0:
                print('Empatou!')
            else:
                print('Prejuizo: ' + str(saldo))
    elif opcao ==8:
        if len(listaPetro) > 0:
            ultimoValor = listaPetro[-1]
            penultimoValor = listaPetro[-2]
            tendencia = ultimoValor/penultimoValor
            if tendencia > 1:
                percentual = tendencia - 1
                print('Alta : ' + str(percentual))
            elif tendencia < 1:
                percentual = 1 - tendencia
                print('Baixa : ' + str(percentual))
            else:
                print('Empatou!')

    elif opcao ==9:
        if len(listaPetro) > 10:
            ultimoValor = listaPetro[len(listaPetro)-1]
            valorUltimoDiaDaSemanaAnterior = listaPetro[len(listaPetro) - 8]
            tendencia = ultimoValor/valorUltimoDiaDaSemanaAnterior
            print(tendencia)
        else:
            print('Nao existem dados suficientes')
    elif opcao ==10:
        if len(listaPetro) >= 9:
            soma = 0
            for i in range(2,9):
                soma = listaPetro[i] + soma
            media = soma/7
            print('Media na primeira semana: ' + str(media))
    elif opcao ==11:
        try:
            qtd_venda = int(input('Digite a quantidade de ações que deseja vender: '))
            if qtd_venda > listaPetro[1]:
                print('Não é possível realizar a venda pois o valor digitado é maior que a quantidade de ações adquirida.')
            else:
                listaPetro[1]=listaPetro[1]-qtd_venda
        except IndexError:
            print('Não é possível realizar a venda pois o valor digitado é maior que a quantidade de ações adquirida.')
            
        if listaPetro[-1]>listaPetro[2]:
            print('Você teve lucro com a venda dessas ações.')
        elif listaPetro[-1]==listaPetro[2]:
            print('O valor de venda é igual ao valor de compra.')
        else:
            print('Você teve prejuízo com a venda dessas ações.')