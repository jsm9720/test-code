'''
작성일 : 2020. 12. 26.
장성자 : 정성모
코드개요 : haversine은 지구의 거리를 구하기 위한 모듈로 두 위도 경도를 통해 거리를 구함
'''
from haversine import haversine

x_min = 32.950424
y_min = 124.773835
x_max = 38.763189
y_max = 131.563393
x_d = x_max - x_min
y_d = y_max - y_min

h_x_d = 589*2
h_y_d = 647*2

per_x_cell = x_d/h_x_d
per_y_cell = y_d/h_y_d


point1 = (x_max, y_min)
point3 = (x_min, y_min)
point2 = (x_max, y_max)
point4 = (x_min, y_max)

print("point1 : ",point1)
print("point2 : ",point2)
print("point3 : ",point3)
print("point4 : ",point4)

km = haversine(point1, point3, unit='km')
print("p1_to_p3 : ",km)
km = haversine(point1, point2, unit='km')
print("p1_to_p2 : ",km)



