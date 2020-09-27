import json

import requests

ENDPOINT = "http://127.0.0.1:8000/status/"


def do(method='get',  data={}, is_json =True):
    headers = {}

    if is_json:
        data = json.dumps(data)
        headers['content-type']  ='application/json'
    print(data)
    r = requests.request(method, ENDPOINT, data=data,headers=headers)
    print(r.text)
    print(r.status_code)
    print(r.headers,"====ehader")
    
    return r



do( data = { 'id':44 })


#r = requests.request("get", ENDPOINT+"?id="+str(id), data = { 'id':12})