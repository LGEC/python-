import turtle

turtle.home()
# 当前位置(0,0)开始逆时针画半径为30的圆
turtle.circle(30)
# 逆时针画半径为50的半圆
turtle.circle(50,180)
# 方向值为180，“standard”模式时方向向左，“logo”模式方向向下
print(turtle.heading())
turtle.circle(-50,180)
print(turtle.heading())
# 逆时针方向半径为40画五边形(5步画接近整圆的图形)
turtle.circle(40,None,5)