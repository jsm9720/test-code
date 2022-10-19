'''
작성일 : 2020. 12. 28.
작성자 : 정성모
코드개요 : folium 모듈을 이용한 데이터 plot - html저장 및 주피터노트북의 실시간 plot 가능
'''
import folium
import json

map_osm = folium.Map(location=[37.566345, 126.977893])
rfile = open("./2019_09_20.geojson", "r", encoding="utf-8").read()
jsonData = json.loads(rfile)
folium.GeoJson(jsonData, name ="json_data").add_to(map_osm)
map_osm.save("./plot.html")
