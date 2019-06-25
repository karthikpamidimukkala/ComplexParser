import requests
import os
import sys
import urllib
import urllib2
import json

API_KEY ='XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

def google_api_matrix():
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        'units': 'imperial',
        'key': API_KEY,
        'origins': 'Dallas, TX',
        'destinations': 'Austin,TX',
        'mode': 'driving'
    }
    r = requests.get(url,params=params)
    final_url = url +'?'+ urllib.urlencode(params)
    print(final_url)
    response = str(urllib.urlopen(final_url).read())
    json_loads = json.loads(response.replace('\\n',''))
    if(json_loads["status"]=='OK'):
        print('The url got the response')
    print(json_loads)
    #print(response)
    return r.json()

a= google_api_matrix()
print(a)