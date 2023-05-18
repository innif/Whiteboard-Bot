import keyboard
import requests

status = ""

def steer(pwr1, pwr2):
    try:
        requests.get(f"http://raspberrypi.local:5000/steer/{pwr1}/{pwr2}")
    except:
        print("fail")

def steer_motor(id, pwr):
    try:
        requests.get(f"http://raspberrypi.local:5000/motor/{id}/{pwr}")
    except:
        print("fail")

while True:
    key = keyboard.read_key() 
    if key == "w":
        steer(-100, 100)
    elif key == "a":
        steer(-100, -100)
    if key == "s":
        steer(100, -100)
    elif key == "d":
        steer(100, 100)
    elif key == "space":
        steer(0, 0)
    else:
        print(key)