import requests
import uuid
import time
from time import sleep
import picamera
import json
 
#url = "https://elecdesign.org.aalto.fi/tracker/api/"
url = "http://localhost:3000/tracker/api/"

id = str(uuid.uuid1())
 
oldTime = time.time()
 
while True:
    sleep(0.5)
    if time.time() - oldTime > 1:
        oldTime = time.time()
        response = requests.post(url, json={'uuid':id, 'c':1})
        print(response.text.encode('utf8'))
        if response.json()['msg'] == 'preview':
            #take image here
            response = requests.post(url, json={'uuid':id, 'msg':'preview'})
            print(response.text.encode('utf8'))
