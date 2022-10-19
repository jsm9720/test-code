'''
작성일 : 2020. 12. 23.
작성자 : 정성모
코드 개요 : .gz 파일을 압축해제 없이 사용하기 위한 test 코드
'''

import fileinput
import json

# with open('TB_TRACKING2_DATA_20200222.sql.gz','r') as fr:
#     line=fr.readline().decode("utf-8")
#     print(line)
            
load_path = 'TB_TRACKING2_DATA_20200222.sql.gz'
data = fileinput.input(load_path, mode ="r", openhook=fileinput.hook_compressed)
for i in data:
    line=i.decode("utf-8")
    
    for j in range(1,len(line[49:-3].split("\'"))-1):
        if j % 6 == 0:
            try:
#                print(line[49:-3].split("\'")[j-1])
#                print(line[49:-3].split("\'")[j-1].replace("\\",""))
                break
                
            except Exception as e:
                print(e)
    break
    
