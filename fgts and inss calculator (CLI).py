rmb = float(input('Digite sua renda mensal bruta: '))

vbfa = rmb+rmb*0.3
vdmi = rmb*0.11
vafg = rmb*0.085*6

print('\n\no valor bruto que você receberá no final do ano considerando décimo terceiro e um terço de férias será de: R$ ', vbfa)
print('\no valor de desconto mensal de INSS é de R$ ', vdmi)
print('\no valor que você terá acumulado no fundo de garantia em seis meses será de R$ ', vafg)

print('\n\nAs alíquotas estão sendo conideradas da seguinte forma:')
print('- 11% de desconto sobre a renda mensal para arrecadação previdenciária ')
print('- 8,5% do salário bruto para FGTS ')


input('\n\nDigite qualquer tecla para encerrar o programa: ')
