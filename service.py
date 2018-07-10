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
    key = {'type': 8}
    res = dycol.find(key).sort('timestamp', pymongo.DESCENDING).skip(index*size).limit(size)
    reslist = []
    if res.count() > 0:
        print(res[0])
        for item in res:
            item.pop('_id')
            res = str(item).replace('\\\\\\', '').replace('\\\\', '')
            dict_a = eval(res)
            out = {}
            # if dict_a['type'] != 8:
            #     continue
            out['upname'] = dict_a['user_profile']['info']['uname']
            out['upid'] = dict_a['user_profile']['info']['uid']
            out['upface'] = dict_a['user_profile']['info']['face']
            out['timestamp'] = dict_a['timestamp']
            out['url'] = 'https://www.bilibili.com/video/av' + str(dict_a['rid'])
            print(str(dict_a['card']))
            card = eval(str(dict_a['card']))
            out['title'] = card['title']
            out['desc'] = card['desc']
            out['pic'] = card['pic']
            reslist.append(out)
        return reslist
    else:
        return -1
