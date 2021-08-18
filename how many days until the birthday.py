from datetime import datetime

i=0
while i<1:
    data_aniversario = str(input('Digite a data do seu próximo aniversário, da seguinte forma DD-MM-AAAA: '))
    data_niver = data_aniversario.split('-')
    ano = int(data_niver[2])
    mes = int(data_niver[1])
    dia = int(data_niver[0])

    h1 = data_aniversario.find('-')
    h2 = data_aniversario.rfind('-')
    if (len(data_aniversario)==10 and h1==2 and h2==5):
       i = 2
    else:
       print('\nO formato de data está incorreto,  tente novamente: ')       

import datetime

datapadrao = datetime.date(ano, mes, dia)
hoje = datetime.date.today()

dias = datapadrao - hoje
dias_restantes = (dias.days)

if (dias_restantes<0):
   print('A data informada é anterior à data atual!')
elif(dias_restantes>0):
   print (f'Faltam {dias_restantes} para seu aniversário')
else:
   print('Seu aniversário é hoje, parabéns!')

input('\n\nDigite qualquer tecla para encerrar o programa: ')