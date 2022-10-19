'''
작성일 : 2020. 12. 28.
작성자 : 정성모
코드개요 : 멀티프로세싱 test 코드- multiprocessing 모듈의 Pool을 이용한 비동기 멀티프로세싱
'''
from multiprocessing import Process, Pool
import time
import os

def a(y):
    time.sleep(5)
    print(y, os.getpid())

b = False

# with를 이용하여 pool을 생성하면 with를 벗어나는 순간 동작중인 process도 강제 종료
with Pool(5) as pool:
    for i in range(30):
        pool.apply_async(a, (i,))
    time.sleep(10)

time.sleep(10)
