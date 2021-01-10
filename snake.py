import turtle
import time
import random

posponer = 0.05

# Marcador
score = 0
high_score = 0

# Configuración de la ventana
main_screen = turtle.Screen()
main_screen.title('La viborita')
main_screen.bgcolor('black')
main_screen.setup(width=600, height=600)
main_screen.tracer(0)

# Cabeza de la snake
cabeza = turtle.Turtle() # Creo un objeto Turtle
cabeza.speed(0)
cabeza.shape('square')
cabeza.penup() # Quita el rastro
cabeza.goto(0,0) # (x, y)
cabeza.color('green')
cabeza.direction = 'stop'

# Cuerpo serpiente / Segmentos
segmentos = [] # Lista vacía

# Marcador
tablero = turtle.Turtle()
tablero.speed(0)
tablero.color('white')
tablero.penup()
tablero.hideturtle()
tablero.goto(0, 284)
tablero.write('Score: 0         High Score: 0', align='center', font=('Consolas', 12, 'normal'))

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.penup()
comida.goto(0,100)
comida.color('red')

# Funciones
def arriba():
    cabeza.direction = 'up'

def abajo():
    cabeza.direction = 'down'

def izquierda():
    cabeza.direction = 'left'

def derecha():
    cabeza.direction = 'right'

def movimiento():
    if cabeza.direction == 'up':
        y = cabeza.ycor() # Devuelve la coordenada del objeto
        cabeza.sety(y + 10)
    elif cabeza.direction == 'down':
        y = cabeza.ycor()
        cabeza.sety(y - 10)
    elif cabeza.direction == 'right':
        x = cabeza.xcor()
        cabeza.setx(x + 10)
    elif cabeza.direction == 'left':
        x = cabeza.xcor()
        cabeza.setx(x - 10)

def resetear_marcador():
    pass

# Eventos de teclado
main_screen.listen()
main_screen.onkeypress(arriba, 'Up') # 'Up' es la flecha del teclado
main_screen.onkeypress(abajo, 'Down')
main_screen.onkeypress(izquierda, 'Left')
main_screen.onkeypress(derecha, 'Right')

while True:
    main_screen.update()

    # Colisiones con los bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = 'stop'
        
        for segmento in segmentos:
            # segmento.goto(1000, 1000)
            segmento.hideturtle()

        segmentos.clear()

        # Reseteo marcador
        score = 0
        tablero.clear()
        tablero.write('Score: {}         High Score: {}'.format(score, high_score), 
            align='center', font=('Consolas', 12, 'normal'))

    if cabeza.distance(comida) < 20: # 20px es el tamaño default de los objetos
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle() # "Objeto" que agrego a la lista
        nuevo_segmento.speed(0)
        nuevo_segmento.shape('square')
        nuevo_segmento.penup()
        nuevo_segmento.color('green')
        segmentos.append(nuevo_segmento)

        # Aumento marcador
        score += 100
        if score > high_score:
            high_score = score

        tablero.clear()
        tablero.write('Score: {}         High Score: {}'.format(score, high_score), 
            align='center', font=('Consolas', 12, 'normal'))


    # Mover el cuerpo de la serpiente
    total_segmentos = len(segmentos)
    for index in range(total_segmentos -1, 0, -1):
        x = segmentos[index -1].xcor() # Obtengo coordenadas del segmento anterior
        y = segmentos[index -1].ycor()
        segmentos[index].goto(x, y)

    if total_segmentos > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    movimiento()

    # Colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 10:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = 'stop'

            # Esconder segmentos
            for segmento in segmentos:
                segmento.goto(1000, 1000)

            segmentos.clear()

            score = 0
            tablero.clear()
            tablero.write('Score: {}         High Score: {}'.format(score, high_score), 
                align='center', font=('Consolas', 12, 'normal'))

    time.sleep(posponer)

turtle.exitonclick()