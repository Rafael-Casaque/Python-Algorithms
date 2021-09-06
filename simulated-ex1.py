#Simulado - Ex1

#1 – Faça um programa para informatizar o cadastro de alunos em uma escola de inglês. Você deve cadastrar os alunos 
# com as seguintes informações: nome do aluno, idade, sexo (M ou F) e valor da mensalidade paga. Devem ser cadastrados 
# alunos até que a idade seja 0 (zero). Depois de cadastrados os alunos informe:

#a- a quantidade de alunos (homens) com mais de 18 anos.
#b- o percentual de alunos que pagam mensalidade maior que R$ 100,00 e menor que R$ 200,00.
#c- o nome do aluno do sexo masculino que paga a menor mensalidade.
#d- o valor da maior mensalidade paga por alunas com idade maior que 50 anos ou com idade menor que 18 anos.
#e- preço médio das mensalidades dos homens com mais de 18 anos.

import os

cadastro_aluno_idade = []
cadastro_aluno_nome = []
cadastro_aluno_sexo = []
cadastro_aluno_mensalidade = []
i = 1
filtro_idade = 0
filtro_mensalidade = 0
filtro_masculino = {}
filtro_feminino = {}
filtro_masculino_mensalidade = []

# entrada de dados

while True:
    idade = int(input(f'Digite a idade do {i}º aluno a ser cadastrado: '))
    if idade == 0:
        os.system('cls')
        break
    cadastro_aluno_idade.append(idade)
    nome = input(f'Digite o nome do {i}º aluno a ser cadastrado: ')
    cadastro_aluno_nome.append(nome)
    sexo = input(f'Digite o sexo do {i}º aluno a ser cadastrado: ')
    cadastro_aluno_sexo.append(sexo)
    mensalidade = float(input(f'Digite o valor da mensalidade do {i}º aluno a ser cadastrado: '))
    cadastro_aluno_mensalidade.append(mensalidade)
    i+=1
    os.system('cls')

# parte a

for i in range(0,len(cadastro_aluno_sexo)):
    if (cadastro_aluno_idade[i] > 18 and cadastro_aluno_sexo[i]=='m'):
        filtro_idade +=1

# parte b

for j in cadastro_aluno_mensalidade:
    if (j>100 and j<200):
        filtro_mensalidade +=1

percentual_mensalidade = filtro_mensalidade/len(cadastro_aluno_mensalidade)*100

# parte c
for i in range(len(cadastro_aluno_sexo)):
    if cadastro_aluno_sexo[i]=='m': #faz a filtragem para apenas pessoas do sexo masculino
        filtro_masculino[cadastro_aluno_nome[i]]=cadastro_aluno_mensalidade[i] #adiciona valor e chave, nome e valor mensalidade

# parte d 

for i in range(len(cadastro_aluno_sexo)):
    if cadastro_aluno_sexo[i]=='f' and cadastro_aluno_idade[i]>50 or cadastro_aluno_sexo[i]=='f' and cadastro_aluno_idade[i]<18:
        filtro_feminino[cadastro_aluno_mensalidade[i]]=cadastro_aluno_mensalidade[i]

#parte e

for i in range(len(cadastro_aluno_idade)):
    if cadastro_aluno_idade[i]>18:
        filtro_masculino_mensalidade.append(cadastro_aluno_mensalidade[i])

media_mensalidade = sum(filtro_masculino_mensalidade)/len(filtro_masculino_mensalidade)

# saída de dados

print('A quantidade de alunos (homens) com mais de 18 anos é: ',filtro_idade)
print('\nO percentual de alunos que pagam entre R$100,00 e R$200,00 de mensalidade é: ',round(percentual_mensalidade, 2),'%')     
print('\nO aluno do sexo masculino que paga a menor mensalidade é: ',min(filtro_masculino)) # busca a chave com menor valor e retorna o nome
print('\nA maior mensalidade paga por alunas com idade maior que 50 anos ou menor que 18 anos é de: R$',round(max(filtro_feminino),2))
print('\nO valor médio de mensalidade paga por homens maiores de 18 anos é de: R$',media_mensalidade)

input('\n\nDigite qualquer tecla para encerrar o programa: ')