# ViralSpiral.py
import turtle
t = turtle.Pen()
t.speed(0)
t.penup()
turtle.bgcolor("black")
sides = int(turtle.numinput("Number of sides",
                             "how many sides in your spiral of spirals? (2-12)", 12,2,12))
colors = ["red", "yellow", "blue", "green", "orange", "purple", "cyan", "navy", "salmon", "forest green", "magenta", "maroon",]
for m in range(1000):
    t.forward(m*1)
    position = t.position()
    heading = t.heading()
    print(position, heading)
    for n in range(int(m/2)):
        t.pendown()
        t.pencolor(colors[n%sides])
        t.forward(2*n)
        t.right(360/sides - 2)
        t.penup()
        t.width(n * sides /200)
    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360/sides + 2)
