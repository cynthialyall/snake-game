# Simple Snake Game for Beginners in Python 3
# Using Turtle Module
import turtle
import random
import time

delay = 0.3

# Score
score = 0
high_score = 0
# setting the screen
win = turtle.Screen()
win.title('Snake Game')
win.bgcolor('black')
win.setup(width=600, height=600)
win.tracer(0) # turns off the screen update

# Snake head
head = turtle.Turtle()
head.shape('square')
head.color('green')
head.goto(0, 0)
head.penup()
head.speed(0) # animation speed
head.direction = 'stop'
# snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)

segment = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score: 0 | High Score: 0', align = 'center', font=('Courier', 24, "normal"))



# Functions
def go_up():
    if head.direction != 'down':
       head.direction = 'up'
def go_down():
    if head.direction != 'up':
      head.direction = 'down'
def go_left():
    if head.direction != 'right':
      head.direction = 'left'
def go_right():
    if head.direction != 'left':
      head.direction = 'right'
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)
# keyboard binding
win.listen()
win.onkeypress(go_up, 'Up')
win.onkeypress(go_down, 'Down')
win.onkeypress(go_left, 'Left')
win.onkeypress(go_right, 'Right')


while True:
    win.update()
    # check for border collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'
        for segments in segment:
            segment.goto(1000, 1000)
        segment.clear()

        score = 0
        delay = 0.4
        pen.clear()
        pen.write('Score: {} | High Score: {}'.format(score, high_score), align='center', font=('Courier', 24, "normal"))



    # Check for head collision with the food
    if head.distance(food) < 20:
        # Move to random
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        # add body to snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('green')
        new_segment.penup()
        segment.append(new_segment)
        # shorten the delay
        delay -= 0.01

        # increase the score
        score +=10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write('Score: {} | High Score: {}'.format(score, high_score), align='center', font=('Courier', 24, "normal"))


    # Move the end body in reverse order
    for index in range(len(segment)-1, 0, -1):
        x = segment[index-1].xcor()
        y = segment[index - 1].ycor()
        segment[index].goto(x, y)
    # Move the body 0 t where the head is
    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x, y)



    move()
    # Check for head collision with body/ segment
    for segments in segment:
        if segments.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'
            # hide the segment
            for segments in segment:
                segments.goto(1000, 1000)
            segment.clear()
    time.sleep(delay)

win.maingameloop()