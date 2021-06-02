import turtle
import random

#Orientation
orientH = [0]

#Up
def u():
    if orientH[0] == 270:
        pass
    else:
        orientH[0] == 90

#Down
def d():
    if orientH[0] == 270:
        pass
    else:
        orientH[0] == 90

#Up
def u():
    if orientH[0] == 90:
        pass
    else:
        orientH[0] == 270

#Left
def l():
    if orientH[0] == 0:
        pass
    else:
        orientH[0] == 180

#Right
def r():
    if orientH[0] == 180:
        pass
    else:
        orientH[0] == 0



#score
scoreA = [0]
scoreB = [0]

#food
foodcoord = [0,0,0]

#position
pos = []

def home(x,y):
    x = 0
    y = 0
    scoreA[0]  = 0
    scoreB[0]  = 0
    orientH[0] = 0

    foodcoord[2] = 0
    pos[:] = [] 
    turtle.hideturtle()
    turtle.clear()
    turtle.pu()
    turtle.color("black")
    turtle.goto(0,0)
    turtle.write("Play")
    turtle.title("SnakePy")
    turtle.onscreenclick(start)
    turtle.mainloop()

def level_1():
    turtle.clear()
    turtle.pu()
    turtle.speed(0)
    turtle.pensize(20)
    turtle.color("grey")
    turtle.goto(-220,220)
    turtle.pd()
    turtle.goto(220,220)
    turtle.goto(220,-220)
    turtle.goto(-220,-220)
    turtle.goto(-220,220)
    turtle.pu()
    turtle.goto(0,0)

def start(x,y):
    turtle.onscreenclick(None)

    level_1()

    turtleFood = turtle.Turtle()    
    turtleFood.hideturtle()
    turtleFood.pu()
    turtleFood.speed(0)
    turtleFood.shape("square")
    turtleFood.color("red")

    turtleScore = turtle.Turtle()
    turtleScore.hideturtle()
    turtleScore.pu()
    turtleScore.speed()
    turtleScore.goto(100,-250)
    turtleScore.write("Score:" +str(scoreA[0]), align="center", font=(10))

    while x > -210 and x < 210 and y > -210 and y < 210:
        if foodcoord[2] == 0:
            food(turtleFood)
            foodcoord[2] = 1
        turtle.onkey(u, "Up")
        turtle.onkey(l, "Left")
        turtle.onkey(r, "Right")
        turtle.onkey(d, "Down") 
        turtle.listen()
        move()
        x = turtle.xcor()
        y = turtle.ycor()

        if x > foodcoord[0]*20-5 and x < foodcoord[0]*20+5 and y > foodcoord[1]*20-5 and y < foodcoord[1]*20+5:
            foodcoord[2] = 0
            turtleFood.clear()
            scoreA[0] += 1
            turtleScore.clear()
            turtleScore.write("Score:" + str(scoreA[0]), align = "center", font=(10))

        if len(pos) > 1:
            for i in range(1, len(pos)):
                if x < pos[i][0]+5 and x > pos[i][0]-5 and y < pos[i][1]+5 and y > pos[i][1]-5:
                    turtleScore.clear()
                    turtleFood.clear()
                    gameover()
    
    turtleScore.clear()
    turtleFood.clear()
    gameover()

#food
def food(turtlefood):
    x = random.randrange(-8,8,1)
    y = random.randrange(-8,8,1)
    foodcoord[0] = x
    foodcoord[1] = y
    turtlefood.hideturtle()
    turtlefood.pu()
    turtlefood.shape("square")
    turtlefood.color("red")
    turtlefood.goto(x*20, y*20)
    turtlefood.stamp()

def move():
    turtle.pensize(1)
    turtle.color("black")
    turtle.pu()
    turtle.speed(3)
    turtle.setheading(orientH[0])
    turtle.shape("square")
    turtle.stamp()
    turtle.fd(20)
    x = turtle.xcor()
    y = turtle.ycor()
    if scoreB[0] > scoreA[0]:
        turtle.clearstamps(1)
        pos.insert(0, [round(x), round(y)])
        pos.pop(-1)
    else:
        pos.insert(0, [round(x), round(y)])
        scoreB[0] += 1

def gameover():
    turtle.onscreenclick(None)
    turtle.speed(0)
    turtle.pu()
    turtle.goto(0,150)
    turtle.color("red")
    turtle.write("Game Over", align="center", font=(10))
    turtle.goto(0,50)
    turtle.write("Score:" + str(scoreA[0], align="center", font=(10)))
    turtle.goto(200,-200)
    turtle.write("(Click to return to the main menu", align="right", font=(0.0000001))
    turtle.onscreenclick(home)
    turtle.mainloop()

# if __name__ == '__main':
#     home(0,0)






