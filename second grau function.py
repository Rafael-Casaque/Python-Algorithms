class funcao_quadratica:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def delta(self):
        delta = self.b**2-4*self.a*self.c
        if(delta==0):
            return 'existe apenas uma raiz para essa função'
        if(delta>0):
            return 'existem duas raizes reais para essa função'
        if(delta<0):
            return 'não existem raizes reais para essa função'

valores = []

for i in range(1,4):
    numero = float(input(f'Digite o {i}º valor: '))
    valores.append(numero)

funcao1 =  funcao_quadratica(valores[0],valores[1],valores[2])

print(funcao1.delta())
    
