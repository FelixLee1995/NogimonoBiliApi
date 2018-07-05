from pymongo import MongoClient
import pymongo
import loadconf
import json
import re

client = MongoClient(loadconf.loadMongoUrl())

db = client['dynamic']


def getDynamicTotalCount():
    dycol = db['dynamic']
    return dycol.find().count()


def getPaginationDynamic(index, size):

    dycol = db['dynamic']
    res = dycol.find().sort('timestamp', pymongo.DESCENDING).skip(index*size).limit(size)
    reslist = []
    if res.count() > 0:
        for item in res:
            item = str(item).encode('utf-8').decode('unicode_escape')


            reslist.append(str(item).replace('\\\\\\', '').replace('\\\\', ''))
        return reslist
    else:
        return -1
