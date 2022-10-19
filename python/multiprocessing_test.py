'''
작성일 : 2020. 12. 28.
작성자 : 정성모
코드개요 : 멀티프로세싱 test 코드- ProcessPoolExecutor를 이용한 멀티프로세싱
'''
from concurrent.futures import ProcessPoolExecutor
import time
import os

def task():
    print("Executing our Task on Process : {}".format(os.getpid()))

def main():
    executor = ProcessPoolExecutor(max_workers=4)

    task1 = executor.submit(task)
    task2 = executor.submit(task)

main()
