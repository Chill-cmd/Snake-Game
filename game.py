import turtle
import time
import random

tiempo = 0.1

pag = turtle.Screen()
pag.title("Snake")
pag.bgcolor("blue")
pag.setup(width = 600, height = 600)
pag.tracer(0)

# Cuerpo de la serpiente (Head)
head = turtle.Turtle()
head.speed(0)
head.color("green")
head.shape("square")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Cuerpo de la manzana
food = turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.penup()
food.goto(0,100)

# Cuerpo
body = []

# ScoreBoard
barr = turtle.Turtle()
barr.color("white")
barr.speed(0)
barr.penup()
barr.hideturtle()
barr.goto(0,260)
barr.write("Score: 0         Best score: 0", align = "center", font =("Corrier", 24, "normal"))

reg = 0
hight_score = 0

# Variables
def arriba():
    head.direction = "up"
def abajo():
    head.direction = "down"
def derecha():
    head.direction = "right"
def izquierda():
    head.direction = "left"

def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Teclas 
pag.listen()
pag.onkeypress(arriba, "Up")
pag.onkeypress(abajo, "Down")
pag.onkeypress(izquierda, "Left")
pag.onkeypress(derecha, "Right")

while True:
    pag.update()

# Comida
    if head.distance(food) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)

        nuevo = turtle.Turtle()
        nuevo.speed(0)
        nuevo.color("green")
        nuevo.shape("square")
        nuevo.penup()
        body.append(nuevo)
    
# Registro
        reg += 10

        if reg > hight_score:
            hight_score = reg

        barr.clear()
        barr.write("Score: {}         Best score: {}".format(reg, hight_score), align = "center", font =("Corrier", 24, "normal"))

# Colision Bordes
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Esconder
        for seg in body:
            seg.goto(1000,1000)

        # Limpiar
        body.clear()
        reg = 0
        barr.clear()
        barr.write("Score: {}         Best score: {}".format(reg, hight_score), align = "center", font =("Corrier", 24, "normal"))

# Movimiento
    totalBody = len(body)
    for index in range(totalBody -1, 0, -1):
        x = body[index - 1].xcor()
        y = body[index - 1].ycor()
        body[index].goto(x,y)
    
    if totalBody > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)

    mov()

# Colision propia
    for seg in body:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Esconder
            for seg in body:
                seg.goto(1000,1000)

            body.clear()
            reg = 0
            barr.clear()
            barr.write("Score: {}         Best score: {}".format(reg, hight_score), align = "center", font =("Corrier", 24, "normal"))

    time.sleep(tiempo)
