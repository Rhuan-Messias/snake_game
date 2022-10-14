import turtle as t

# lembre-se que em python, uma constante é nomeada com todas as letras
# maiúsculas
POSIÇÃO_INICIAL = [(0,0),(-20,0),(-40,0)]
RASTEJAR = 20

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
        self.partes_do_corpo[0].forward(RASTEJAR)

    def cima(self):
        self.direção.setheading(90)
    def baixo(self):
        self.direção.setheading(270)
    def esquerda(self):
        self.direção.setheading(180)
    def direita(self):
        self.direção.setheading(0)