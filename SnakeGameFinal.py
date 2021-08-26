#imports
import turtle
import time
import random

delay = 0.2  # Delay is to control snake speed

#scores
score = 0
high_score = 0

#set up screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor((0.63,0.78,0.85))
wn.setup(width=600, height=600)
wn.tracer(0)

# Draw Border 

t = turtle.Turtle()
t.color((0.8,0,0))
t.pensize(5)
t.hideturtle()
t.penup()
t.goto(-290,290) 
l = 580

t.pendown()
t.forward(l)
t.right(90)  
t.forward(l)
t.right(90) 
t.forward(l)
t.right(90) 
t.forward(l)
t.right(90) 

#snake head
head = turtle.Turtle()
head.speed(1)
head.shape("square")
head.color((0.06,0.39,0.83))
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food= turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#scoreboards
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("Score: 0  High score: 0  Speed: 0", align = "center", font=("consolas", 18, "normal"))

#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#keyboard controls (Arrow Keys)
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

#MainLoop
Gcolor = 0.99
eat_count = 0
lbord_speed = 1

while True:
    wn.update()

    #Collision on Border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        Gcolor = 0.99
        eat_count = 0
        lbord_speed = 1

        #Remove snakes body
        for segment in segments:
            segment.goto(1000,1000) 

        segments.clear()

        #reset score
        score = 0

        #reset delay
        delay = 0.2

        sc.clear()
        sc.write("Score: {}  High score: {}  Speed: {}".format(score, high_score,lbord_speed), align="center", font=("consolas", 18, "normal"))

    #Eating Food
    if head.distance(food) <20:

        eat_count += 1

        if eat_count % 2 == 0 :
            lbord_speed = int(eat_count/2) 
        else :
            lbord_speed = int(eat_count//2)

        # Make food appear at random places
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)

        #New segment after eating food
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        
        # Change color slightly for each segment 
        # So it look like a gradient
        Gcolor = Gcolor - 0.04
        if Gcolor < 0 :
            new_segment.color((0,0,0))
        else :
            new_segment.color((0,Gcolor,0)) 

        new_segment.penup()
        segments.append(new_segment)

        #shorten delay = Snake speed faster
        delay -= 0.005
        #increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        sc.clear()
        sc.write("Score: {}  High score: {}  Speed: {}".format(score,high_score,lbord_speed), align="center", font=("consolas", 18, "normal")) 

    #move the segments in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to head
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #Collision with tail 
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            Gcolor = 0.99
            eat_count = 0

            lbord_speed = 1 

            #hide segments
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.2

            # Scoreboard update 
            sc.clear()
            sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal"))

    time.sleep(delay)

wn.mainloop()   
