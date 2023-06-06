import turtle as t 
from time import sleep

def go_to(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    
def head(x,y,r):
    go_to(x,y)
    t.speed(20)
    t.circle(r)

def leg(x,y):
    t.right(90)
    t.forward(100)
    t.right(30)
    t.forward(100)
    t.left(120)
    go_to(x,y-180)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.left(120)
    hand(x,y)

def hand(x,y):
    go_to(x,y-180)
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.left(60)
    eye(x,y)

def eye(x,y):
    go_to(x-50,y+130)
    t.right(90)
    t.forward(50)
    t.go_to(x+40,y+130)
    t.forward(50)
    t.left(90)

def big_circle(size):
    t.speed(20)
    for i in range(150):
        t.forward(size)
        t.right(0.3)

def line(size):
    t.speed(10)
    t.forward(51*size)
    
def small_circle(size):
    t.speed(size)
    for i in range(210):
        t.forward(size)
        t.right(0.786)
        
def heart(x,y,size):
    go_to(x,y)
    t.left(150)
    t.begin_fill()
    line(size)
    big_circle(size)
    small_circle(size)
    t.left(120)
    small_circle(size)
    big_circle(size)
    line(size)
    t.end_fill()
    
def main():
    t.pensize(2)
    t.color('red', 'pink')
    head(-120, 100, 100)
    heart(250, -80, 1)
    go_to(100, -300)
    # <3
    t.done()
main()
       