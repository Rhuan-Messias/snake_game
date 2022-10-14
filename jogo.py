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
#tela.onkey(cobrinha.cima,"Cima")
#tela.onkey(cobrinha.baixo,"Baixo")
#tela.onkey(cobrinha.esquerda,"Esquerda")
#tela.onkey(cobrinha.direita,"Direita")


jogo_rodando = True 
while jogo_rodando:
    tela.update()
    time.sleep(0.3)
    cobrinha.mover() #chamamos o método movimento 
    #cobrinha.cima()




tela.exitonclick()