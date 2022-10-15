import turtle as t

# lembre-se que em python, uma constante é nomeada com todas as letras
# maiúsculas
POSIÇÃO_INICIAL = [(0,0),(-20,0),(-40,0)]
RASTEJAR = 20
CIMA = 90
BAIXO = 270
DIREITA = 0
ESQUERDA = 180 

#classe começa com letra maiúscula 
# Toda vez que crio uma cobra dessa classe, aparecerá as 3 partes do
# corpo, e se moverá da maneira correta 
class Cobrinha:

    def __init__(self):
        self.partes_do_corpo = []
        self.criar_cobrinha()
        self.direção = self.partes_do_corpo[0]
    
    def criar_cobrinha(self):
        for i in POSIÇÃO_INICIAL:
            cobrinha = t.Turtle(shape='square')
            cobrinha.color('gray10')
            cobrinha.penup()
            cobrinha.goto(i)
            self.partes_do_corpo.append(cobrinha)
    
    #esse pedaço de código vai fazer com que a cobrinha se mova para
    #frente automaticamente
    def mover(self):
        for parte in range(len(self.partes_do_corpo)-1,0,-1):
            posição_x = self.partes_do_corpo[parte-1].xcor()
            posição_y = self.partes_do_corpo[parte-1].ycor()
            self.partes_do_corpo[parte].goto(posição_x,posição_y)
        self.head.forward(RASTEJAR)

    def cima(self):
        if self.head.heading() != BAIXO:
            self.direção.setheading(CIMA)
    def baixo(self):
        if self.head.heading() != CIMA:
            self.direção.setheading(BAIXO)
    def esquerda(self):
        if self.head.heading() != DIREITA:
            self.direção.setheading(ESQUERDA)
    def direita(self):
        if self.head.heading() != ESQUERDA:
            self.direção.setheading(DIREITA)