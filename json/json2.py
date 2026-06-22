# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file.

import json
import urllib.request

url = input('Enter location: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_2433914.json'

print('Retrieving', url)
info = json.loads(urllib.request.urlopen(url).read())
print('Retrieved',len(info),'characters')

print('User count:', len(info['comments']))
print('Sum:', sum([item['count'] for item in info['comments']]))
