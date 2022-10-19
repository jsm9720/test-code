'''
작성일 : 2020. 12. 28
작성자 : 정성모
코드개요 : segemnt와 주어진 프인트가 직교하는 포인트를 찾고, 직교하는 포인트와 주어진 포인트의 거리를 구함
           (segment와 주어진 포인트의 가장 최단거리)
'''
from haversine import haversine
x1 = 2
y1 = 2 
x2 = 3
y2 = 3
x3 = 4
y3 = 4

def point_in_seg(x1, y1, x2, y2, x3, y3):
    f_a = ((y2-y1)/(x2-x1))
    f_b = ((y2-y1)/(x2-x1))*-x1+y1

    a = -f_a**-1
    b = f_a**-1*x3+y3

    x = (b-f_b)/(f_a-a)
    y = a*x+b

    return x, y


x, y = point_in_seg(x1, y1, x2, y2, x3, y3)
point1 = (x3, y3)
point2 = (x, y)
print(x, y)
display = haversine(point1, point2, unit = 'm' )
print(display)
