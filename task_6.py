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
# from turtle import * 
# tracer(0)
# screensize(2000, 2000)
# left(90)
# scale = 25

# for i in range(3):
#     forward(7 * scale)
#     right(90)
# forward(8 * scale)
# for i in range(3):
#     left(90)
#     forward(5 * scale)

# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*scale, y*scale)
#         dot('red')
# done()



# Повтори 7 [Вперёд 4 Направо 90 Вперёд 3 Направо 90] 
# from turtle import * 
# tracer(0)
# screensize(2000, 2000)
# left(90)
# scale = 25

# for i in range(7):
#     forward(4 * scale)
#     right(90)
#     forward(3 * scale)
#     right(90)

# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*scale, y*scale)
#         dot('red')
# done()



# Повтори 9 [Вперёд 22 Направо 90 Вперед 6 Направо 90]
# Поднять хвост
# Вперед 1 Направо 90 Вперёд 5 Налево 90
# Опустить хвост
# Повтори 9 [Вперёд 53 Направо 90 Вперёд 75 Направо 90]
# Определите периметр области пересечения фигур, ограниченных заданным
# алгоритмом линиями.
# from turtle import*
# tracer(0)
# screensize(2000, 2000)
# scale = 25

# left(90)
# down()

# for i in range(9):
#     forward(22 * scale)
#     right(90)
#     forward(6 * scale)
#     right(90)
# up()
# forward(1 * scale)
# right(90)
# forward(5 * scale)
# left(90)
# down()
# for i in range(9):
#     forward(53 * scale)
#     right(90)
#     forward(75 * scale)
#     right(90)
# up()

# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * scale, y * scale)
#         dot('red')
# done()



# Повтори 9 [Вперёд 29 Направо 90 Вперёд 17 Направо 90]
# Поднять хвост
# Вперёд 5 Направо 90 Вперёд 1 Налево 90
# Опустить хвост
# Повтори 9 [Вперёд 64 Направо 90 Вперёд 48 Направо 90]
# from turtle import*
# tracer(0)
# screensize(2000,2000)
# scale = 25
# left(90)

# for i in range(9):
#     forward(29 * scale)
#     right(90)
#     forward(17 * scale)
#     right(90)
# up()
# forward(5 * scale)
# right(90)
# forward(1 * scale)
# left(90)
# down()
# for i in range(9):
#     forward(64 * scale)
#     right(90)
#     forward(48 * scale)
#     right(90)
# up()

# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * scale, y * scale)
#         dot('red')
# done()



# Повтори 5 [Вперёд 9 Направо 90 Вперёд 3 Направо 90]
# from turtle import*
# tracer(0)
# screensize(2000, 2000)
# scale = 25
# left(90)

# for i in range(5):
#     forward(9*scale)
#     right(90)
#     forward(3*scale)
#     right(90)
# up()

# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x*scale, y*scale)
#         dot('red')
# done()



# Направо 90 Повтори 4 [Вперёд 4sqrt5 Направо 150 Вперёд 4sqrt5  Направо 300]
from turtle import*
from math import*
tracer(0)
screensize(2000, 2000)
scale = 25
left(90)

right(90)
for i in range(4):
    forward(4*sqrt(5)*scale)
    right(150)
    forward(4*sqrt(5)*scale)
    right(300)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*scale, y*scale)
        dot('red')
done()