# Python program to draw square
# using Turtle programming

### sin loop

from turtle import *

# shape("turtle")
# for i in range (4):
#     forward(500)
#     right(90)

# done()


# dibuja una estrella

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()