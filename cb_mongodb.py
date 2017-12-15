import pymongo
import unittest

HOST = 'localhost'
PORT = 27017
DB = 'test_db'
COLL = 'chat_list'

cli = None
coll = None

def init_mongodb():
    print('init_mongodb')
    global cli, coll
    cli = pymongo.MongoClient(host=HOST, port=PORT, serverSelectionTimeoutMS=1000)
    db = cli[DB]
    coll = db[COLL]

def log_to_mongodb(nick, chat): # callback
    print('log_to_mongodb')
    coll.insert_one({'nick': nick, 'chat': chat})

def close_mongodb():
    print('close_mongodb')
    cli.close()

class TestMongodb(unittest.TestCase):
    def test_log(self):
        init_mongodb()
        log_to_mongodb('nick', 'chat')
        close_mongodb()

if __name__ == '__main__':
    unittest.main()
