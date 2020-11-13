"""importing turtle module"""
import turtle
import time
import random
"""set the time delay"""
delay = 0.1

score = 0
high_score = 0
"""setting up window"""
wn = turtle.Screen()
wn.title("BUG Game play for fun") 
wn.bgcolor("Black")
wn.setup(width=700, height =700)
#wn.tracer(0)            #turn off the animation

"""display"""
disp = turtle.Turtle()
disp.speed(0)
disp.shape("square")
disp.color('white')
disp.penup()
disp.goto(0,290)
disp.write("Score: 0 High Score: 0", align = "center", font =("Courier", 20, "italic"))
disp.hideturtle()


"""snake head"""
head = turtle.Turtle()
head.color('brown')
head.shape('turtle')
head.speed(0)
head.penup()
head.goto(0,0)
head.direction = "stop"
head.shapesize(1, 1)
body = []

"""For Food"""

apples = turtle.Turtle()
apples.speed(0)
shapes= random.choice(["circle"])
colors = random.choice(['pink','green', 'blue'])
apples.penup()
apples.goto(1,100)
apples.shape(shapes)
apples.color(colors)
apples.shapesize(0.80, 0.80)

""" functions"""
def go_up():
    if head.direction != "down":   #it won't work in reverse direction 
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

""" snake moving functions"""
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+18)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-18)

    if head.direction == "left":
        x= head.xcor()
        head.setx(x-18)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+18)

"""keyboard bindings"""
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

"""Game loop"""
#repeats over and over again
while True:    
    wn.update()

    """checking for touching the food"""
    if head.distance(apples)<15:
        """move the food to the random spot"""
        x = random.randint(-340, 340)
        y = random.randint(-340, 340)
        apples.goto(x, y)

        """Adding  segments"""
        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.shape('square')
        new_part.color('pink')
        new_part.shapesize(.80, .80)
        new_part.penup()
        body.append(new_part)
        #delay -= 0.001
        
        """incrementing the score"""
        score += 10
        if score>high_score:
            high_score=score


        disp.clear()
        disp.write("Score: {} High Score: {}".format(score, high_score), align = "center", font =("Courier", 20, "italic"))

    # Check for border collision
    if head.xcor() > 340 or head.xcor() < -340 or head.ycor() > 340 or head.ycor() < -340:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        colors = random.choice(['red','green', 'blue'])
        shapes= random.choice(["circle",'square', 'triangle'])
        """Hiding the segments"""
        for segment in body:
            segment.goto(1000, 1000)

        """clear the parts in body"""
        body.clear()

        """reset the score"""
        score = 0

        """reset the delay"""
        delay = 0.1
        
        """updating the high_score"""
        disp.clear()
        disp.write("Score: {} High Score: {}".format(score, high_score), align = "center", font =("Courier", 20, "italic"))



    """move the last segments in reverse order"""
    for i in range(len(body)-1, 0, -1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x, y)


    """move seg 0 to where head is located"""
    if len(body)>0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)

    move()
    """for Body Collisions"""
    for segment in body:
        if segment.distance(head) <15:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            for segment in body:                #hide the parts of body
                segment.goto(1000, 1000)
            body.clear()                        #clear body list

            """reset the score"""
            score = 0
        
            """updating the high_score"""
            disp.clear()
            disp.write("Score: {} High Score: {}".format(score, high_score), align = "center", font =("Courier", 20, "italic"))


    time.sleep(delay)
wn.mainloop()      #code will be between tracer and mainloop

