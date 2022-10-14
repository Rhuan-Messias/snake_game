import turtle as t

tela = t.Screen()
tela.setup(width=600, height=600) #keyword arguments, quando o parâmetro recebe as informações, onde azul é o parametro e a o numero é o argumento chave
tela.bgcolor('green')
tela.title('Jogo da Cobrinha')
tela.tracer(0)

#Passo 1: criar o corpo cobrinha 
#Passo 2: fazer a cobrinha se mover 
partes_do_corpo = []
posições_iniciais = [-40,-20,0]
for i in posições_iniciais:
    cobrinha = t.Turtle(shape='square')
    #cobrinha.color('gray10')
    cobrinha.penup()
    cobrinha.goto(i,0)
    partes_do_corpo.append(cobrinha)

tela.update()

jogo_rodando = True 

while jogo_rodando:
    for parte in partes_do_corpo:
        parte.forward(20)

















tela.exitonclick()