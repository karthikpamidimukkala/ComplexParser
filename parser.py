import os;
import sys;
import re;
import time;
import json;
import requests

sys.setdefaultencoding('utf-8')


f = open('C:\Users\karth\OneDrive\Desktop\complex.json','r');


#a= f.readlines()
#print(a)
y =''
for i in f:
    y = y + i



z ={}
z= y


x_json = json.loads(z)



def extract_values(obj,key):
    arr =[]

    def extract(obj,arr,key):
        if isinstance(obj, dict):
            for k,v in obj.items():
                if isinstance(v,(dict,list)):
                    extract(v,arr,key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj,list):
            for item in obj:
                extract(item,arr,key)
        return arr

    results = extract(obj,arr,key)
    return results

json_results = extract_values(x_json,"destination_addresses")

print(x_json.keys())
print(type(json_results))
print(json_results)

print(x_json.get('destination_addresses'))

