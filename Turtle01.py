import turtle
x = turtle.Turtle()
x.speed(1)
for i in range(200, 10000, 100):
    x.forward(i)
    x.left(90)
    x.forward(i)
    x.right(90)
    x.backward(i)
    x.left(90)
    x.backward(i+100)
    x.pencolor('red')
    x.color('blue')
    x.filling()

turtle.done()