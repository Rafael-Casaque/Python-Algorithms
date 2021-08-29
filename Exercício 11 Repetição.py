#Duas fabricantes de calçado disputam o mercado no Brasil. A empresa A tem produção de 10.000 pares/mês 
#e um crescimento mensal de 15%. A empresa B, de 8.000 pares/mês e tem um crescimento mensal de 20%. 
#Determinar o número de meses necessários para que a empresa B supere o número de pares produzidos pela empresa A.

i = 1
while True:
    crescimento_a = 10000+(10000*0.15*i)
    crescimento_b = 8000+(8000*0.20*i)
    i += 1
    if (crescimento_b>crescimento_a):
        print(f'No mês {i-1} o faturamento da empresa b supera o faturamento da empresa a')
        break
input('\n\nDigite qualquer tecla para encerrar o programa: ')
