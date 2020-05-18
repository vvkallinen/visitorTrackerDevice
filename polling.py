import requests
import uuid
import time
from time import sleep
#from picamera import PiCamera
import json
import cv2

#url = "https://elecdesign.org.aalto.fi/tracker/api/"
url = "http://localhost:3000/tracker/api/"
#url = "http://192.168.2.36:3000/tracker/api/"

#camera = PiCamera()
camera = cv2.VideoCapture(0)

id = str(uuid.getnode())
 
oldTime = time.time()
 
while True:
    sleep(0.5)
    if time.time() - oldTime > 1:
        oldTime = time.time()
        response = requests.post(url, json={'uuid':id, 'c':1})
        print(response.text.encode('utf8'))
        if response.json()['msg'] == 'preview':
            #camera.capture('./previews/{}.jpg'.format(id))
            ret, frame = camera.read()
            cv2.imwrite('./previews/{}.jpg'.format(id), frame)
            files = {'file':open('./previews/{}.jpg'.format(id),'rb')}
            response = requests.post(url, files=files)
            print(response.text.encode('utf8'))
