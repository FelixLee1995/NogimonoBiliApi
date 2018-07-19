import json
import os

def loadInterval():
    with open('conf.json', 'r') as json_f:
        json_dict = json.load(json_f)
        if json_dict['interval']:
            return json_dict['interval']
        else:
            return 20


def loadUpList():
    with open('conf.json', 'r') as json_f:
        json_dict = json.load(json_f)
        return json_dict['upList']


def loadStartTimeStamp():
    with open('conf.json', 'r') as json_f:
        json_dict = json.load(json_f)
        return json_dict['startTimestamp']

def loadMongoUrl():
    if os.environ.get('DB_HOST'):
        print(os.environ.get('DB_HOST'))
        return 'mongodb://'+str(os.environ.get('mongourl'))+':27017/'
    with open('conf.json', 'r') as json_f:
        json_dict = json.load(json_f)
        return json_dict['mongourl']
