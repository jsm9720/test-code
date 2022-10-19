'''
작성일 : 2020. 12. 28.
작성자 : 정성모
코드개요 : python 환경에서 accumulo 조작을 위한 pysharkbite 모듈 사용
           (GLIBC 2.29 버전이상 지원)
'''
import pysharkbite

zoo_instance = "dblab"
zookeepers = "dblab-node-01:2182,dblab-server-01:2182,dblab-server-02:2182,dblab-server-03:2182"
username = "root"
password = "1"

configuration = pysharkbite.Configuration()

zk = pysharkbite.ZookeeperInstance(zoo_instance, zookeepers, 1000, configuration)

user = pysharkbite.AuthInfo(username, password, zk.getInstanceId())

print(dir(pysharkbite))

try:
    connector = pysharkbite.AccumuloConnector(user, zk)
    table_operations = connector.tableOps("jsm_test")
    print(table_operations.exists(True))
except Exception as e:
    print("disconnect")
    print(e)
finally:
    connector.close()

print("end")

