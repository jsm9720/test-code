from pymongo import MongoClient

# 충북대 농진청 DB 접속
mongodb_URL = "mongodb://203.255.77.162:27017"
client = MongoClient(mongodb_URL)

# 데이터베이스 리스트
#print(client.list_database_names())

# DB 접근
#db = client.tomato
db = client['tomato']
col = db['TomatoFruit']

print(col.count())
