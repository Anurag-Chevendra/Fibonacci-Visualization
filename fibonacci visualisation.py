import turtle
win=turtle.Screen()
win.title("Fibonacci Visualization")
win.bgcolor("black")
t=turtle.Turtle()
tt=turtle.Turtle()
axis=turtle.Turtle()
en=turtle.Turtle()
axis.color("grey")
t.color("white")
t.hideturtle()
t.width(3)
fib=[]
en.speed(9)
en.width(2)
en.color("grey")
en.hideturtle()
x=[0]
y=[0]
def drawAxis(x,y):
    axis.clear()
    axis.hideturtle()
    axis.speed(8)
    axis.color("green")
    axis.width(2)
    for o in range(4):
        axis.penup()
        axis.goto(x, y)
        axis.pendown()
        axis.setheading(90 * o)
        axis.forward(50)



def diagram():
    rad=win.numinput("Input", "Max Radius:")
    mf=win.numinput("Input" , "Enter Multiplication Factor : (*this basically zooms in and out*)")
    tt.hideturtle()
    tt.speed(-1)
    tt.color("yellow")
    for i in range(4):
        tt.setheading(90 * i)
        tt.forward(800)
        tt.goto(0,0)
    fibonaci(0, 1 , rad)
    for i in range(len(fib)):
        en.penup()
        en.pendown()
        en.clear()
        t.width(3)
        t.pendown()
        en.circle(fib[i]*mf)
        t.circle(fib[i]*mf,90)
        t.color("red")
        x.append(t.pos()[0])
        y.append(t.pos()[1])
        drawAxis(x[1],y[1])
        t.width(2)
        t.penup()
        t.goto(x[0],y[0])
        t.pendown()
        t.goto(x[1],y[1])

        x.pop(0)
        y.pop(0)
        t.penup()
        t.color("white")
    en.clear()
    axis.clear()
    t.hideturtle()



def fibonaci(x1,x2,r):

    fib.append(x1+x2)
    if not (x1+x2)>=r :
        fibonaci(x2, x1 + x2,r)



diagram()

turtle.mainloop()