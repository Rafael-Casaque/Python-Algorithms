from numpy.core.numeric import NaN
import pandas as pd
import os

atualizacoes = 0

try:
    open('hospital-database.csv')
except FileNotFoundError:
    with open('hospital-database.csv', 'w',encoding='utf-8') as hospital:
        hospital.write('nome,idade,tipo de atendimento')

while True:
    os.system('cls')
    print('\n--------Menu de Opções--------')
    print('1 - Cadastrar novos pacientes.')
    print('2 - Listar pacientes.')
    print('3 - Atualizar informações.')
    print('4 - Listar pacientes por tipo de atendimento.')
    print('5 - Exibir a quantidade de pacientes com atualizações de dados.')
    print('6 - Exibir a média de idades de pacientes com plano de saúde.')
    print('7 - Exibir o nome do paciente mais velho.')
    print('8 - Excluir a base de dados')
    print('9 - Finalizar o programa')
    print('------------------------------')
    n = input('Escolha a opção desejada: ')

    if n =='1':
        os.system('cls')
        with open('hospital-database.csv', 'a',encoding='utf-8') as hospital:
            hospital_db = pd.read_csv('hospital-database.csv')
            nome = input('Digite o nome do paciente: ')                        
            validacao = str(hospital_db.loc[hospital_db['nome']==nome.lower()])            
            if validacao!="Empty DataFrame\nColumns: [nome, idade, tipo de atendimento]\nIndex: []":
                print('Já tem um paciente com esse nome na base de dados')
            else:
                idade = int(input('Digite a idade do paciente: '))
                plano = input('Digite o tipo de atendimento;\n1 - Plano de Saúde\n2 - SUS\n3 - Particular:  ')
                if plano == '1':
                    plano = 'Plano de Saúde'
                elif plano == '2':
                    plano = 'SUS'
                if plano == '3':
                    plano = 'Particular'    
                hospital.write(f'\n{nome.lower()},{idade},{plano}')                    
    
    elif n=='2':

        os.system('cls')
        hospital_db = pd.read_csv('hospital-database.csv')        
        if hospital_db.shape == (0,3):
            print('\nO banco de dados de pacientes está vazio')
        else:
            print('Base de dados encontrada:\n\n')
            print(hospital_db)
        input('\nDigite qualquer tecla para voltar ao menu:')        
    
    elif n=='3':
        os.system('cls')
        hospital_db = pd.read_csv('hospital-database.csv')
        nome = str(input('Digite o nome do paciente que deseja alterar a idade: '))        
        validacao = str(hospital_db.loc[hospital_db['nome']==nome.lower()])            
        if validacao=="Empty DataFrame\nColumns: [nome, idade, tipo de atendimento]\nIndex: []":
            print('Não há um paciente com esse nome na base de dados!')
        else:
            idade = int(input('Digite a idade atualizada: '))
            hospital_db = pd.read_csv('hospital-database.csv')
            hospital_db.loc[hospital_db['nome']==nome.lower(),'idade'] = idade
            lista = []                                              
            delimitador = hospital_db.shape                           
            for i in range(0,delimitador[0]):                       
                lista.append(f'{hospital_db.iloc[i,0]},{hospital_db.iloc[i,1]},{hospital_db.iloc[i,2]}')
            with open('hospital-database.csv','w',encoding='utf-8') as hospital:   
                hospital.write('nome,idade,tipo de atendimento')
                for i in range(0,len(lista)):
                    hospital.write(f'\n{lista[i]}')
            print('\nDados atualizados com sucesso!')
            atualizacoes += 1
        input('\nDigite qualquer tecla para voltar ao menu: ')
    elif n=='4':        
        os.system('cls')
        with open('hospital-database.csv', 'a') as hospital:
            hospital_db = pd.read_csv('hospital-database.csv')
        busca_tipo_atendimento = int(input('Informe o tipo de atendimento que deseja buscar: \n1 - Plano de Saúde\n2 - SUS\n3 - Particular: '))        
        os.system('cls')
        if busca_tipo_atendimento == 1:
            validacao2 = str(hospital_db.loc[hospital_db['tipo de atendimento']=='Plano de Saúde'])
            if validacao2!="Empty DataFrame\nColumns: [nome, idade, tipo de atendimento]\nIndex: []":
                print('A relação de pacientes que possuem plano de saúde como atendimento é: ')
                print(hospital_db.loc[hospital_db['tipo de atendimento']=='Plano de Saúde'])
            else:
                print('\nNão há registros de pacientes com esse tipo de atendimento')
            input('\nDigite qualquer tecla para voltar ao menu:')
        elif busca_tipo_atendimento == 2:
            validacao2 = str(hospital_db.loc[hospital_db['tipo de atendimento']=='SUS'])
            if validacao2!="Empty DataFrame\nColumns: [nome, idade, tipo de atendimento]\nIndex: []":
                print('A relação de pacientes que possuem SUS como atendimento é: ')
                print(hospital_db.loc[hospital_db['tipo de atendimento']=='SUS'])
            else:
                print('\nNão há registros de pacientes com esse tipo de atendimento')
            input('\nDigite qualquer tecla para voltar ao menu:')            
        elif busca_tipo_atendimento == 3:
            validacao2 = str(hospital_db.loc[hospital_db['tipo de atendimento']=='Particular'])
            if validacao2!="Empty DataFrame\nColumns: [nome, idade, tipo de atendimento]\nIndex: []":
                print('A relação de pacientes que possuem atendimento particular é: ')
                print(hospital_db.loc[hospital_db['tipo de atendimento']=='Particular'])
            else:
                print('\nNão há registros de pacientes com esse tipo de atendimento')
            input('\nDigite qualquer tecla para voltar ao menu:')
    elif n=='5':
        os.system('cls')
        print(f'{atualizacoes} pacientes tiveram seus dados atualizados.')
        input('Digite qualquer tecla para voltar ao menu: ')
    elif n=='6':
        hospital_db = pd.read_csv('hospital-database.csv')
        os.system('cls') 
        if str(hospital_db.loc[hospital_db['tipo de atendimento']=='Plano de Saúde','idade'].mean()) == 'nan':
            print('Não há pacientes com Plano de Saúde na base de dados!')
        else:
            print('A média das idades dos pacientes com Plano de Saúde é: ',hospital_db.loc[hospital_db['tipo de atendimento']=='Plano de Saúde','idade'].mean())
        input('\nDigite qualquer tecla para voltar ao menu: ')
    elif n=='7':
        print('Abaixo estão os dados do paciente mais velho:\n\n',hospital_db['idade'].max())
        input('Digite qualquer tecla para voltar ao menu: ')
    elif n=='8':
        os.system('cls')
        with open('hospital-database.csv', 'w') as hospital:
            hospital.write('nome,idade,tipo de atendimento')
        print('A base de dados foi apagada!')
        input('\nDigite qualquer tecla para voltar ao menu:')
    
    elif n=='9':        
        os.system('cls')
        break