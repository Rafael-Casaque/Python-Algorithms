# Programação Orientada a Objetos: Classe e Objeto

# Classe: um agrupamento de objetos similares que apresentam os mesmos atributos e métodos

# Métodos: são as funções realizadas pelas classes

# Exemplo: Molde de biscoito, o tamanho e formato serão sempre os mesmos, porém as características variam 

class Triangulo:
    def __init__(self, l1,l2,l3,b,a): #função padrão para passar os parâmetros iniciais
        self.l1 = l1 # cria os atributos, o self indica "a criação de uma característica" 
        self.l2 = l2
        self.l3 = l3
        self.b = b
        self.a = a
    def area(self):
        return self.b * self.a /2  
    def tipo(self):
        if(self.l1>self.l2+self.l3 or self.l2>self.l1+self.l3 or self.l3>self.l2+self.l1 ):
            return 'Esses lados não formam um triangulo'
        elif(self.l1==self.l2==self.l3):
            return 'Esses lados formam um triângulo equilatero'
        elif(self.l1!=self.l2 and self.l2!=self.l3 and self.l3!=self.l1):
            return 'Esses lados formam um triângulo escaleno'
        else:
            return 'Esses lados formam um triângulo isósceles' 


t1 = Triangulo(3,4,5,2,4) # cria o objeto t1 passando os parâmetros solicitados
t2 = Triangulo(3,3,3,2,4)
t3 = Triangulo(3,4,3,2,4)
t4 = Triangulo(3,3,7,2,4)
t5 = Triangulo(3,4,5,2,4)
print(t1.l1,t1.l2,t1.l3) # printa os atributos criados na classe
print(t1.area()) # printa a função !!! não usa parâmetro pois o objeto já foi definido anteriormente 

print(t2.tipo())
print(t3.tipo())
print(t4.tipo())
print(t5.tipo())