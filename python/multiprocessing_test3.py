'''
작성일 : 2020. 12. 28.
작성자 : 정성모
코드개요 : 멀티프로세싱 test 코드- multiprocessing Pool의 close(), join() 테스트
'''
from multiprocessing import Process, Pool
from queue import Queue

import time
import os


count = 0
while True:
    pool = Pool(20)
    while True:
        if count == 5000:
            count = 0
            pool.close() # 더이상 작업을 할당하지 않게 close 함
            pool.join() #join을 사용하여 멀티프로세스에 남아있는 작업들을 기다림
            print("que size :",que.qsize())
            break
        value = que.get() # 자원을 쓰지않으며 대기 상태
        count += 1
        pool.apply_async(mapping, (value,))

        if count % 1000 == 0:
            print(count, que.qsize())

'''
count가 5000일떄, break로만 멈췄을 경우
- 새로운 pool이 만들어져 위와 같은 겨우에는 총 40개의 프로세스가 동작하게 됨
- 메모리를 너무 많이 사용하게 됨
10000개 처리
소요시간 : 약 2분
처리 데이터 : 약 327292
메모리 : 약 30G까지 올라갔음

count가 5000일때, join 사용한 경우
- close와 join을 사용하여 이전 작업하던 pool이 다 끝날때 까지 기다림
10000개 처리
소요시간 : 약 2분
처리 데이터 : 약 327227, 329361
메모리 : 약 15 ~ 16G 유지

count 1000일때, pool 파라미터인 maxtasksperchild 이용한 경우
- maxtasksperchild를 이용하여 총 pool이 할당 프로세스에서 처리 할 횟수 지정
- ex) pool(5, maxtasksperchild=2) 프로세스 5개가 작업을 2번씩 하고 다른 프로세스로 변경
- 하나의 pool을 계속 사용하다 보면 파이썬의 GC의 문제로 계속해서 메모리가 사용량이 증가 함
10000개 처리
소요시간 : 약 2분 10초
처리 데이터 : 약 327228
메모리 : 약 8 ~ 9G 유지

count 5000일때, pool 파라미터인 maxtasksperchild 이용한 경우
10000개 처리
소요시간 : 약 2분
처리 데이터 : 약 327295
메모리 : 약 15 ~ 16G 유지
'''
