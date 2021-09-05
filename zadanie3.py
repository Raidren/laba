from math import sqrt
x1=int(input('x1 = '))
y1=int(input('y1 = '))
x2=int(input('x2 = '))
y2=int(input('y2 = '))
x3=int(input('x3 = '))
y3=int(input('y3 = '))
x4=int(input('x4 = '))
y4=int(input('y4 = '))
if sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) == sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2) and sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2) == sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2) and sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2) == sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2):
    print('Точки являются вершинами квадрата')
else:
    print('Эти точки не вершины квадрата!')

