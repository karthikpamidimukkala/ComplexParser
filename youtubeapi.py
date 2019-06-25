import urllib
import json
import sys

API_KEY ='XXXXXXXXXXXXXXXXXXXXXXXXXXXXx'
url ='https://www.googleapis.com/youtube/v3/channels'

params = {'part': 'snippet,contentDetails,statistics','forUsername': 'CaseyNeistat', 'key': API_KEY}


final_url = url+'?'+urllib.urlencode(params)

a = urllib.urlopen(final_url).read()
print(a)


print(final_url)
