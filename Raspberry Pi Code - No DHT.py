
import RPi.GPIO as GPIO
from time import sleep
import datetime
from firebase import firebase
import Adafruit_DHT

import urllib2, urllib, httplib
import json
import os 
from functools import partial

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
#sensor = Adafruit_DHT.DHT11

# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
pin = 4

# Try to grab a sensor reading. Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
#humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


firebase = firebase.FirebaseApplication('https://YOUR_FIREBASE_URL.firebaseio.com/', None)
#firebase.put("/dht", "/temp", "0.00")
#firebase.put("/dht", "/humidity", "0.00")

current_temp = 0
target_temp = 0

def update_firebase():

    #humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    #if humidity is not None and temperature is not None:
    #    sleep(5)
    #    str_temp = ' {0:0.2f} *C '.format(temperature) 
    #    str_hum = ' {0:0.2f} %'.format(humidity)
    #    print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity)) 

    #else:
    #    print('Failed to get reading. Try again!') 
    #    sleep(10)


    temperature = 25 #change this when DHT working

    firebase.put("/users", "/gaZcDfg5rcRyjaUfvaMzqGb0Arx1", "/ct", temperature)

    current_temp = temperature

def get_target_temp():

    target_temp = firebase.get("/users/gaZcDfg5rcRyjaUfvaMzqGb0Arx1/tt")

def heating():
    if 18 > current_temp:
        print("Turn heating on")
    else if target_temp <  current_temp:
        print("Turn heating on")
    else:
        ("Turn heating off")

while True:
    update_firebase()
    
    sleep(5)

    get_target_temp()

    sleep(5)

    heating()

    #sleepTime = int(sleepTime)
    sleep(5)
