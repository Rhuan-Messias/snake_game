import turtle as t
import time

tela = t.Screen()
tela.setup(width=600, height=600) #keyword arguments, quando o parâmetro recebe as informações, onde azul é o parametro e a o numero é o argumento chave
tela.bgcolor('green')
tela.title('Jogo da Cobrinha')
tela.tracer(0)

#Passo 1: criar o corpo cobrinha 
#Passo 2: fazer a cobrinha se mover 
partes_do_corpo = []
posições_iniciais = [(0,0),(-20,0),(-40,0)]
for i in posições_iniciais:
    cobrinha = t.Turtle(shape='square')
    cobrinha.color('gray10')
    cobrinha.penup()
    cobrinha.goto(i)
    partes_do_corpo.append(cobrinha)



jogo_rodando = True 

#esse pedaço de código vai fazer com que a cobrinha se mova para
#frente automaticamente
while jogo_rodando:
    tela.update()
    time.sleep(0.3)
    for parte in range(len(partes_do_corpo)-1,0,-1):
        posição_x = partes_do_corpo[parte-1].xcor()
        posição_y = partes_do_corpo[parte-1].ycor()
        partes_do_corpo[parte].goto(posição_x,posição_y)
    partes_do_corpo[0].forward(20)



tela.exitonclick()