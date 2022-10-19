'''
작성일 : 2020. 12. 23
작성자 : 정성모
코드 개요 : 북쪽을 기준으로 360도 방향을 수치화
'''
from math import radians, sin, cos, atan2, degrees

s_lat = 36.991149299055195
s_lng = 127.92685004656414
e_lat = 36.99115305251849
e_lng = 127.92544558954162

def bearing(s_lat, s_lng, e_lat, e_lng):
        lat1 = radians(s_lat)
        lat2 = radians(e_lat)
        diffLong = radians(e_lng - s_lng)

        b_x = sin(diffLong) * cos(lat2)
        b_y = cos(lat1) * sin(lat2) - (sin(lat1) * cos(lat2) * cos(diffLong))
        initial_bearing = atan2(b_x, b_y)
        initial_bearing = degrees(initial_bearing)
        compass_bearing = (initial_bearing + 360) % 360 
        return int(compass_bearing)


test = bearing(s_lat, s_lng, e_lat, e_lng)
print(test)
