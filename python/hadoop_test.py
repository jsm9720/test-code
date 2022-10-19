'''
작성일 : 2020. 12. 24
작성자 : 정성모
코드 개요 : python code 에서 hdfs 사용
'''
from hdfs import InsecureClient
import csv
import json
import time
import sys

def main():
    csv.field_size_limit(1000000000)

    # namenode url
    client_hdfs = InsecureClient("http://192.168.1.17:50070")

    print(client_hdfs.list("/"))
    '''
    read_path = "/wedrive_data/proc_01_parsed_line/data_%s.csv" % 20200301
    with client_hdfs.read(read_path,encoding="utf-8") as r:
        r_data = csv.reader(r)
        count = 0
        start = time.time()
        
        for i in r_data:
            join_data = ','.join(i[2:])
            print(type(join_data))
           # json_data = json.loads(join_data)
            break
            if count % 10000 == 0:
                print(count)
            count+=1
        print(time.time()-start)
        
        # next or for 속도 차이는 없음
        while True:
            try:
                data = next(r_data)[2:]
                join_data1 = json.loads(','.join(data))
                print(type(join_data1))
                break
                if count % 10000 == 0:
                    print(count)
                count += 1
            except StopIteration:
                print(time.time()-start)
                sys.exit(0)
        
    '''
main()
