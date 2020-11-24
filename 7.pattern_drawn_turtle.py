#"A nautilus shape"
from turtle import *
penup()
goto(0,-60)
pendown()
speed('fastest')
size=1

while size < 255:
    for _ in range(4):
          forward(size)
          right(90)
          size=size + 1
    right(10)

done()
