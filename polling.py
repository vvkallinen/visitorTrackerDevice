import requests
import uuid
import time
from time import sleep
from picamera import PiCamera
import json

camera = PiCamera()
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
            #camera.start_preview()
            #sleep(5)
            camera.capture('./previews/{}.jpg'.format(id))
            #camera.stop_preview()
            files = {'file':open('./previews/{}.jpg'.format(id),'rb')}
            response = requests.post(url, files=files)
            print(response.text.encode('utf8'))
