'''
작성일 : 2020. 12. 28.
작성자 : 정성모
코드개요 : pyaccmulo 모듈 (python 2.x버전만 지원) 
'''
from pyaccumulo import Accumulo, Mutation, Range
conn = Accumulo(host="my.proxy.hostname", port=50096, user="root", password="secret")
