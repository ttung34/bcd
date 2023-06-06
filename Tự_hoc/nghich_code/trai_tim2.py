import turtle

#Tao doi tuong turtle
t = turtle.Turtle()

#Dat ve toc do chay 
t.speed(10)

#Code mot nua trai tim
t.penup()
t.goto(-100,0)
t.pendown()
t.begin_fill()
t.color('red')
t.circle(100,180)
t.setheading(0)
t.circle(-100,180)
t.end_fill()

#Code mot nua trai tim con lai 
t.penup()
t.goto(-100,0)
t.pendown()
t.begin_fill()
t.color('red')
t.circle(-100,180)
t.end_fill()

#Dung phim bat ki de tat chuong trinh