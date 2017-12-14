import pymongo

HOST = 'localhost'
PORT = 27017
DB = 'test_db'
COLL = 'chat_list'

cli = None
coll = None
    
def init_mongodb():
    print('init_mongodb')
    global cli, coll
    cli = pymongo.MongoClient(host=HOST, port=PORT)
    db = cli[DB]
    coll = db[COLL]

def log_to_mongodb(nick, chat): # callback
    print('log_to_mongodb')
    global coll
    coll.insert_one({'nick': nick, 'chat': chat})

def close_mongodb():
    print('close_mongodb')
    global cli
    cli.close()