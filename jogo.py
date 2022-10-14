import turtle as t
import cobra as c
import time

tela = t.Screen()
tela.setup(width=600, height=600) #keyword arguments, quando o parâmetro recebe as informações, onde azul é o parametro e a o numero é o argumento chave
tela.bgcolor('green')
tela.title('Jogo da Cobrinha')
tela.tracer(0)

cobrinha = c.Cobrinha() #vai rodar o __init__, criando a cobrinha com 3 segmentos

tela.listen()
#precisa ser em inglês, para indicar que são as setinhas 
tela.onkey(cobrinha.cima,"Up")
tela.onkey(cobrinha.baixo,"Down")
tela.onkey(cobrinha.esquerda,"Left")
tela.onkey(cobrinha.direita,"Right")


jogo_rodando = True 
while jogo_rodando:
    tela.update()
    time.sleep(0.3)
    cobrinha.mover() #chamamos o método movimento 
    #cobrinha.cima()




tela.exitonclick()