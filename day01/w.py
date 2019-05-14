import turtle

screen = turtle.getscreen()
screen.title('tuttle练习')

# 跑道绘制
turtle.pensize(4)
turtle.pencolor('red')
turtle.home()
turtle.circle(50,180)
turtle.fd(100)
turtle.lt(90)
turtle.rt(90)
turtle.circle(50,180)
turtle.fd(100)
turtle.lt(90)

# 画笔抬起
turtle.pu()

turtle.setpos(0,-150)

# 画笔按下
turtle.pd()

# M绘制
turtle.pencolor('#50A14F')
turtle.rt(30)
turtle.fd(100)
turtle.rt(120)
turtle.fd(120)
turtle.lt(120)
turtle.fd(120)
turtle.rt(120)
turtle.fd(100)
turtle.mainloop()