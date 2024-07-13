# В1
# from turtle import * 
# tracer(0)
# screensize(2000, 2000)
# left(90)
# scale = 10

# x = 18
# for i in range(4):
#     forward(x*scale)
#     right(90)
#     forward(x*scale)
#     left(90)
#     forward(x*scale)
#     right(90)

# up()
# for i in range(-50, 50):
#     for y in range(-50, 50):
#         goto(i*scale, y*scale)
#         dot('red')
# done()

# for x in range(1, 100):
#     if (3 * x + 1) ** 2 - ((x + 1) ** 2) * 4 - 4 * (x - 1) >= 1500:
#         print(x)
#         break




#В2
# from turtle import * 
# tracer(0)
# screensize(2000, 2000)
# left(90)
# scale = 25

# for i in range(4):
#     forward(12 * scale)
#     right(90)
# for i in range(5):
#     forward(4 * scale)
#     right(45)

# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*scale, y*scale)
#         dot('red')
# done()


#B3
from turtle import * 
tracer(0)
screensize(2000, 2000)
left(90)
scale = 25

for i in range(3):
    forward(7 * scale)
    right(90)
forward(8 * scale)
for i in range(3):
    left(90)
    forward(5 * scale)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*scale, y*scale)
        dot('red')
done()
