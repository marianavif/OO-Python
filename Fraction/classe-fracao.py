#Classe que cria um objeto do tipo fração, sendo iniciada com
#duas variáveis
class fraction(object):

    #Inicialização do objeto com duas variáveis, sendo elas numerador
    #e denominador da fração. Executa o método verificaTipo para
    # verificar que ambas variáveis são do tipo inteiro e
    #verificaDenNulo para verificar se o denominador é zero
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.verifyType()
        self.verifyNullDen()


    #Método para verificar se numerador e denominador são inteiros
    #Levanta uma exceção se ao menos um dos dois não for
    def verifyType(self):
        if isinstance(self.numerator, int) == False:
            raise Exception('numerator must be integer')
        if isinstance(self.denominator, int) == False:
            raise Exception('denominator must be integer')


    #Método para verificar se denominador é nulo.
    #Levanta uma exceção se for
    def verifyNullDen(self):
        if self.denominator == 0:
            raise Exception("denominator can't be null or zero")


    #Método para igualar o denominador do objeto ao denominador
    #do objeto parâmetro. Assim as frações se tornam comparáveis
    def lcm(self, x):
        den1 = self.denominator
        den2 = x.denominator
        x.numerator *= den1
        x.denominator *= den1
        self.denominator *= den2
        self.numerator *= den2


    #Método para simplificar o objeto. Calcula a lista de
    #divisores do numerador e do denominador e compara até
    #achar o maior em comum. Então divide ambos numerador
    #e denominador por este número
    def simplify(self):
        divNum = []
        divDen = []
        divisor = 1
        for i in range(1, self.numerator + 1):
            if self.numerator % i == 0:
                divNum.append(i)
        for j in range(1, self.denominator + 1):
            if self.denominator % j == 0:
                divDen.append(j)
        if len(divNum) >= len(divDen):
            for k in divNum:
                for l in divDen:
                    if l == k:
                        divisor = l
                        break
        else:
            for m in divDen:
                for n in divNum:
                    if n == m:
                        divisor = n
                        break
        self.numerator = int(self.numerator / divisor)
        self.denominator = int(self.denominator / divisor)


    #Método de soma do objeto com objeto parâmetro
    #Utiliza o método mmc, soma os numeradores e então
    #utiliza o método simplifica
    def add(self, x):
       self.lcm(x)
       self.numerator += x.numerator
       self.simplify()
       self.printFraction()

    #Método de acréscimo de 1 do objeto
    #Ao somar 1, acresce-se ao objeto uma fração em que ambos
    #o numerador e o denominador são iguais ao denominador do objeto
    #Logo, soma-se ao numerador do objeto o seu denominador
    #Então utiliza o método simplifica
    def increase(self):
        self.numerator += self.denominator
        self.simplify()
        self.printFraction()


    #Método para multiplicação do objeto com o objeto parâmetro
    #Multiplicam-se os numeradores entre si e os denominadores
    #entre si. Depois, utiliza o método simplifica
    def multiply(self, x):
        self.numerator *= x.numerator
        self.denominator *= x.denominator
        self.simplify()
        self.printFraction()


    #Método para subtração do objeto pelo objeto parâmetro
    #Utiliza-se o método mmc e então subtrai-se do numerador o
    #valor do numerador do objeto parâmetro. Então utiliza o
    #método simplifica
    def subtract(self, x):
        self.lcm(x)
        self.numerator -= x.numerator
        self.simplify()
        self.printFraction()


    #Método para comparar o objeto com o objeto parâmetro
    #Utiliza o método mmc para torná-los comparáveis e
    #então se numerador e denominador do objeto forem iguais
    #ao numerador e denominador do objeto parâmetro, respectivamente,
    # o método retorna o valor Verdadeiro. Senão retorna Falso.
    def equality(self, x):
        self.lcm(x)
        if self.numerator == x.numerator and self.denominator == x.denominator:
            self.simplify()
            print("Equality")
            return True
        else:
            self.simplify()
            print("Inequality")
            return False


    #Método para dividir o objeto pelo objeto parâmetro
    #Na divisão de frações, há a multiplicação cruzada
    #O numerador do objeto multiplica o denominador do objeto
    #parâmetro e o denominador do objeto multiplica o
    #numerador do objeto parâmetro e então é utilizado
    #o método simplifica
    def divide(self,x):
        self.numerator *= x.denominator
        self.denominator *= x.numerator
        self.simplify()
        self.printFraction()


    #Método para imprimir na tela a fração que representa o
    #objeto
    def printFraction(self):
        print("%d/%d" % (self.numerator, self.denominator))

fracao = fraction(1,25)
fracao2 = fraction(1,10)
fracao.printFraction()